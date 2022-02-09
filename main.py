import os
import queue
import re
import subprocess
import sys
import threading
import time
from datetime import datetime

import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon, QTextCursor

class Ui_MainWindow(object):
  def setupUi(self, MainWindow):
    MainWindow.setObjectName("MainWindow")
    MainWindow.setEnabled(True)
    MainWindow.resize(800, 450)
    MainWindow.setMinimumSize(QtCore.QSize(800, 450))
    MainWindow.setMaximumSize(QtCore.QSize(800, 450))
    MainWindow.setWindowIcon(QIcon(icoPath))
    self.centralwidget = QtWidgets.QWidget(MainWindow)
    self.centralwidget.setObjectName("centralwidget")
    self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
    self.tabWidget.setGeometry(QtCore.QRect(0, 0, 800, 450))
    self.tabWidget.setMovable(False)
    self.tabWidget.setObjectName("tabWidget")
    self.index = QtWidgets.QWidget()
    self.index.setObjectName("index")
    self.controls = QtWidgets.QGroupBox(self.index)
    self.controls.setGeometry(QtCore.QRect(4, 310, 221, 91))
    self.controls.setObjectName("controls")
    self.start = QtWidgets.QPushButton(self.controls)
    self.start.setGeometry(QtCore.QRect(5, 15, 100, 30))
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    self.start.setFont(font)
    self.start.setObjectName("start")
    self.stop = QtWidgets.QPushButton(self.controls)
    self.stop.setEnabled(False)
    self.stop.setGeometry(QtCore.QRect(115, 15, 100, 30))
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    self.stop.setFont(font)
    self.stop.setObjectName("stop")
    self.forcestop = QtWidgets.QPushButton(self.controls)
    self.forcestop.setEnabled(False)
    self.forcestop.setGeometry(QtCore.QRect(115, 50, 100, 30))
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    font.setBold(False)
    font.setItalic(False)
    font.setWeight(50)
    self.forcestop.setFont(font)
    self.forcestop.setObjectName("forcestop")
    self.restart = QtWidgets.QPushButton(self.controls)
    self.restart.setEnabled(False)
    self.restart.setGeometry(QtCore.QRect(5, 50, 100, 30))
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    self.restart.setFont(font)
    self.restart.setObjectName("restart")
    self.consolegroup = QtWidgets.QGroupBox(self.index)
    self.consolegroup.setGeometry(QtCore.QRect(230, 10, 561, 391))
    self.consolegroup.setObjectName("consolegroup")
    self.console = QtWidgets.QTextBrowser(self.consolegroup)
    self.console.setGeometry(QtCore.QRect(10, 20, 541, 331))
    font = QtGui.QFont()
    font.setFamily("Courier")
    font.setPointSize(10)
    self.console.setFont(font)
    self.console.setObjectName("console")
    self.input = QtWidgets.QLineEdit(self.consolegroup)
    self.input.setGeometry(QtCore.QRect(10, 360, 541, 21))
    self.input.setObjectName("input")
    self.info = QtWidgets.QGroupBox(self.index)
    self.info.setGeometry(QtCore.QRect(9, 9, 211, 291))
    self.info.setObjectName("info")
    self.state = QtWidgets.QLabel(self.info)
    self.state.setGeometry(QtCore.QRect(10, 25, 191, 31))
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    self.state.setFont(font)
    self.state.setScaledContents(False)
    self.state.setWordWrap(False)
    self.state.setObjectName("state")
    self.version = QtWidgets.QLabel(self.info)
    self.version.setGeometry(QtCore.QRect(10, 65, 191, 31))
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    self.version.setFont(font)
    self.version.setScaledContents(False)
    self.version.setWordWrap(False)
    self.version.setObjectName("version")
    self.gamemode = QtWidgets.QLabel(self.info)
    self.gamemode.setGeometry(QtCore.QRect(10, 105, 191, 31))
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    self.gamemode.setFont(font)
    self.gamemode.setScaledContents(False)
    self.gamemode.setWordWrap(False)
    self.gamemode.setObjectName("gamemode")
    self.difficulty = QtWidgets.QLabel(self.info)
    self.difficulty.setGeometry(QtCore.QRect(11, 145, 191, 31))
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    self.difficulty.setFont(font)
    self.difficulty.setScaledContents(False)
    self.difficulty.setWordWrap(False)
    self.difficulty.setObjectName("difficulty")
    self.levelname = QtWidgets.QLabel(self.info)
    self.levelname.setGeometry(QtCore.QRect(11, 185, 191, 31))
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    self.levelname.setFont(font)
    self.levelname.setScaledContents(False)
    self.levelname.setWordWrap(False)
    self.levelname.setObjectName("levelname")
    self.port = QtWidgets.QLabel(self.info)
    self.port.setGeometry(QtCore.QRect(11, 225, 191, 31))
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    self.port.setFont(font)
    self.port.setScaledContents(False)
    self.port.setWordWrap(False)
    self.port.setObjectName("port")
    self.tabWidget.addTab(self.index, "")
    self.tab_2 = QtWidgets.QWidget()
    self.tab_2.setObjectName("tab_2")
    self.tabWidget.addTab(self.tab_2, "")
    self.statusbar = QtWidgets.QStatusBar(MainWindow)

    self.retranslateUi(MainWindow)
    self.tabWidget.setCurrentIndex(0)
    QtCore.QMetaObject.connectSlotsByName(MainWindow)

    self.input.setDisabled(True)
    self.start.setDisabled(False)
    self.restart.setDisabled(True)
    self.stop.setDisabled(True)
    self.forcestop.setDisabled(True)
    self.start.clicked.connect(lambda: self.control(1))
    self.stop.clicked.connect(lambda: self.control(2))
    self.input.returnPressed.connect(self.transferCommand)
    formQueue.put(item={
      "console":self.console,
      "input":self.input,
      "start":self.start,
      "stop":self.stop,
      "restart":self.restart,
      "forcestop":self.forcestop,
      "state":self.state,
      "version":self.version,
      "gamemode":self.gamemode,
      "difficulty":self.difficulty,
      "levelname":self.levelname,
      "port":self.port
      })


  def retranslateUi(self, MainWindow):
    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "Dylan "+VERSION))
    self.controls.setTitle(_translate("MainWindow", "控制"))
    self.start.setText(_translate("MainWindow", "▶ 启动"))
    self.stop.setText(_translate("MainWindow", "■ 停止"))
    self.forcestop.setText(_translate("MainWindow", "强制关闭"))
    self.restart.setText(_translate("MainWindow", "↻ 重启"))
    self.consolegroup.setTitle(_translate("MainWindow", "控制台"))
    self.input.setPlaceholderText(_translate("MainWindow", "> 在此输入指令..."))
    self.info.setTitle(_translate("MainWindow", "服务器信息"))
    self.state.setText(_translate("MainWindow", "状态："))
    self.version.setText(_translate("MainWindow", "版本："))
    self.gamemode.setText(_translate("MainWindow", "模式："))
    self.difficulty.setText(_translate("MainWindow", "难度："))
    self.levelname.setText(_translate("MainWindow", "存档名称："))
    self.port.setText(_translate("MainWindow", "端口："))
    self.tabWidget.setTabText(self.tabWidget.indexOf(self.index), _translate("MainWindow", "主页"))
    self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "unknown"))

  def transferCommand(self):
    text=self.input.text()
    outputCommand(text)
    self.input.setText("")
  
  def control(self,type):
    global state

    if type==1 and state!=1:
      state=1
      time.sleep(1)
      
      self.start.setDisabled(True)
      self.stop.setDisabled(False)
      # self.restart.setDisabled(False)
      # self.forcestop.setDisabled(False)
      self.input.setDisabled(False)
    elif type==2:
      outputCommand("stop")

  

