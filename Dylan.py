import json
import os
import queue
import re
import subprocess
import sys
import threading
import time

import requests
from flask import Flask, request

import psutil
import PyQt5
from gui import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, QUrl, pyqtSlot
from PyQt5.QtGui import QCursor, QIcon, QPalette,QColor
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWidgets import *


class gui(QWidget,Ui_MainWindow):
  '''主窗口'''
  def __init__(self, parent=None):
    '''主窗口设置'''
    super(gui, self).__init__(parent)
    self.setupUi(self)
    global consolePath,forms,datas
    channel.registerObject("obj", Function)
    self.setWindowTitle("Dylan_"+VERSION)
    self.tabWidget.setCurrentIndex(0)
    #############
    self.Panel_input.setDisabled(True)
    self.Panel_start.setDisabled(False)
    self.Panel_restart.setDisabled(True)
    self.Panel_stop.setDisabled(True)
    self.Panel_forcestop.setDisabled(True)

    self.regularlist.customContextMenuRequested.connect(self.createRegularMenu)
    self.loadRegular()
    self.connectFunctions()
    forms={
      "panel":{
        "console":self.Panel_console,
        "input":self.Panel_input,
        "start":self.Panel_start,
        "stop":self.Panel_stop,
        "restart":self.Panel_restart,
        "forcestop":self.Panel_forcestop,
        "state":self.Panel_state_2,
        "version":self.Panel_version_2,
        "gamemode":self.Panel_gamemode_2,
        "difficulty":self.Panel_difficulty_2,
        "levelname":self.Panel_levelname_2,
        "port":self.Panel_port_2,
        "ram":self.Panel_ram_2,
        "cpu":self.Panel_cpu_2
      },
      "setting":{
        "start":{
          "filepath":self.setting_filepath,
          "compatibilityMode":self.setting_compatibilityMode,
          "autoRestart":self.setting_autoRestart
        },
        "bot":{
          "sendPort":self.setting_sendPort,
          "listenPort":self.setting_listenPort,
          "botFilepath":self.setting_botFilepath
        },
        "console":{
          "colorfulLogOut":self.setting_colorfulLogOut,
          "enableOutputToLog":self.setting_enableOutputToLog
        },
        "msg":{
          "groupList":self.setting_groupList,
          "permissionList":self.setting_permissionList,
          "givePermissionToAllAdmin":self.setting_givePermissionToAllAdmin,
          "outputMsgToLog":self.setting_outputMsgToLog
        },
        "Dylan":{
          "enableUpdate":self.setting_enableUpdate,
          "enableAnnouncement":self.setting_enableAnnouncement,
          "chosenTheme":self.setting_chosenTheme,
        }
      },
      "regularlist":self.regularlist
      }
    self.loadSetting()
    
  def loadSetting(self):
    settingList=forms["setting"]
    for group in settingList:
      for object in settingList[group]:
        if type(settings[group][object])==bool:
          if "setChecked" in dir(settingList[group][object]):
            settingList[group][object].setChecked(settings[group][object])
        elif type(settings[group][object])==int:
          if "setValue" in dir(settingList[group][object]):
            settingList[group][object].setValue(settings[group][object])
          elif "setCurrentIndex" in dir(settingList[group][object]):
            settingList[group][object].setCurrentIndex(settings[group][object])
        elif type(settings[group][object])==str:
          if "setText" in dir(settingList[group][object]):
            settingList[group][object].setText(settings[group][object])
    self.setThemes(self.setting_chosenTheme.currentIndex())

  def setHtml(self,theme):
    self.Panel_console.load(QUrl("file:///"+str(consolePath).replace('\\',"/")+f"?width=539&height=319&type=bds&theme={theme}"))
    self.Panel_console.page().setWebChannel(channel)
    self.CQ_console.load(QUrl("file:///"+str(consolePath).replace('\\',"/")+f"?width=599&height=382&type=bot&theme={theme}"))
    self.CQ_console.page().setWebChannel(channel)

  def connectFunctions(self):
    '''连接组件与函数'''
    self.setting_selectfile.clicked.connect(lambda: self.selectFile())
    self.Panel_start.clicked.connect(lambda: self.serverControl(1))
    self.Panel_stop.clicked.connect(lambda: self.serverControl(2))
    self.Panel_input.returnPressed.connect(self.transferCommand)

  def setThemes(self,themeId):
    '''设置主题'''
    if themeId==0:
      self.setting_scrollArea.setStyleSheet(
        "#setting_scrollAreaWidgetContents{\nbackground:rgb(255,255,255);}")
      self.setHtml("default")
    elif themeId==1:
      qApp.setStyle("Fusion")
      self.setting_scrollArea.setStyleSheet(
        "#setting_scrollAreaWidgetContents{\nbackground:rgb(252,252,252);}")
      self.setHtml("fusion")
    elif themeId==2:
      qApp.setStyle("Fusion")
      dark_palette = QPalette()
      dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
      dark_palette.setColor(QPalette.WindowText, QColor(255,255,255))
      dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
      dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
      dark_palette.setColor(QPalette.ToolTipBase, QColor(255,255,255))
      dark_palette.setColor(QPalette.ToolTipText, QColor(255,255,255))
      dark_palette.setColor(QPalette.Text, QColor(255,255,255))
      dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
      dark_palette.setColor(QPalette.Disabled,QPalette.Button, QColor(30,30,30))
      dark_palette.setColor(QPalette.Disabled,QPalette.Text, QColor(0,0,0,0))
      dark_palette.setColor(QPalette.ButtonText, QColor(255,255,255))
      dark_palette.setColor(QPalette.BrightText, QColor(255,0,0))
      dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
      dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
      dark_palette.setColor(QPalette.HighlightedText, QColor(0,0,0))
      qApp.setPalette(dark_palette)
      qApp.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
      self.setHtml("fusion_dark")

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
    text=self.Panel_input.text()
    outputCommand(text)
    self.Panel_input.setText("")

  def serverControl(self,type):
    '''服务器控制按钮'''
    global state
    if type==1 and state!=1:
      if not os.path.exists(self.setting_filepath.text()):
        print("启动目标文件不存在")
      else:
        state=1
        self.Panel_start.setDisabled(True)
        self.Panel_stop.setDisabled(False)
        self.Panel_input.setDisabled(False)
    elif type==2:
      outputCommand("stop")

  def selectFile(self):
    '''选择启动文件'''
    startFile=QFileDialog.getOpenFileName(self, "选择文件",selfPath, "可启动文件 (*.exe *.bat *.cmd)")
    if startFile[0]!='':
      self.setting_filepath.setText(startFile[0])

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
      f"确定要删除第{row+1}行吗？\n第{row+1}行将会永远失去！（真的很久！）",
      QMessageBox.Yes | QMessageBox.No,
      QMessageBox.No
      )
      if reply == QMessageBox.Yes:
        self.regularlist.removeRow(row)

