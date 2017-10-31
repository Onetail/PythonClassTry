import Global 
import random
import usage
import os 
import sys
import re


class Test:
	def __init__(self):
		pass
	
	def rAndom(self,number = 10):
		number_list = [random.randint(0,999) for i in range(number)]
		return number_list

	def oPensystem(self,url = ""):
		#   start 'url' in command line
		data = os.system("start " + url) if url != "" else None
		return  data

	def sAvefile(self,data=""):
		
		with open(Global.ADDRESS,"w",encoding = "utf-8") as fopen:
			fopen.write("測試")
			
	
	def mAkedir(self):
		#   try 'data' is exist? if yes do remove else if no do build
		if os.path.exists(Global.ADDRESS):
			self.rEmovedir()
		else:
			print("\n已建立 "+Global.ADDRESS+" 目錄")
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
		
	def mOdelenvironment(self,model):
		#	build a environment in command line
		data = ""
		Global.LOOPMODEL = True
		
		while Global.LOOPMODEL:
			#	use loop model command line
			data = input(">")
			if data.upper() == "EXIT":
				self.bReakloop()
			elif data.upper() == "BUILD":
				if not Global.MODELEXIST:
					model = model.LinkedList("Root","1000")
					Global.MODELEXIST = True	# model is build
					self.mOdelmessage(1)
				else:
					self.mOdelmessage(2)

			else:
				if Global.MODELEXIST:
					if data.upper() == "ADD":
						data = input(">輸入人員姓名,價值: ")
						data = re.split(r"\s+",data)
						if len(data) > 1:
							model.aDd(data[0],data[1])
							self.mOdelmessage(5,data)
						else:
							self.mOdelmessage(4)
				else:
					self.mOdelmessage(3)
					
			
			
	def bReakloop(self):
		#	stop loop
		Global.LOOPMODEL = False

	def mOdelmessage(self,type,data=""):
		string = ""
		string += "\n\t已建立 Linkedlist model.\t" if type == 1 else ""
		string += "\n\tmodel 已存在!\t" if type == 2 else ""
		string += "\n\t請先建立 model (use >'build')\t" if type == 3 else ""
		string += "\n\t請同時輸入姓名與價值!" if type == 4 else ""
		string += "\n\t人員 姓名:{:} 價值:{:} 已加入model!".format(data[0],data[1]) if type == 5 else ""
		string += "\n"
		return print(string)