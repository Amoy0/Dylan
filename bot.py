import re
import time
from queue import *

def messageProcessing(regQueue=Queue):
  global datas,settings
  while True:
    if "regQueue" not in dir():
      continue
    if not regQueue.empty():
      item=regQueue.get()
      if item.get("type")=="datas":
        datas=item
      elif item.get("type")=="settings":
        settings=item
      if item.get("post_type")!="message" or item.get("user_id") is None:
        continue
      qq=item.get("user_id")
      permissionList=settings["msg"]["permissionList"]
      print(qq,item)
      if item.get("message_type")=="group" and item.get("group_id") in settings["msg"]["groupList"]:
        url="http://127.0.0.1:{0}/send_group_msg?group_id={1}&message={2}&auto_escape=false"
        if settings["msg"]["givePermissionToAllAdmin"]:
          if item.get("sender").get("role")=="owner" or item.get("sender").get("role")=="admin":
            permissionList.append(qq)
        if qq in permissionList:
          result=reply(settings,item,datas["regular"]["group_admin"])
        else:
          result=reply(settings,item,datas["regular"]["group"])
      elif item.get("message_type")=="private":
        if qq in permissionList:
          result=reply(settings,item,datas["regular"]["private_admin"])
        else:
          result=reply(settings,item,datas["regular"]["private"])
      print(result)
    else:
      time.sleep(0.1)

def reply(settings,item,datas):
  target=None
  executionContent=None
  for record in datas:
    print(record)
    if not re.search(record["regular"],item["raw_message"]):
      continue
    command=record["command"].split("|",1)
    if len(command)<=1:
      continue
    detailCommand=command[0].upper()
    if detailCommand[0]=="G" and settings["msg"]["groupList"]!=[]:
      if len(detailCommand)==1:
        target=item.get("group_id")
      elif re.search("^\d+?$",detailCommand[2:]):
        target=detailCommand[2:]
    elif detailCommand[0]=="P":
      if len(detailCommand)==1:
        target=item.get("user_id")
      elif re.search("^\d+?$",detailCommand[2:]):
        target=detailCommand[2:]
    executionContent=textProcessing(command[1],record,item["raw_message"])

  return [target,executionContent]

def textProcessing(text,record,content):
  for i in range(len(re.findall(record["regular"],content))):
    print("$"+str(i+1),re.findall(record["regular"],content)[i])
    if type(re.findall(record["regular"],content)[i])==tuple:
      for j in range(len(re.findall(record["regular"],content)[0])):
        text=text.replace("$"+str(j+1),re.findall(record["regular"],content)[0][j])
    elif type(re.findall(record["regular"],content)[i])==str:
      text=text.replace("$"+str(i+1),re.findall(record["regular"],content)[i])
  return text