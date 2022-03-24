import datetime
import os
import queue
import re
import subprocess
import threading
import time
import psutil

from betterLog import *


class Server(object):
  def __init__(
    self,
    commandQueue:queue.Queue,
    logQueue:queue.Queue,
    regQueue:queue.Queue,
    selfPath:str
    ) -> None:
    '''程序入口'''
    self.infomation={}
    self.commandQueue=commandQueue
    self.regQueue=regQueue
    self.logQueue=logQueue
    self.selfPath=selfPath
    self.restart=False
    self.running=False

  def start(self):
    '''启动服务器进程'''
    if self.running:
      return False
    if not os.path.exists(self.settings["start"]["filepath"]):
      return False
    self.infomation={}
    self.serverProcess=subprocess.Popen(
    self.settings["start"]["filepath"],
    stdout=subprocess.PIPE,
    stdin=subprocess.PIPE,
    universal_newlines=True,
    cwd=os.path.split(self.settings["start"]["filepath"])[0],
    bufsize=1,
    encoding="UTF-8"
    )
    threading.Thread(target=self.listening,daemon=True).start()
    threading.Thread(target=self.inputCommand,daemon=True).start()

  def listening(self):
    '''监听服务器输出'''
    self.logQueue.put("#cls")
    self.logQueue.put("[<span style='color:#007ACC'>Dylan</span>]服务器启动中...")
    self.stopFlag=0
    self.started=0
    self.running=True
    while self.running:
      if self.stopFlag>0:
        self.stopFlag-=1
      try:
        log=""
        log=self.serverProcess.stdout.readline()
      except:
        pass
      if log!=None and not re.search('^[\n\s\r]+?$',log) and log!="":
        self.regQueue.put({
          "log":outputRecognition(log),
          "type":"console"
        })
        if self.settings["console"]["enableOutputToLog"]:
          self.logger(log)
        log_=outputRecognition(log)
        if re.search('stop',log_,re.I) or re.search('exit',log_,re.I) or re.search('quit',log_,re.I):
          self.stopFlag=10
        if ((re.search("Server\sstarted\.$",log_) or log_.find("Done")>0)) and self.started==0:
          self.infomation={
            "version":version[:10],
            "gamemode":gamemode,
            "difficulty":difficulty,
            "levelname":levelname[:20],
            "port":ipv4+"/"+ipv6
          }
          self.started=1
        if self.started==0:
          if log_.find("Version")>0:
            version=re.sub("^.+?(version|Version)[:\s]([0-9\.]+).+$",r"\2",log_)
          elif log_.find("Game mode")>0 :
            if log_.find("Survival")>0:
              gamemode="生存"
            elif log_.find("Creative")>0:
              gamemode="创造"
            else:
              gamemode="冒险"
          elif log_.find("Difficulty")>0:
            if log_.find("PEACEFUL")>0:
              difficulty="和平"
            elif log_.find("EASY")>0:
              difficulty="简单"
            elif log_.find("NORMAL")>0:
              difficulty="普通"
            else:
              difficulty="困难"
          elif log_.find("Level Name")>0:
            levelname=re.sub("^(.+?)(Level\sName)[:\s]+?(.+?)$",r"\3",log_)
          elif log_.find("IPv4")>0:
            ipv4=re.sub("^(.+?)(port)[:\s]+?(.+?)$",r"\3",log_)
          elif log_.find("IPv6")>0:
            ipv6=re.sub("^(.+?)(port)[:\s]+?(.+?)$",r"\3",log_)
        log=escapeLog(log)
        log=colorLog(log,self.settings["console"]["colorfulLogOut"])
        self.logQueue.put(log)
      try:
        psutil.Process(self.serverProcess.pid)
      except:
        if self.settings["start"]["autoRestart"] and self.stopFlag==0:
          self.restart=True
        self.running=False
      finally:
        if bool(self.serverProcess.poll()) or self.running==False:
          self.running=False
          self.logQueue.put("<br>")
          if self.stopFlag>0:
            self.logQueue.put(("[<span style='color:#007ACC'>Dylan</span>]服务器进程已退出"))
          elif self.stopFlag==-1:
            self.logQueue.put(("[<span style='color:#007ACC'>Dylan</span>]服务器进程被强制结束"))
          else:
            self.logQueue.put(("[<span style='color:#007ACC'>Dylan</span>]服务器进程疑似异常终止"))
          if self.restart:
            self.logQueue.put(("[<span style='color:#007ACC'>Dylan</span>]服务器将在5s后重启 Tip:可按下停止按钮停用重启进程"))
            for i in range(10):
              time.sleep(0.5)
              if not self.restart:
                self.logQueue.put(("[<span style='color:#007ACC'>Dylan</span>]重启已取消"))
                break
            if self.restart:
              self.start()
          break
 
  def outputCommand(self,command:str):
    '''将指令输出至bds和控制台'''
    if self.settings["console"]["outputCommandToConsole"]:
      self.logQueue.put(">"+command)
    if self.settings["console"]["enableOutputToLog"]:
      self.logger(
        f"{str(datetime.datetime.now().time()).split('.')[0]} COMMAND {command}"
        )
    if command=="#start":
      self.run()
    elif command=="#refresh":
      self.logQueue.put(command)
    else:
      try:
        self.serverProcess.stdin.write(command+"\n")
      except:
        pass

  def logger(self,text:str):
    '''控制台消息输出'''
    with open(
      os.path.join(
        self.selfPath,"log",
        f"console-{datetime.date.today()}.log"
      ),
      "a",
      encoding="UTF-8"
      ) as logFile:
      logFile.write(outputRecognition(text)+"\n")

  def updateSettings(self,settings:dict):
    '''更新设置'''
    self.settings=settings

  def isRunning(self):
    '''返回运行状态'''
    return self.running

  def isWaitingRestart(self):
    '''返回重启状态'''
    return self.restart

  def info(self):
    '''返回状态'''
    return self.infomation

  def changeRestart(self,restart):
    '''更改重启状态'''
    self.restart=restart

  def inputCommand(self):
    '''输入命令'''
    while self.isRunning:
      if not self.commandQueue.empty():
        self.outputCommand(self.commandQueue.get())
      time.sleep(0.1)
  
  def forceStop(self):
    '''强制结束进程'''
    process=psutil.Process(self.serverProcess.pid)
    while True:
      if process.name()!="cmd.exe":
        process.terminate()
        self.stopFlag=-1
        break
      else:
        if process.children()!=[]:
          process=process.children()[0]
        else:
          break
    self.running=False
    self.restart=False