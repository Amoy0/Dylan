import re
import time
from queue import *
from command import *

def regProcessing(regQueue:Queue,commandQueue:Queue):
  '''消息处理'''
  global datas,settings
  while True:
    if "regQueue" not in dir():
      continue
    if not regQueue.empty():
      try:
        item=regQueue.get()
        if item.get("type")=="datas":
          datas=item
        elif item.get("type")=="settings":
          settings=item
        elif item.get("type")=="console":
          reply(settings,item,datas["regular"]["console"],commandQueue)
        if item.get("post_type")!="message" or item.get("user_id") is None:
          continue
        qq=item.get("user_id")
        permissionList=settings["msg"]["permissionList"]
        print(qq,item)
        if item.get("message_type")=="group" and item.get("group_id") in settings["msg"]["groupList"]:
          if settings["msg"]["givePermissionToAllAdmin"]:
            if item.get("sender").get("role")=="owner" or item.get("sender").get("role")=="admin":
              permissionList.append(qq)
          if qq in permissionList:
            reply(settings,item,datas["regular"]["group_admin"],commandQueue)
          else:
            reply(settings,item,datas["regular"]["group"],commandQueue)
        elif item.get("message_type")=="private":
          if qq in permissionList:
            reply(settings,item,datas["regular"]["private_admin"],commandQueue)
          else:
            reply(settings,item,datas["regular"]["private"],commandQueue)
      except Exception as e:
        print(e)
        pass
    else:
      time.sleep(0.1)

def reply(settings,item,datas,commandQueue):
  '''回复处理'''
  if item.get("raw_message") != None:
    content=item.get("raw_message")
  elif item.get("log")!=None:
    content=item.get("log")
  if not re.search('^[\n\s\r]+?$',content):
    for record in datas:
      if not re.search(record["regular"],content):
        continue
      cmdProcess(commandQueue,settings,record["command"],"reg",record,content,item)
      