def server(path):
  
  global serverProcess,state
  state=1
  serverProcess=subprocess.Popen(
    path,
    stdout=subprocess.PIPE,
    stdin=subprocess.PIPE,
    universal_newlines=True,
    bufsize=1,
    encoding="UTF-8"
    )
  logQueue.put("[<span style='color:rgb(0,122,204)'>Dylan</span>]服务器启动中...")

  started=0
  while state==1:
    try:
      log=serverProcess.stdout.readline()
    except:
      state=0
    if log!=None:
      log=outputRecognition(log)
      if len(log)>200:
        log=log[:100]+"[剩余{}字符未显示]".format(len(log)-100)# 防止渲染出错
      if not re.search('^[\n\s\r]+?$',log) and log!="":
        if re.search("Server\sstarted\.$",log) and started==0:
          started=1
        # if started==0:
        #   if re.search('version|Version',log):
        #     version=re.sub("^.+?version|Version(.?)$",r"\1",log)[:20]
        #     forms["version"].setText("版本："+version)
        #     pass
        logQueue.put(log)
        print(log.replace("\n",""))

    if bool(serverProcess.poll()) or re.search("Quit\scorrectly",log) or state==0:
      state=0
      logQueue.put("--------------------")
      logQueue.put(("[<span style='color:rgb(0,122,204)'>Dylan</span>]进程已退出"))
      time.sleep(0.05)
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
def logger():
  global forms
  forms=""
  while True:
    time.sleep(0.1)
    if not formQueue.empty() and forms=="":
      forms=formQueue.get()
      time.sleep(2)
      continue
    if not logQueue.empty():
      log=logQueue.get()
      logOut(forms["console"],log)
    else:
      time.sleep(0.2)
