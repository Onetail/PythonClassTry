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

	def sAvefile(self,data="",savefile="data.txt",type="w",pack = True,style="scroll"):	# if model == write pack == false save == true
		if savefile =="":	#	if save = ' ' is error
			savefile = "data.txt"
		if savefile != "Package":
			if style.upper() == "MODEL1":
				with open(Global.ADDRESS+"/"+savefile,"r",encoding = "utf-8") as fopen:
					data = fopen.read()
				with open(Global.ADDRESS+"/"+savefile,"w+",encoding = "utf-8") as fopen:
					fopen.write("<div>")
					fopen.write("<div style='color:#ffaa39;font-size:48px'>")
					fopen.write("\n"+data) if data != "" else fopen.write("")
			elif style.upper()=="SCROLL":		
				with open(Global.ADDRESS+"/"+savefile,type,encoding = "utf-8") as fopen:
					fopen.write("\n"+data)
			else:
				print("\n\tNot have this save mode\n")

			if savefile != "data.txt" and pack == True:
				self.sAvepackagedata(savefile=savefile)
				
			return False
		else:
			return True

	def rEadfile(self,readfile="data.txt",type="r",model="normal"):
		if readfile=="":
			readfile = "data.txt"
		with open(Global.ADDRESS+"/"+readfile,type,encoding="utf=8") as fopen:
			data = fopen.read()
			if model != "normal":
				datasize = data.split('\n')
				response = datasize[len(datasize)-1] if datasize[len(datasize)-1]!='' else "此行無資料"
				with open(Global.ADDRESS+"/"+readfile,"w+",encoding="utf-8") as f:
					for i in range(len(datasize)-1):
						f.write(datasize[i]+"\n") if i != len(datasize)-2 else f.write(datasize[i])
				return response
		return data
			

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

	def sAvepackagedata(self,savefile=""):
		# deal with Package problem repeat filename and space list
		if not os.path.exists(Global.ADDRESS+"/Package"):	#	if package not exists run
			with open(Global.ADDRESS +"/Package","w",encoding="utf-8") as fopen:
				fopen.write("")
			# if filename is repeat , do overwrite else add in Package
		with open(Global.ADDRESS+"/Package","r",encoding="utf-8") as f:
			Packagedata = f.read()
			Packagedata = Packagedata.split(" ")
			for i in range(len(Packagedata)):
				if Packagedata[i] == savefile:
					#repeat ! 
					del Packagedata[i]
					break
			# remove list more space
			Packagedata.remove('')
			with open(Global.ADDRESS+"/Package","w+",encoding="utf-8") as f:
				for i in range(len(Packagedata)):
					f.write(Packagedata[i]+" ")
		with open(Global.ADDRESS+"/Package","a+",encoding="utf-8") as fopen:
			fopen.write(savefile+" ")		