import re

def colorLog(line:str,type:int):
  '''彩色输出'''
  line=re.sub('^> ',"",line)
  line=re.sub('^>',"",line)
  line=re.sub('\s$',"",line)
  output=""
  if type==1 or type==3:
    for arg in re.findall("\[([^]+?)m([^]*)",line):
      style=""
      spanClass=""
      for childArgIndex in range(len(arg[0].split(";"))):
        childArg=arg[0].split(";")[childArgIndex]
        if childArg=="1":
          style=style+"font-weight:bold;"
        elif childArg=="3":
          style=style+"font-style: italic;"
        elif childArg=="4":
          style=style+"text-decoration: underline;"
        elif childArg=="38" and arg[0].split(";")[childArgIndex+1]=="2" and childArgIndex+4<=len(arg[0].split(";")):
          color2=f"rgb({arg[0].split(';')[childArgIndex+2]},{arg[0].split(';')[childArgIndex+3]},{arg[0].split(';')[childArgIndex+4]})"
          style=style+f"color:{color2};"
        elif childArg=="48" and arg[0].split(";")[childArgIndex+1]=="2" and childArgIndex+4<=len(arg[0].split(";")):
          color2=f"rgb({arg[0].split(';')[childArgIndex+2]},{arg[0].split(';')[childArgIndex+3]},{arg[0].split(';')[childArgIndex+4]})"
          style=style+f"background:{color2};"
        elif childArg in [
          "30",
          "31",
          "32",
          "33",
          "34",
          "35",
          "36",
          "37",
          "40",
          "41",
          "42",
          "43",
          "44",
          "45",
          "46",
          "47",
          "91"
          ]:
          spanClass=spanClass+"color"+childArg+" "
      if spanClass!="":
        spanClass=spanClass+"colored "
      if arg[1]!="":
        output=output+f"<span style='{style}' class='{spanClass}'>{arg[1]}</span>"
    if type==3:
      output=re.sub("\[(SERVER|server|Server)\]",r"[<span class='server'>\1</span>]",output) #server
      output=re.sub("\[([A-Za-z0-9\s]+?)\]",r"[<span class='plugins \1'>\1</span>]",output)  #ck
      output=re.sub("([0-9A-Za-z\._-]+\.)(py|jar|dll|exe|bat|json|lua|js|yaml|png|jpg|csv|log)",r"<span class='file'>\1\2</span>",output)#{files}
      output=re.sub("(\d{5,})",r"<span class='int'>\1</span>",output)#{files}
  elif type=="2":
    line=re.sub("\[.+?m","",line)
    line=re.sub("","",line)
    line=re.sub("([\[\s])(INFO|info|Info)",r"\1<span class='info'>\2</span>",line) #info
    line=re.sub("([\[\s])(WARNING|warning|Warning)",r"\1<span class='warn'><b>\2</b></span>",line) #warn
    line=re.sub("([\[\s])(WARN|warn|Warn)",r"\1<span class='warn'><b>\2</b></span>",line) #warn
    line=re.sub("([\[\s])(ERROR|error|Error)",r"\1<span class='error'><b>\2</b></span>",line) #error
    line=re.sub("([\[\s])(DEBUG|debug|Debug)",r"\1<span class='debug'>\2</span>",line) #debug
    line=re.sub("\[(SERVER|server|Server)\]",r"[<span class='server'>\1</span>]",line) #server
    line=re.sub("\[([A-Za-z0-9\s-]+?)\]",r"[<span class='plugins \1'>\1</span>]",line)  #ck
    line=re.sub("([0-9A-Za-z\._-]+\.)(py|jar|dll|exe|bat|json|lua|js|yaml|png|jpg|csv|log)",r"<span class='file'>\1\2</span>",line)#{files}
    line=re.sub("(\d{5,})",r"<span class='int'>\1</span>",line)#{files}
    output=line
  return(output)

def outputRecognition(line:str):
  '''处理输入前缀和颜色代码'''
  line=re.sub("\[.+?m","",line)
  line=re.sub("","",line)
  line=re.sub('^> ',"",line)
  line=re.sub('^>',"",line)
  line=re.sub('\s$',"",line)
  return line

def escapeLog(line:str):
  '''转义log中的部分字符'''
  line=line.replace('/',"&#47;")
  line=line.replace('"',"&quot;")
  line=line.replace(',',"&#44;")
  line=line.replace(':',"&#58;")
  line=line.replace("<","&lt;")
  line=line.replace(">","&gt;")
  return line
