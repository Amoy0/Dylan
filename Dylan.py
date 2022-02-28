import os
import queue
import re
import subprocess
import sys
import threading
import time

import psutil
import PyQt5
from PyQt5 import QtCore, QtGui, QtWebEngineWidgets, QtWidgets
from PyQt5.QtCore import QObject, QUrl, pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWebChannel import QWebChannel


class Ui_MainWindow(object):
  def setupUi(self, MainWindow):
    MainWindow.setObjectName("MainWindow")
    MainWindow.setEnabled(True)
    MainWindow.resize(800, 450)
    MainWindow.setMinimumSize(QtCore.QSize(800, 450))
    MainWindow.setMaximumSize(QtCore.QSize(800, 450))
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("ico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    MainWindow.setWindowIcon(icon)
    MainWindow.setWindowOpacity(1.0)
    self.centralwidget = QtWidgets.QWidget(MainWindow)
    self.centralwidget.setObjectName("centralwidget")
    self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
    self.tabWidget.setGeometry(QtCore.QRect(0, 0, 800, 450))
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    self.tabWidget.setFont(font)
    self.tabWidget.setObjectName("tabWidget")
    self.panel = QtWidgets.QWidget()
    self.panel.setObjectName("panel")
    self.controls = QtWidgets.QGroupBox(self.panel)
    self.controls.setGeometry(QtCore.QRect(4, 310, 221, 91))
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    self.controls.setFont(font)
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
    self.consolegroup = QtWidgets.QGroupBox(self.panel)
    self.consolegroup.setGeometry(QtCore.QRect(230, 10, 561, 391))
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    self.consolegroup.setFont(font)
    self.consolegroup.setObjectName("consolegroup")
    self.input = QtWidgets.QLineEdit(self.consolegroup)
    self.input.setGeometry(QtCore.QRect(10, 360, 541, 21))
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    self.input.setFont(font)
    self.input.setObjectName("input")
    self.console = QtWebEngineWidgets.QWebEngineView(self.consolegroup)
    self.console.setGeometry(QtCore.QRect(9, 19, 541, 331))
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    self.console.setFont(font)
    self.console.setObjectName("console")
    self.info = QtWidgets.QGroupBox(self.panel)
    self.info.setGeometry(QtCore.QRect(9, 9, 211, 271))
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    self.info.setFont(font)
    self.info.setObjectName("info")
    self.state = QtWidgets.QLabel(self.info)
    self.state.setGeometry(QtCore.QRect(11, 20, 60, 31))
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    self.state.setFont(font)
    self.state.setScaledContents(False)
    self.state.setWordWrap(False)
    self.state.setObjectName("state")
    self.version = QtWidgets.QLabel(self.info)
    self.version.setGeometry(QtCore.QRect(11, 50, 60, 31))
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    self.version.setFont(font)
    self.version.setScaledContents(False)
    self.version.setWordWrap(False)
    self.version.setObjectName("version")
    self.gamemode = QtWidgets.QLabel(self.info)
    self.gamemode.setGeometry(QtCore.QRect(11, 80, 60, 31))
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    self.gamemode.setFont(font)
    self.gamemode.setScaledContents(False)
    self.gamemode.setWordWrap(False)
    self.gamemode.setObjectName("gamemode")
    self.difficulty = QtWidgets.QLabel(self.info)
    self.difficulty.setGeometry(QtCore.QRect(12, 110, 60, 31))
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    self.difficulty.setFont(font)
    self.difficulty.setScaledContents(False)
    self.difficulty.setWordWrap(False)
    self.difficulty.setObjectName("difficulty")
    self.levelname = QtWidgets.QLabel(self.info)
    self.levelname.setGeometry(QtCore.QRect(12, 140, 60, 31))
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    self.levelname.setFont(font)
    self.levelname.setScaledContents(False)
    self.levelname.setWordWrap(False)
    self.levelname.setObjectName("levelname")
    self.port = QtWidgets.QLabel(self.info)
    self.port.setGeometry(QtCore.QRect(12, 170, 60, 31))
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    self.port.setFont(font)
    self.port.setScaledContents(False)
    self.port.setWordWrap(False)
    self.port.setObjectName("port")
    self.port_2 = QtWidgets.QLabel(self.info)
    self.port_2.setGeometry(QtCore.QRect(70, 170, 125, 31))
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    self.port_2.setFont(font)
    self.port_2.setScaledContents(False)
    self.port_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.port_2.setWordWrap(False)
    self.port_2.setObjectName("port_2")
    self.gamemode_2 = QtWidgets.QLabel(self.info)
    self.gamemode_2.setGeometry(QtCore.QRect(70, 80, 125, 31))
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    self.gamemode_2.setFont(font)
    self.gamemode_2.setScaledContents(False)
    self.gamemode_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.gamemode_2.setWordWrap(False)
    self.gamemode_2.setObjectName("gamemode_2")
    self.difficulty_2 = QtWidgets.QLabel(self.info)
    self.difficulty_2.setGeometry(QtCore.QRect(70, 110, 125, 31))
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    self.difficulty_2.setFont(font)
    self.difficulty_2.setScaledContents(False)
    self.difficulty_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.difficulty_2.setWordWrap(False)
    self.difficulty_2.setObjectName("difficulty_2")
    self.version_2 = QtWidgets.QLabel(self.info)
    self.version_2.setGeometry(QtCore.QRect(70, 50, 125, 31))
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    self.version_2.setFont(font)
    self.version_2.setScaledContents(False)
    self.version_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.version_2.setWordWrap(False)
    self.version_2.setObjectName("version_2")
    self.state_2 = QtWidgets.QLabel(self.info)
    self.state_2.setGeometry(QtCore.QRect(70, 20, 125, 31))
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    self.state_2.setFont(font)
    self.state_2.setScaledContents(False)
    self.state_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.state_2.setObjectName("state_2")
    self.levelname_2 = QtWidgets.QLabel(self.info)
    self.levelname_2.setGeometry(QtCore.QRect(70, 140, 125, 31))
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    self.levelname_2.setFont(font)
    self.levelname_2.setScaledContents(False)
    self.levelname_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.levelname_2.setWordWrap(False)
    self.levelname_2.setObjectName("levelname_2")
    self.cpu = QtWidgets.QLabel(self.info)
    self.cpu.setGeometry(QtCore.QRect(12, 200, 71, 31))
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    self.cpu.setFont(font)
    self.cpu.setScaledContents(False)
    self.cpu.setWordWrap(False)
    self.cpu.setObjectName("cpu")
    self.cpu_2 = QtWidgets.QLabel(self.info)
    self.cpu_2.setGeometry(QtCore.QRect(70, 200, 125, 31))
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    self.cpu_2.setFont(font)
    self.cpu_2.setScaledContents(False)
    self.cpu_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.cpu_2.setWordWrap(False)
    self.cpu_2.setObjectName("cpu_2")
    self.ram_2 = QtWidgets.QLabel(self.info)
    self.ram_2.setGeometry(QtCore.QRect(70, 230, 125, 31))
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    self.ram_2.setFont(font)
    self.ram_2.setScaledContents(False)
    self.ram_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.ram_2.setWordWrap(False)
    self.ram_2.setObjectName("ram_2")
    self.ram = QtWidgets.QLabel(self.info)
    self.ram.setGeometry(QtCore.QRect(12, 230, 71, 31))
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    self.ram.setFont(font)
    self.ram.setScaledContents(False)
    self.ram.setWordWrap(False)
    self.ram.setObjectName("ram")
    self.tabWidget.addTab(self.panel, "")
    self.regular = QtWidgets.QWidget()
    self.regular.setObjectName("regular")
    self.tabWidget.addTab(self.regular, "")
    self.setting = QtWidgets.QWidget()
    self.setting.setObjectName("setting")
    self.groupBox = QtWidgets.QGroupBox(self.setting)
    self.groupBox.setGeometry(QtCore.QRect(10, 10, 771, 121))
    self.groupBox.setObjectName("groupBox")
    self.file = QtWidgets.QLabel(self.groupBox)
    self.file.setGeometry(QtCore.QRect(10, 20, 201, 16))
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    self.file.setFont(font)
    self.file.setObjectName("file")
    self.filepath = QtWidgets.QLineEdit(self.groupBox)
    self.filepath.setGeometry(QtCore.QRect(10, 40, 661, 21))
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    self.filepath.setFont(font)
    self.filepath.setReadOnly(True)
    self.filepath.setObjectName("filepath")
    self.selectfile = QtWidgets.QPushButton(self.groupBox)
    self.selectfile.setGeometry(QtCore.QRect(680, 39, 81, 23))
    self.selectfile.setObjectName("selectfile")
    self.enableColorfulLog = QtWidgets.QCheckBox(self.groupBox)
    self.enableColorfulLog.setGeometry(QtCore.QRect(10, 70, 241, 16))
    self.enableColorfulLog.setChecked(True)
    self.enableColorfulLog.setObjectName("enableColorfulLog")
    self.compatibilityMode = QtWidgets.QCheckBox(self.groupBox)
    self.compatibilityMode.setGeometry(QtCore.QRect(10, 90, 491, 16))
    self.compatibilityMode.setObjectName("compatibilityMode")
    self.tabWidget.addTab(self.setting, "")
    self.about = QtWidgets.QWidget()
    self.about.setObjectName("about")
    self.tabWidget.addTab(self.about, "")

    self.retranslateUi(MainWindow)
    self.tabWidget.setCurrentIndex(0)
    QtCore.QMetaObject.connectSlotsByName(MainWindow)

  def retranslateUi(self, MainWindow):
    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "Dylan"))
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
    self.gamemode.setText(_translate("MainWindow", "游戏模式："))
    self.difficulty.setText(_translate("MainWindow", "游戏难度："))
    self.levelname.setText(_translate("MainWindow", "存档名称："))
    self.port.setText(_translate("MainWindow", "端口："))
    self.port_2.setText(_translate("MainWindow", "- / -"))
    self.gamemode_2.setText(_translate("MainWindow", "-"))
    self.difficulty_2.setText(_translate("MainWindow", "-"))
    self.version_2.setText(_translate("MainWindow", "-"))
    self.state_2.setText(_translate("MainWindow", "未启动"))
    self.levelname_2.setText(_translate("MainWindow", "-"))
    self.cpu.setText(_translate("MainWindow", "CPU使用率："))
    self.cpu_2.setText(_translate("MainWindow", "-%"))
    self.ram_2.setText(_translate("MainWindow", "-%"))
    self.ram.setText(_translate("MainWindow", "内存使用率："))
    self.tabWidget.setTabText(self.tabWidget.indexOf(self.panel), _translate("MainWindow", "控制面板"))
    self.tabWidget.setTabText(self.tabWidget.indexOf(self.regular), _translate("MainWindow", "正则"))
    self.groupBox.setTitle(_translate("MainWindow", "启动设置"))
    self.file.setText(_translate("MainWindow", "启动路径（推荐使用.exe或.bat）"))
    self.selectfile.setText(_translate("MainWindow", "选择文件"))
    self.enableColorfulLog.setText(_translate("MainWindow", "彩色日志输出（部分语法高亮）"))
    self.compatibilityMode.setText(_translate("MainWindow", "兼容模式（使用嵌套批处理文件开服） 若出现服务器启动失败可尝试开启此选项）"))
    self.tabWidget.setTabText(self.tabWidget.indexOf(self.setting), _translate("MainWindow", "设置"))
    self.tabWidget.setTabText(self.tabWidget.indexOf(self.about), _translate("MainWindow", "关于"))
    self.customize()

  def customize(self):
    global consolePath
    self.filepath.setText(setting["path"])
    consolePath="file:///"+str(consolePath).replace('\\',"/")
    self.console.load(QUrl(consolePath))
    channel.registerObject("obj", factorial)
    self.console.page().setWebChannel(channel)
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
      "state":self.state_2,
      "version":self.version_2,
      "gamemode":self.gamemode_2,
      "difficulty":self.difficulty_2,
      "levelname":self.levelname_2,
      "port":self.port_2,
      "ram":self.ram_2,
      "cpu":self.cpu_2,
      "enableColorfulLog":self.enableColorfulLog,
      "compatibilityMode":self.compatibilityMode
      })

  def transferCommand(self):
    text=self.input.text()
    outputCommand(text)
    self.input.setText("")

  def control(self,type):
    global state

    if type==1 and state!=1:
      state=1

      self.start.setDisabled(True)
      self.stop.setDisabled(False)
      # self.restart.setDisabled(False)
      # self.forcestop.setDisabled(False)
      self.input.setDisabled(False)
    elif type==2:
      outputCommand("stop")

  def changeState(void,data):
    # self.ver
    pass