class Functions(QObject):
  '''QtWeb通信模块'''
  @pyqtSlot(str, result=str)
  def bdslog(self,void):
    if not logQueue.empty():
      return logQueue.get()
    else:
      return "None"

  @pyqtSlot(str, result=str)
  def botlog(self,void):
    if not botQueue.empty():
      return botQueue.get()
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
          captureArea=forms["regularlist"].cellWidget(singleRow,0).currentIndex()
          if captureArea==0:
            captureArea="disabled"
          elif captureArea==1:
            captureArea="private_admin"
          elif captureArea==2:
            captureArea="private"

          elif captureArea==3:
            captureArea="group_admin"
          elif captureArea==4:
            captureArea="group"
          datas["regular"][captureArea].append({
              "regular":regular,
              "command":command,
              "remark":remark
            })
      with open(os.path.join(selfPath,"datas.json"), 'w',encoding='utf-8')as jsonFile:
        jsonFile.write(json.dumps(datas,sort_keys=True,ensure_ascii=False,indent=2))


      settings={
        "start":{
          "filepath":forms["setting"]["start"]["filepath"].text(),
          "compatibilityMode":forms["setting"]["start"]["compatibilityMode"].isChecked(),
          "autoRestart":forms["setting"]["start"]["autoRestart"].isChecked()
        },
        "bot":{
          "sendPort":forms["setting"]["bot"]["sendPort"].value(),
          "listenPort":forms["setting"]["bot"]["listenPort"].value(),
          "botFilepath":forms["setting"]["bot"]["botFilepath"].text()
        },
        "console":{
          "colorfulLogOut":forms["setting"]["console"]["colorfulLogOut"].currentIndex(),
          "enableOutputToLog":forms["setting"]["console"]["enableOutputToLog"].isChecked()
        },
        "msg":{
          "groupList":processingList(forms["setting"]["msg"]["groupList"].toPlainText()),
          "permissionList":processingList(forms["setting"]["msg"]["permissionList"].toPlainText()),
          "givePermissionToAllAdmin":forms["setting"]["msg"]["givePermissionToAllAdmin"].isChecked(),
          "outputMsgToLog":forms["setting"]["msg"]["outputMsgToLog"].isChecked()
        },
        "Dylan":{
          "enableUpdate":forms["setting"]["Dylan"]["enableUpdate"].isChecked(),
          "enableAnnouncement":forms["setting"]["Dylan"]["enableAnnouncement"].currentIndex(),
          "chosenTheme":forms["setting"]["Dylan"]["chosenTheme"].currentIndex()
        }
      }
      with open(os.path.join(selfPath,"setting.json"), 'w',encoding='utf-8')as jsonFile:
        jsonFile.write(json.dumps(settings,sort_keys=True,ensure_ascii=False,indent=2))

    try:
      if MainWindow.isVisible():
        UiFinished=True
    except:
      continue

