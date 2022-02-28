import json
import os
import queue
import re
import subprocess
import sys
import threading
import time

import psutil
import PyQt5
from gui import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, QUrl, pyqtSlot
from PyQt5.QtGui import QCursor, QIcon
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWidgets import *


class gui(QWidget,Ui_MainWindow):
  '''主窗口'''
  def __init__(self, parent=None):
    '''主窗口设置'''
    super(gui, self).__init__(parent)
    self.setupUi(self)
    global consolePath,forms,datas
    self.setWindowTitle("Dylan_"+VERSION)
    self.tabWidget.setCurrentIndex(0)
    self.enableColorfulLog.setChecked(datas["setting"]["enable_colorful_log"])
    self.compatibilityMode.setChecked(datas["setting"]["compatibility_mode"])
    self.filepath.setText(datas["setting"]["path"])
    consolePath="file:///"+str(consolePath).replace('\\',"/")
    self.console.load(QUrl(consolePath))
    channel.registerObject("obj", factorial)
    self.console.page().setWebChannel(channel)
    self.input.setDisabled(True)
    self.start.setDisabled(False)
    self.restart.setDisabled(True)
    self.stop.setDisabled(True)
    self.forcestop.setDisabled(True)
    self.regularlist.customContextMenuRequested.connect(self.createRegularMenu)
    self.loadRegular()
    self.start.clicked.connect(lambda: self.serverControl(1))
    self.selectfile.clicked.connect(lambda: self.selectFile())
    self.stop.clicked.connect(lambda: self.serverControl(2))
    self.input.returnPressed.connect(self.transferCommand)
    forms={
      "console":self.console,
      "input":self.input,
      "start":self.start,
      "stop":self.stop,
      "restart":self.restart,
      "forcestop":self.forcestop,
      "state":self.state_2,
      "version":self.version_2,
      "gamemode":self.gamemode_2,
      "difficulty":self.difficulty_2,
      "levelname":self.levelname_2,
      "port":self.port_2,
      "ram":self.ram_2,
      "cpu":self.cpu_2,
      "filepath":self.filepath,
      "enableColorfulLog":self.enableColorfulLog,
      "compatibilityMode":self.compatibilityMode,
      "regularlist":self.regularlist
      }

  def addSingelRegular(self,type=str):
    '''读取时添加正则记录'''
    if type=="disabled":
      typeIndex=0
    elif type=="private_admin":
      typeIndex=1
    elif type=="private":
      typeIndex=2
    elif type=="group_admin":
      typeIndex=3
    elif type=="group":
      typeIndex=4
    for i in datas["regular"][type]:
      self.regularlist.insertRow(0)
      captureArea=QComboBox()
      captureArea.addItems(["禁用","私聊（管理）","私聊（所有）","群聊（管理）","群聊（所有）"])
      captureArea.setCurrentIndex(typeIndex)
      self.regularlist.setCellWidget(0, 0, captureArea)
      self.regularlist.setItem(0,1,QTableWidgetItem(i["regular"]))
      self.regularlist.setItem(0,2,QTableWidgetItem(i["remark"]))
      self.regularlist.setItem(0,3,QTableWidgetItem(i["command"]))

  def loadRegular(self):
    '''加载正则记录'''
    self.addSingelRegular("group")
    self.addSingelRegular("group_admin")
    self.addSingelRegular("private")
    self.addSingelRegular("private_admin")
    self.addSingelRegular("disabled")
  
  def removeAllReg(self):
    '''删除所有正则记录'''
    reply = QMessageBox.warning(
      self,
      'Dylan',
      "确定要清空所有记录吗？\n他们将会永远失去！（真的很久！）",
      QMessageBox.Yes | QMessageBox.No, 
      QMessageBox.No
      )
    if reply == QMessageBox.Yes:
      for i in range(self.regularlist.rowCount()):
        self.regularlist.removeRow(0)

  def reloadRegular(self):
    '''重载正则记录'''
    for i in range(self.regularlist.rowCount()):
      self.regularlist.removeRow(0)
    self.loadRegular()

  def transferCommand(self):
    '''转发输入命令'''
    text=self.input.text()
    outputCommand(text)
    self.input.setText("")

  def serverControl(self,type):
    '''服务器控制按钮'''
    global state
    if type==1 and state!=1:
      if not os.path.exists(datas["setting"]["path"]):
        print("启动目标文件不存在")
      else:
        state=1
        self.start.setDisabled(True)
        self.stop.setDisabled(False)
        # self.restart.setDisabled(False)
        # self.forcestop.setDisabled(False)
        self.input.setDisabled(False)
    elif type==2:
      outputCommand("stop")

  def selectFile(self):
    '''选择启动文件'''
    startFile=QFileDialog.getOpenFileName(self, "选择文件",selfPath, "可启动文件 (*.exe *.bat *.cmd)")
    if startFile[0]!='':
      self.filepath.setText(startFile[0])
      print(startFile)
  
  def createRegularMenu(self,pos):
    '''创建正则管理页面的右键菜单'''
    item = self.regularlist.indexAt(pos)
    row=item.row()
    self.regularMenu = QMenu(self.regularlist)
    self.addRegular = QAction('添加记录',self.regularlist)
    self.regularMenu.addAction(self.addRegular)
    self.removeRegular = QAction('删除记录',self.regularlist)
    self.regularMenu.addAction(self.removeRegular)
    self.removeAllRegular = QAction('清空记录',self.regularlist)
    self.regularMenu.addAction(self.removeAllRegular)
    self.regularMenu.addSeparator()
    self.refreshRegular = QAction('刷新',self.regularlist)
    self.regularMenu.addAction(self.refreshRegular)
    if row==-1:
      self.removeRegular.setDisabled(True)
    if self.regularlist.rowCount()<=0:
      self.removeAllRegular.setDisabled(True)
    self.addRegular.triggered.connect(lambda: self.regularManagement(1))
    self.removeRegular.triggered.connect(lambda: self.regularManagement(2,row))
    self.refreshRegular.triggered.connect(lambda: self.reloadRegular())
    self.removeAllRegular.triggered.connect(lambda: self.removeAllReg())
    self.regularMenu.popup(QCursor.pos())

  def regularManagement(self,type,row=-1):
    '''
    正则管理  type：操作类型（1=添加，2=删除）
    '''
    if type==1:
      self.regularlist.insertRow(0)
      captureArea=QComboBox()
      captureArea.addItems(["禁用","私聊（管理）","私聊（所有）","群聊（管理）","群聊（所有）"])
      self.regularlist.setCellWidget(0, 0, captureArea)
    elif type==2 and row!=-1:
      reply = QMessageBox.warning(
      self,
      'Dylan',
      f"确定要删除第{row+1}行记录吗？\n第{row+1}行将会永远失去！（真的很久！）",
      QMessageBox.Yes | QMessageBox.No, 
      QMessageBox.No
      )
      if reply == QMessageBox.Yes:
        self.regularlist.removeRow(row)

