import os
import re
import subprocess
import sys
import threading
import queue
from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5
from PyQt5.QtGui import QIcon ,QTextCursor
import gui



VERSION="Alpha 1.0.20220207"
selfPath=os.path.split(os.path.realpath(__file__))[0]





class Ui_MainWindow(object):
  def setupUi(self, MainWindow):
    MainWindow.setObjectName("MainWindow")
    MainWindow.setEnabled(True)
    MainWindow.resize(800, 450)
    MainWindow.setMinimumSize(QtCore.QSize(400, 225))
    MainWindow.setMaximumSize(QtCore.QSize(1600, 16777215))
    MainWindow.setWindowOpacity(1.0)
    MainWindow.setAutoFillBackground(False)
    self.centralwidget = QtWidgets.QWidget(MainWindow)
    self.centralwidget.setObjectName("centralwidget")

    self.console = QtWidgets.QTextEdit(self.centralwidget)
    self.console.setGeometry(QtCore.QRect(239, 10, 551, 350))
    font = QtGui.QFont()
    font.setFamily("Courier")
    font.setPointSize(10)
    self.console.setReadOnly(True)

    self.console.setFont(font)
    self.console.setObjectName("console")

    self.input = QtWidgets.QLineEdit(self.centralwidget)
    self.input.setGeometry(QtCore.QRect(239, 370, 501, 51))
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    self.input.setFont(font)
    self.input.setFocusPolicy(QtCore.Qt.ClickFocus)
    self.input.setReadOnly(False)
    self.input.setObjectName("input")
    self.enter = QtWidgets.QPushButton(self.centralwidget)
    self.enter.setEnabled(True)
    self.enter.setGeometry(QtCore.QRect(750, 370, 40, 51))
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    self.enter.setFont(font)
    self.enter.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    self.enter.setAcceptDrops(False)
    self.enter.setObjectName("enter")
    self.label = QtWidgets.QLabel(self.centralwidget)
    self.label.setGeometry(QtCore.QRect(10, 10, 200, 40))
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    self.label.setFont(font)
    self.label.setScaledContents(False)
    self.label.setWordWrap(False)
    self.label.setObjectName("label")
    self.label_2 = QtWidgets.QLabel(self.centralwidget)
    self.label_2.setGeometry(QtCore.QRect(10, 50, 200, 40))
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    self.label_2.setFont(font)
    self.label_2.setScaledContents(False)
    self.label_2.setWordWrap(False)
    self.label_2.setObjectName("label_2")
    self.label_3 = QtWidgets.QLabel(self.centralwidget)
    self.label_3.setGeometry(QtCore.QRect(10, 90, 200, 40))
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    self.label_3.setFont(font)
    self.label_3.setScaledContents(False)
    self.label_3.setWordWrap(False)
    self.label_3.setObjectName("label_3")
    self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
    self.groupBox.setGeometry(QtCore.QRect(10, 350, 225, 70))
    self.groupBox.setObjectName("groupBox")
    self.start = QtWidgets.QPushButton(self.groupBox)
    self.start.setGeometry(QtCore.QRect(5, 15, 105, 51))
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    self.start.setFont(font)
    self.start.setObjectName("start")
    self.stop = QtWidgets.QPushButton(self.groupBox)
    self.stop.setGeometry(QtCore.QRect(115, 15, 105, 51))
    font = QtGui.QFont()
    font.setFamily("宋体")
    font.setPointSize(10)
    self.stop.setFont(font)
    self.stop.setObjectName("stop")
    self.statusbar = QtWidgets.QStatusBar(MainWindow)
    self.statusbar.setObjectName("statusbar")

    self.retranslateUi(MainWindow)
    QtCore.QMetaObject.connectSlotsByName(MainWindow)

    formQueue.put(item={
      "console":self.console
    })

  def retranslateUi(self, MainWindow):
    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "Server Manager "+VERSION))
    self.enter.setText(_translate("MainWindow", "△"))
    self.label.setText(_translate("MainWindow", "TextLabel"))
    self.label_2.setText(_translate("MainWindow", "TextLabel"))
    self.label_3.setText(_translate("MainWindow", "TextLabel"))
    self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
    self.start.setText(_translate("MainWindow", "启动"))
    self.stop.setText(_translate("MainWindow", "停止"))

  def command(self):
    command=input.lineEdit.text()
    pass

def server(path):
  lines=0

  queue=formQueue.get()
  console=queue["console"]
  serverProcess=subprocess.Popen(
    path,
    stdout=subprocess.PIPE,
    stdin=subprocess.PIPE,
    universal_newlines=True,
    bufsize=1,
    encoding="UTF-8"
    )
  while True:
    log=serverProcess.stdout.readline()
    log=log.replace("\n","")
    if not re.search('^[\n\s\r]+?$',log) and log!="" and log!=None:
      print(log)
      logOut(console,log)
    if bool(serverProcess.poll()):
      print(f"服务器已退出，返回：{serverProcess.poll()}")
      break
    lines+=1
    if lines>1000:
      console.insertText("")


def logOut(console,text):
  cursor = console.textCursor()
  cursor.movePosition(QTextCursor.End)
  cursor.insertText(text+"\n")
  console.setTextCursor(cursor)
  console.ensureCursorVisible()

def gui():
  app=QtWidgets.QApplication(sys.argv)  
  MainWindow=QtWidgets.QWidget()  
  ui=Ui_MainWindow()  
  ui.setupUi(MainWindow)  
  MainWindow.show()  
  sys.exit(app.exec_())  

formQueue=queue.Queue(maxsize=10)


path=r"C:/Users/QZ_wht/Desktop/Programming/mcm/bedrock-server-1.18.2.03 (1)/bedrock_server.exe"

gui_=threading.Thread(target=gui)
gui_.start()
server(path)
exit()
