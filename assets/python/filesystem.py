import os 
import assets.python.Global as Global
import random

class Test:
	def rAndom(self,number = 10,type="normal"):
		number_list = [chr(random.randint(0,128)) for i in range(number)] if type == "normal" else [random.randint(0,999) for i in range(number)]
		return number_list

	def oPensystem(self,url = ""):
		#   start 'url' in command line
		data = os.system("start " + url) if url != "" else None
		return  data

	def sAvefile(self,data="",savefile="data.txt",type="w",pack = True):	# if model == write pack == false save == true
		if savefile =="":	#	if save = ' ' is error
			savefile = "data.txt"
		if savefile != "Package":
			with open(Global.ADDRESS+"/"+savefile,type,encoding = "utf-8") as fopen:
				fopen.write(data+"\n")
			if savefile != "data.txt" and pack == True:
				if not os.path.exists(Global.ADDRESS+"/Package"):	#	if package not exists run
					with open(Global.ADDRESS +"/Package","w",encoding="utf-8") as fopen:
							fopen.write("")
				with open(Global.ADDRESS+"/Package","a+",encoding="utf-8") as fopen:
					fopen.write(savefile+" ")		
				
			return False
		else:
			return True
	def mAkedir(self):
		#   try 'data' is exist? if yes do remove else if no do build
		if os.path.exists(Global.ADDRESS):
			self.rEmovedir()
		else:
			print("\nBuild "+Global.ADDRESS+" Dir")
			os.makedirs(".\\"+Global.ADDRESS)

	def rEmovedir(self,address = os.getcwd()+'\\data'):	
		#   remove dir 'data'
		command = "rmdir %s /s /q"
		command = command % address
		result = os.system(command)
		if result == 0:
			print("\n已刪除: "+os.getcwd()+"\\data\n***********************************")
		else:
			print("\nWARN:刪除失敗\n***********************************")