class Factorial(QObject):
  '''QtWeb通信模块'''
  @pyqtSlot(str, result=str)
  def factorial(self,void):
    if not logQueue.empty():
      return logQueue.get()
    else:
      return "None"

def componentInformation():
  '''组件信息处理'''
  global MainWindow,forms,datas
  UiFinished=False
  while True:
    time.sleep(1)
    while UiFinished:
      time.sleep(1)
      try:
        if not MainWindow.isVisible():
          exit()
      except:
        exit()
      datas={
        "_notice":"请不要在此修改任何内容！！！",
        "regular":{
          "disabled":[],
          "private":[],
          "private_admin":[],
          "group":[],
          "group_admin":[]
        },
        "setting":{
          "enable_colorful_log":forms["enableColorfulLog"].isChecked(),
          "compatibility_mode":forms["compatibilityMode"].isChecked(),
          "path":forms["filepath"].text(),
          "http_msg":8080,
          "http_send":5700
          
        }
      }
      rows=forms["regularlist"].rowCount()
      if rows>0:
        for singleRow in range(rows):
          # print(singleRow,rows)
          if forms["regularlist"].item(singleRow,1):
            regular=forms["regularlist"].item(singleRow,1).text()
          else:
            regular=""
          if forms["regularlist"].item(singleRow,2):
            remark=forms["regularlist"].item(singleRow,2).text()
          else:
            remark=""
          if forms["regularlist"].item(singleRow,3):
            command=forms["regularlist"].item(singleRow,3).text()
          else:
            command=""
          captureArea=forms["regularlist"].cellWidget(singleRow,0).currentText()
          if captureArea=="禁用":
            captureArea="disabled"
          elif captureArea=="私聊（所有）":
            captureArea="private"
          elif captureArea=="私聊（管理）":
            captureArea="private_admin"
          elif captureArea=="群聊（所有）":
            captureArea="group"
          elif captureArea=="群聊（管理）":
            captureArea="group_admin"
          datas["regular"][captureArea].append({
              "regular":regular,
              "command":command,
              "remark":remark
            })
      with open(os.path.join(selfPath,"datas.json"), 'w',encoding='utf-8')as jsonFile:
        jsonFile.write(json.dumps(datas,sort_keys=True,ensure_ascii=False,indent=2))
            
    try:
      if MainWindow.isVisible():
        UiFinished=True
    except:
      continue

