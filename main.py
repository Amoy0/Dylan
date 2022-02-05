import os
import tkinter
import threading
import subprocess
# root=tkinter.Tk()
# root.title("sb")
# tkinter.Text(root).pack()
# root.mainloop()

TempCommandList=[]
path=r"C:/Users/QZ_wht/Desktop/Programming/mcm/bedrock-server-1.18.2.03 (1)/bedrock_server.exe"
process=subprocess.Popen(path,stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True, bufsize=1)
while 1:
  print(process.stdout.readline().replace("\n",""))
  if bool(process.poll()):
    print(process.poll())
    break
