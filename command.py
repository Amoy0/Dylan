from queue import *
import os
import requests
import re

def execute(commandQueue:Queue,settings:dict,type:str,object:str,args=None):
  if type=="cq-group":
    requests.get(f'http://127.0.0.1:{settings["bot"]["sendPort"]}/send_group_msg?group_id={object}&message={args}&auto_escape=false')
  elif type=="cq-private":
    requests.get(f'http://127.0.0.1:{settings["bot"]["sendPort"]}/send_msg?message_type=private&user_id={object}&message={args}&auto_escape=false')
  elif type=="server-cmd":
    commandQueue.put(object)
  elif type=="system-cmd":
    os.system(object)

def cmdProcess(commandQueue,settings,command,type=None,record=None,content=None,item=None):
  command=command.split("|",1)
  if len(command)<=1:
    return None
  detailCommand=command[0].upper()
  if type=="reg":
    executionContent=textProcessing(command[1],record,content)
  else:
    executionContent=command[1]
  if detailCommand[0]=="G":
    if len(detailCommand)==1:
      target=item.get("group_id")
    elif re.search("^\d+?$",detailCommand[2:]):
      target=detailCommand[2:]
    else:
      return None
    execute(commandQueue,settings,"cq-group",target,executionContent)
  elif detailCommand[0]=="P":
    if len(detailCommand)==1:
      target=item.get("user_id")
    elif re.search("^\d+?$",detailCommand[2:]):
      target=detailCommand[2:]
    else:
      return None
    execute(commandQueue,settings,"cq-private",target,executionContent)
  elif detailCommand=="C":
    execute(commandQueue,settings,"server-cmd",executionContent)
  elif detailCommand=="CMD":
    execute(commandQueue,settings,"system-cmd",executionContent)
  return True

def textProcessing(text,record,content):
  '''文本匹配处理'''
  for i in range(len(re.findall(record["regular"],content))):
    if type(re.findall(record["regular"],content)[i])==tuple:
      for j in range(len(re.findall(record["regular"],content)[0])):
        text=text.replace("$"+str(j+1),re.findall(record["regular"],content)[0][j])
    elif type(re.findall(record["regular"],content)[i])==str:
      text=text.replace("$"+str(i+1),re.findall(record["regular"],content)[i])
  return text