def server(path):
  '''服务器输出读取和状态监控'''
  global serverProcess,state,forms
  state=1
  serverProcess=subprocess.Popen(
    path,
    stdout=subprocess.PIPE,
    stdin=subprocess.PIPE,
    universal_newlines=True,
    bufsize=1,
    encoding="UTF-8"
    )
  logQueue.put("#cls")
  logQueue.put("[<span style='color:#007ACC'>Dylan</span>]服务器启动中...")
  started=0
  line=0
  print(serverProcess.pid)
  while state==1:
    try:
      log=serverProcess.stdout.readline()
    except:
      state=0
    if log!=None:
      log=outputRecognition(log)
      if not re.search('^[\n\s\r]+?$',log) and log!="":
        if (re.search("Server\sstarted\.$",log) or log.find("Done")>0) and started==0:
          forms["version"].setText(version[:10])
          forms["gamemode"].setText(gamemode)
          forms["difficulty"].setText(difficulty)
          forms["state"].setText("已启动")
          forms["levelname"].setText(levelname[:20])
          forms["port"].setText(ipv4+" /"+ipv6)
          started=1
        if started==0:
          if log.find("Version")>0:
            version=re.sub("^.+?(version|Version)[:\s]([0-9\.]+).+$",r"\2",log)
          elif log.find("Game mode")>0 :
            if log.find("Survival")>0:
              gamemode="生存"
            elif log.find("Creative")>0:
              gamemode="创造"
            else:
              gamemode="冒险"
          elif log.find("Difficulty")>0:
            if log.find("PEACEFUL")>0:
              difficulty="和平"
            elif log.find("EASY")>0:
              difficulty="简单"
            elif log.find("NORMAL")>0:
              difficulty="普通"
            else:
              difficulty="困难"
          elif log.find("Level Name")>0:
            levelname=re.sub("^(.+?)(Level\sName)[:\s]+?(.+?)$",r"\3",log)
          elif log.find("IPv4")>0:
            ipv4=re.sub("^(.+?)(port)[:\s]+?(.+?)$",r"\3",log)
          elif log.find("IPv6")>0:
            ipv6=re.sub("^(.+?)(port)[:\s]+?(.+?)$",r"\3",log)
          forms["state"].setText("启动中")
        if not logQueue.full():
          log=escape(log)
          if forms["enableColorfulLog"].isChecked():
            log=colorLog(log)
          logQueue.put(log)
    if bool(serverProcess.poll()) or re.search("Quit\scorrectly",log) or state==0:
      state=0
      logQueue.put("--------------------")
      logQueue.put(("[<span style='color:#007ACC'>Dylan</span>]进程已退出"))
      time.sleep(0.05)
      forms["port"].setText("- / -")
      forms["levelname"].setText("-")
      forms["difficulty"].setText("-")
      forms["gamemode"].setText("-")
      forms["state"].setText("未启动")
      forms["version"].setText("-")
      forms["input"].setText("")
      forms["input"].setDisabled(True)
      forms["start"].setDisabled(False)
      forms["restart"].setDisabled(True)
      forms["stop"].setDisabled(True)
      forms["forcestop"].setDisabled(True)
      break
    try:
      if not MainWindow.isVisible():
        serverProcess.stdin.write("stop\n")
        break
    except:
      serverProcess.stdin.write("stop\n")
      break
    if line>32000:
      logQueue.put("#cls")

def outputCommand(command):
  '''将指令输出至bds和控制台'''
  global serverProcess
  print(command)
  try:
    serverProcess.stdin.write(command+"\n")
  except:
    pass
  logQueue.put(">"+command)