class Factorial(QObject):
  @pyqtSlot(str, result=str)
  def factorial(self,void):
    if not logQueue.empty():
      return logQueue.get()
    else:
      return "None"



def server(path):
  global serverProcess,state,stateData,forms
  if not formQueue.empty() and forms=="":
    forms=formQueue.get()

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
    line+=1
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
        # print(log.replace("\n",""))

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
  global serverProcess
  print(command)
  try:
    serverProcess.stdin.write(command+"\n")
  except:
    pass
  logQueue.put(">"+command)


def outputRecognition(log):
  log=re.sub("\[.+?m","",log)# 处理LL加载器下的输入前缀和颜色代码
  log=re.sub("","",log)
  log=re.sub('^> ',"",log)
  log=re.sub('^>',"",log)
  log=re.sub('\s$',"",log)
  return log

def escape(log):
  log=log.replace('/',"&#47;")# 转义防炸
  log=log.replace('"',"&quot;")
  log=log.replace(',',"&#44;")
  log=log.replace(':',"&#58;")
  log=log.replace("<","&lt;")
  log=log.replace(">","&gt;")
  return log

def colorLog(log):
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
  time.sleep(5)
  _state=0
  while True:
    if state==1 and _state==0:
      _state=1
      server(setting["path"])
      _state=0
    if state==1 or _state==1:
      try:
        if not MainWindow.isVisible():
          serverProcess.stdin.write("stop\n")
          break
      except:
        serverProcess.stdin.write("stop\n")
        break
    time.sleep(1)
  exit()

