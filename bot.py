import os
import re
import time
from queue import *

import requests

def messageProcessing(regQueue=Queue,commandQueue=Queue):
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
          result=reply(settings,item,datas["regular"]["console"],commandQueue)
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
      except Exception:
        print(Exception)
        pass
    else:
      time.sleep(0.1)

def reply(settings,item,datas,commandQueue):
  url="http://127.0.0.1:{0}/send_group_msg?group_id={1}&message={2}&auto_escape=false"
  target=None
  detailCommand=None
  executionContent=None
  if item.get("raw_message") != None:
    content=item.get("raw_message")
  elif item.get("log")!=None:
    content=item.get("log")
  for record in datas:
    if not re.search(record["regular"],content):
      continue
    command=record["command"].split("|",1)
    if len(command)<=1:
      continue
    detailCommand=command[0].upper()
    executionContent=textProcessing(command[1],record,content)
    if detailCommand[0]=="G" and settings["msg"]["groupList"]!=[]:
      if len(detailCommand)==1:
        target=item.get("group_id")
      elif re.search("^\d+?$",detailCommand[2:]):
        target=detailCommand[2:]
      else:
        continue
      requests.get(f'http://127.0.0.1:{settings["bot"]["sendPort"]}/send_group_msg?group_id={target}&message={executionContent}&auto_escape=false')
    elif detailCommand[0]=="P":
      if len(detailCommand)==1:
        target=item.get("user_id")
      elif re.search("^\d+?$",detailCommand[2:]):
        target=detailCommand[2:]
      else:
        continue
      requests.get(f'http://127.0.0.1:{settings["bot"]["sendPort"]}/send_msg?message_type=private&user_id={target}&message={executionContent}&auto_escape=false')

    elif detailCommand=="C":
      commandQueue.put(executionContent)
    elif detailCommand=="CMD":
      os.system(executionContent)
  print([detailCommand,target,executionContent])

def textProcessing(text,record,content):
  for i in range(len(re.findall(record["regular"],content))):
    if type(re.findall(record["regular"],content)[i])==tuple:
      for j in range(len(re.findall(record["regular"],content)[0])):
        text=text.replace("$"+str(j+1),re.findall(record["regular"],content)[0][j])
    elif type(re.findall(record["regular"],content)[i])==str:
      text=text.replace("$"+str(i+1),re.findall(record["regular"],content)[i])
  return text