def outputRecognition(log):
  '''处理LL加载器下的输入前缀和颜色代码'''
  log=re.sub("\[.+?m","",log)
  log=re.sub("","",log)
  log=re.sub('^> ',"",log)
  log=re.sub('^>',"",log)
  log=re.sub('\s$',"",log)
  return log

def escape(log):
  '''转义log中的部分字符'''
  log=log.replace('/',"&#47;")
  log=log.replace('"',"&quot;")
  log=log.replace(',',"&#44;")
  log=log.replace(':',"&#58;")
  log=log.replace("<","&lt;")
  log=log.replace(">","&gt;")
  return log

def colorLog(log):
  '''彩色日志处理'''
  log=re.sub("\s(INFO|info|Info)",r"<span id='info'> \1</span>",log) #info
  log=re.sub("\s(WARN|warn|Warn)",r"<span id='warn'><b> \1</b></span>",log) #warn
  log=re.sub("\s(ERROR|error|Error)",r"<span id='error'><b> \1</b></span>",log) #error
  log=re.sub("\s(DEBUG|debug|Debug)",r"<span id='debug'> \1</span>",log) #debug
  log=re.sub("\[(SERVER|server|Server)\]",r"[<span id='server'>\1</span>]",log) #server
  log=re.sub("\[([A-Za-z0-9\s]+?)\]",r"[<span id='\1'>\1</span>]",log)  #ck
  log=re.sub("(([0-9A-Za-z\._-]+\.[a-z]{2,3}))",r"<span id='file'>\1</span>",log)#{files}
  return log

def startServer():
  global state
  _state=0
  while True:
    if state==1 and _state==0:
      _state=1
      server(datas["setting"]["path"])
      _state=0
    if state==1 or _state==1:
      try:
        if not MainWindow.isVisible():
          serverProcess.stdin.write("stop\n")
          break
      except:
        serverProcess.stdin.write("stop\n")
        break
    time.sleep(0.5)
  exit()

def statusMonitoring():
  '''系统CPU占用与内存使用率监控'''
  global serverProcess,forms,MainWindow
  while True:
    try:
      if not MainWindow.isVisible():
        break
    except:
      break
    time.sleep(0.5)
    while state==1:
      time.sleep(1)
      try:
        if not MainWindow.isVisible():
          break
      except:
        break
      forms["cpu"].setText(str(psutil.cpu_percent())+"%")
      forms["ram"].setText(str(psutil.virtual_memory()[2])+"%")
    if forms!="":
      forms["cpu"].setText("-%")
      forms["ram"].setText("-%")



def mainGui():
  '''主程序'''
  global MainWindow
  app=QtWidgets.QApplication(sys.argv)
  app.setWindowIcon(QIcon(icoPath))
  MainWindow=gui()
  MainWindow.show()
  sys.exit(app.exec_())

if __name__=="__main__":
  channel = QWebChannel()
  factorial = Factorial()
  VERSION="Alpha 1.6.20220228"
  selfPath=os.path.dirname(os.path.realpath(sys.argv[0]))
  print("I Run at",selfPath)
  consolePath=os.path.join(selfPath,"console.html")
  icoPath=os.path.join(selfPath,"ico.png")
  commandQueue=queue.Queue(maxsize=100)
  logQueue=queue.Queue(maxsize=10000)
  state=0
  forms=""
  if not os.path.exists(os.path.join(selfPath,"datas.json")):
    datas={"_notice": "请不要在此修改任何内容！！！","regular": {"disabled": [],"group": [],"group_admin": [],"private": [],"private_admin": []},"setting": {"compatibility_mode": False,"enable_colorful_log": True,"http_msg": 8080,"http_send": 5700,"path": ""}}
  else:
    with open(os.path.join(selfPath,"datas.json"), 'r',encoding='utf-8')as jsonFile:
      datas=json.load(jsonFile)
  if not os.path.exists(os.path.join(selfPath,"console.html")):
    print("console.html文件不存在")
    exit(input())
  getComponentInformation=threading.Thread(target=componentInformation,daemon=True)
  getComponentInformation.start()
  serverThread=threading.Thread(target=startServer,daemon=True)
  serverThread.start()
  monitoringThread=threading.Thread(target=statusMonitoring,daemon=True)
  monitoringThread.start()
  mainGui()
