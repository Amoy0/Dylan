import datetime
import queue
import threading
import time
import re
from command import *
from crontab import CronTab

class Task(object):
  def __init__(
    self,
    commandQueue:queue.Queue
    ) -> None:
    self.taskList={}
    self.commandQueue=commandQueue
    self.threading=threading.Thread(target=self.loop,daemon=True)
    self.threading.start()

  def check(self):
    '''检测运行时间'''
    for task in list(self.taskList.keys()):
      if self.taskList[task]["type"]==0 or self.taskList[task]["command"]=="" or self.taskList[task]["name"]=="" or self.taskList[task]["value"]=="":
        continue
      elif self.taskList[task].get("time")==None:
        self.taskList[task]=self.updateTaskTime(self.taskList[task])
        if self.taskList[task].get("time")==None:
          continue
      elif self.taskList[task]["time"]<time.time():
        cmdProcess(
          commandQueue=self.commandQueue,
          settings=self.settings,
          command=self.taskList[task]["command"]
          )
        self.taskList[task]=self.updateTaskTime(self.taskList[task])

  def updateSettings(self,settings:dict):
    '''更新设置'''
    self.settings=settings

  def updateTaskList(self,newTaskList:dict):
    '''更新任务列表'''
    if newTaskList=={}:
      self.taskList.clear()
      return True
    for newTask in newTaskList:
      new=True
      for task in list(self.taskList.keys()):
        if self.taskList[task]["name"]==newTaskList[newTask]["name"]:
          self.taskList[task]["value"]=newTaskList[newTask]["value"]
          self.taskList[task]["type"]=newTaskList[newTask]["type"]
          self.taskList[task]["command"]=newTaskList[newTask]["command"]
          new=False
      if new:
        self.taskList[newTask]=newTaskList[newTask]
    for task in list(self.taskList.keys()):
      if task not in newTaskList:
        self.taskList.pop(task)

  def updateTaskTime(self,task:dict):
    ''''更新任务时间'''
    task["value"]=task["value"].rstrip(' ')
    if task.get("type")==None or task.get("value")==None:
      pass
    elif task["type"]==1:
      if re.search("^[\d]{0,}\.?[\d]{1,}$",task["value"]):
        if float(task["value"])>0.01:
          task["time"]=time.time()+float(task["value"])
        else:
          task["time"]=time.time()+0.01
      else:
        task["time"]=time.time()*2
    elif task["type"]==2:
      try:
        task["time"]=CronTab(task["value"]).next(default_utc=False)+time.time()
      except Exception as e:
        # print(e)
        pass
    return task

  def loop(self):
    '''循环'''
    while True:
      startTime=time.time()
      time.sleep(0.01)
      self.check()
      self.deviationTime=str(format(time.time()-startTime-0.01,".10f"))

  def deviation(self):
    '''返回当前的误差时间'''
    return self.deviationTime