def processingList(text):
  textList=text.split("\n")
  list=[]
  for i in textList:
    if i and len(i)>=5 and len(i)<=12:
      try:
        list.append(int(i.replace(" ","")))
      except:
        pass
  return list

def server():
  '''服务器输出读取和状态监控'''
  global serverProcess,state,forms
  state=1
  serverProcess=subprocess.Popen(
    forms["setting"]["start"]["filepath"].text(),
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
          forms["panel"]["version"].setText(version[:10])
          forms["panel"]["gamemode"].setText(gamemode)
          forms["panel"]["difficulty"].setText(difficulty)
          forms["panel"]["state"].setText("已启动")
          forms["panel"]["levelname"].setText(levelname[:20])
          forms["panel"]["port"].setText(ipv4+" /"+ipv6)
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
          forms["panel"]["state"].setText("启动中")
        if not logQueue.full():
          log=escape(log)
          if forms["setting"]["console"]["colorfulLogOut"].currentIndex()==2:
            log=colorLog(log)
          logQueue.put(log)
    if bool(serverProcess.poll()) or re.search("Quit\scorrectly",log) or state==0:
      state=0
      logQueue.put("--------------------")
      logQueue.put(("[<span style='color:#007ACC'>Dylan</span>]进程已退出"))
      time.sleep(0.05)
      forms["panel"]["port"].setText("- / -")
      forms["panel"]["levelname"].setText("-")
      forms["panel"]["difficulty"].setText("-")
      forms["panel"]["gamemode"].setText("-")
      forms["panel"]["state"].setText("未启动")
      forms["panel"]["version"].setText("-")
      forms["panel"]["input"].setText("")
      forms["panel"]["input"].setDisabled(True)
      forms["panel"]["start"].setDisabled(False)
      forms["panel"]["restart"].setDisabled(True)
      forms["panel"]["stop"].setDisabled(True)
      forms["panel"]["forcestop"].setDisabled(True)
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
      server()
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
      forms["panel"]["cpu"].setText(str(psutil.cpu_percent())+"%")
      forms["panel"]["ram"].setText(str(psutil.virtual_memory()[2])+"%")
    if forms!="":
      forms["panel"]["cpu"].setText("-%")
      forms["panel"]["ram"].setText("-%")

app = Flask(__name__)
@app.route('/', methods=["POST"])
def post_data():
  put = 'http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}&auto_escape=false'
  if request.get_json().get("meta_event_type") == 'heartbeat':
    return 'ok'
  else:
    print(request.get_json())
  if request.get_json().get('message_type') == 'private':  # 私聊信息
    nickname = request.get_json().get('sender').get('nickname')
    uid = request.get_json().get('sender').get('user_id')
    message = request.get_json().get('raw_message')
    print(message, uid,nickname)

  if request.get_json().get('message_type') == 'group':  # 如果是群聊信息
    gid = request.get_json().get('group_id')
    uid = request.get_json().get('sender').get('user_id')
    card = request.get_json().get('sender').get('card')
    message = request.get_json().get('raw_message')
    print(message, uid, gid,card)
    requests.get(url=put.format(954829203, message))
    # requests.get(url=put.format(962568264, message))
  return 'ok'

def runHttp(port):
  app.run(host='127.0.0.1', port=settings["cqhttp"]["http_msg"])

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
  Function = Functions()
  VERSION="Alpha 1.6.20220228_2"
  selfPath=os.path.dirname(os.path.realpath(sys.argv[0]))
  print("I Run at",selfPath)
  consolePath=os.path.join(selfPath,"console.html")
  icoPath=os.path.join(selfPath,"ico.png")
  commandQueue=queue.Queue(maxsize=100)
  logQueue=queue.Queue(maxsize=10000)
  botQueue=queue.Queue(maxsize=10000)
  state=0
  forms=""
  if not os.path.exists(os.path.join(selfPath,"datas.json")):
    datas={
      "_notice": "请不要在此修改任何内容！！！",
      "regular": {
        "disabled": [],
        "group": [],
        "group_admin": [],
        "private": [],
        "private_admin": []
        },
      "setting": {
        "compatibility_mode": False,
        "enable_colorful_log": True,
        "http_msg": 8080,
        "http_send": 5700,
        "path": ""
        }
      }
  else:
    with open(os.path.join(selfPath,"datas.json"), 'r',encoding='utf-8') as jsonFile:
      datas=json.load(jsonFile)
  if not os.path.exists(os.path.join(selfPath,"setting.json")):
    settings={
        "start_server":{
          "enable_colorful_log":False,
          "compatibility_mode":True,
          "path":""
        },
        "cqhttp":{
          "enable":True,
          "http_msg":8080,
          "http_send":5700
        }
      }
  else:
    with open(os.path.join(selfPath,"setting.json"), 'r',encoding='utf-8')as jsonFile:
      settings=json.load(jsonFile)
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