def outputCommand(command):
  print(command)
  serverProcess.stdin.write(command+"\n")
  logQueue.put(">"+command)
  

def outputRecognition(log):
  log=re.sub("^>.+\dm","",log)# 处理LL加载器下的输入前缀和颜色代码
  log=re.sub("\[\d+?m","",log)
  log=re.sub('[]',"",log)
  log=re.sub('^> ',"",log)
  log=re.sub('^>',"",log)
  log=log.replace('/',"&#47;")# 转义防炸
  log=log.replace('"',"&quot;")
  log=log.replace(',',"&#44;")
  log=log.replace(':',"&#58;")
  log=log.replace("<","&lt;")
  log=log.replace(">","&gt;")

  log=re.sub("(INFO|info|Info)[\s]?\]",r"<span style='color:rgb(0,170,0)'>\1</span>]",log)
  log=re.sub("(WARN|warn|Warn)[\s]?\]",r"<span style='color:rgb(202,121,62)'><b>\1</b></span>]",log)
  log=re.sub("(ERROR|error|Error)[\s]?\]",r"<span style='color:rgb(184,27,27)'><b>\1</b></span>]",log)
  log=re.sub("(DEBUG|debug|Debug)[\s]?\]",r"<span style='color:rgb(170,0,170)'>\1</span>]",log)
  log=re.sub("([0-9A-Za-z\.-]+?dll)",r"<span style='color:rgb(104,130,146)'><b>\1</b></span>",log)
  log=re.sub("([0-9A-Za-z\.-]+?js)",r"<span style='color:rgb(104,130,146)'><b>\1</b></span>",log)
  log=re.sub("([0-9A-Za-z\.-]+?py)",r"<span style='color:rgb(104,130,146)'><b>\1</b></span>",log)
  return log

def startServer():
  global state
  time.sleep(5)
  _state=0
  while True:
    if state==1 and _state==0:
      _state=1
      server(setting["path"])
      _state=0
    try:
      if not MainWindow.isVisible():
        serverProcess.stdin.write("stop\n")
        break
    except:
      serverProcess.stdin.write("stop\n")
      break
    time.sleep(1)
  exit()

def logOut(console,log,html=1):
  cursor = console.textCursor()
  cursor.movePosition(QTextCursor.End)
  try:
    if html==1:
      cursor.insertHtml("<div>"+log+"</div>")
    else:
      cursor.insertText(log+"\n")
  except:
    pass
  cursor.insertText("\n")
  console.setTextCursor(cursor)
  console.ensureCursorVisible()

def gui():
  global MainWindow
  app=QtWidgets.QApplication(sys.argv)
  MainWindow=QtWidgets.QWidget()
  ui=Ui_MainWindow()
  ui.setupUi(MainWindow)
  MainWindow.show()
  sys.exit(app.exec_())


if __name__=="__main__":
  VERSION="Alpha 1.2.20220209"
  selfPath=os.path.split(os.path.realpath(__file__))[0]
  icoPath=os.path.join(selfPath,"ico.png")
  formQueue=queue.Queue(maxsize=10)
  commandQueue=queue.Queue(maxsize=100)
  logQueue=queue.Queue(maxsize=10000)
  state=0
  if os.path.exists(os.path.join(selfPath,"setting.ini")):
    settingFile=open(os.path.join(selfPath,"setting.ini"),encoding="UTF-8")
    setting={}
    for line in settingFile:
      if line.find('=') > 0:
        strs = line.replace('\n', '').split('=')
        setting[strs[0]] = strs[1]
  else:
    print("setting.ini文件不存在")
    exit(os.system("pause"))
  serverThread=threading.Thread(target=startServer)
  serverThread.daemon=1
  serverThread.start()
  logThread=threading.Thread(target=logger)
  logThread.daemon=1
  logThread.start()
  gui()