def statusMonitoring():
  global serverProcess,forms
  while True:
    time.sleep(5)
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
      


def gui():
  global MainWindow
  app=QtWidgets.QApplication(sys.argv)
  app.setWindowIcon(QIcon(icoPath))
  MainWindow=QtWidgets.QWidget()
  ui=Ui_MainWindow()
  ui.setupUi(MainWindow)
  MainWindow.show()
  sys.exit(app.exec_())


if __name__=="__main__":
  channel = QWebChannel()
  factorial = Factorial()
  VERSION="Alpha 1.5.20220219"
  selfPath=os.path.dirname(os.path.realpath(sys.argv[0]))
  print("I Run at",selfPath)
  consolePath=os.path.join(selfPath,"console.html")
  icoPath=os.path.join(selfPath,"ico.png")
  formQueue=queue.Queue(maxsize=2)
  commandQueue=queue.Queue(maxsize=100)
  logQueue=queue.Queue(maxsize=10000)
  state=0
  forms=""
  if os.path.exists(os.path.join(selfPath,"setting.ini")):
    settingFile=open(os.path.join(selfPath,"setting.ini"),encoding="UTF-8")
    setting={}
    for line in settingFile:
      if line.find('=') > 0:
        strs = line.replace('\n', '').split('=')
        setting[strs[0]] = strs[1]
  else:
    print("setting.ini文件不存在")
  if not os.path.exists(os.path.join(selfPath,"console.html")):
    print("console.html文件不存在")
  serverThread=threading.Thread(target=startServer)
  serverThread.daemon=1
  serverThread.start()
  monitoringThread=threading.Thread(target=statusMonitoring)
  monitoringThread.daemon=1
  monitoringThread.start()
  gui()
