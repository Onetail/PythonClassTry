import assets.python.Global as Global

class Style:
	def fIlestyle(self,data="",savefile="",color="#ffaacc",fontsize="36px"):
		with open(Global.ADDRESS+"/"+savefile,"r",encoding = "utf-8") as fopen:
			data = fopen.read()
		with open(Global.ADDRESS+"/"+savefile,"w+",encoding = "utf-8") as fopen:
			fopen.write("<div class='scrollbar'><div id='centerframe'>")
			fopen.write("<div style='color:"+color+";font-size:"+fontsize+"'><pre>")
			fopen.write("\n"+data) if data != "" else fopen.write("")

	def rEmovestyle(self,data="",savefile=""):
		with open(Global.ADDRESS+"/"+savefile,"r",encoding="utf-8") as fopen:
			data = fopen.read()
		data = data.split("\n")
		data[0] = ""
		with open(Global.ADDRESS + "/" +savefile,+"w+",encoding="utf-8") as fopen:
			for i in range(len(data)):
				fopen.write("\n"+data[i])