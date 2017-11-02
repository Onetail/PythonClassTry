import Global 
import random
import usage
import os 
import sys
import re


class Test:
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
		
	

class Model:
	def mOdelenvironment(self,model):
			#	build a environment in command line
		data = ""
		Global.LOOPMODEL = True
		
		while Global.LOOPMODEL:
			#	use loop model command line
			data = input(">")
			if data.strip().upper() == "EXIT" or data.strip().upper() == "BYE":
				self.bReakloop()
			elif data.strip().upper() == "BUILD":
				if not Global.MODELEXIST:
					model = model.LinkedList("Root","1000")
					Global.MODELEXIST = True	# model is build
					self.mOdelmessage(1)
				else:
					self.mOdelmessage(2)

			else:
				if Global.MODELEXIST:
					if data.strip().upper() == "ADD":
						data = input(">Enter personnel 'Name' and 'Value': ")
						data = data.strip()
						data = re.split(r"\s+",data)
						if len(data) > 1:
							model.aDd(data[0],data[1])
							self.mOdelmessage(5,data)
						else:
							self.mOdelmessage(4)
					elif data.strip().upper() == "PRINT" or data.strip().upper() == "LIST":
							model.oUtput()
					elif data.strip().upper() == "DELETE":
							data = input(">Enter want to delete personnel 'Name': ")
							data = data.strip()
							if model.iSexist(data):
								model.dElete(data)
								self.mOdelmessage(6,data)
							else:
								self.mOdelmessage("Ename")	#	error name not exist 
								
					elif data.strip().upper() == "UPDATE":
							data = input(">Enter want to modify personnel Name:")
							data = data.strip()
							_ = input(">New 'Value':")
							_ = _.strip()
							data = (data,_)
							if model.iSexist(data[0]):
								model.uPdate(data[0],data[1])
							else:
								self.mOdelmessage("Ename")
					else:
						self.mOdelmessage(7)	
				else:
					self.mOdelmessage(3)		
			
			
	def bReakloop(self):
		#	stop loop
		Global.LOOPMODEL = False

	def mOdelmessage(self,type,data=""):
		string = ""
		string += "\n\tBuild Linkedlist model success!\t" if type == 1 else ""
		string += "\n\tmodel is exist!\t" if type == 2 else ""
		string += "\n\tPlease first to build model (use >'build')\t" if type == 3 else ""
		string += "\n\tPlease enter two value for 'name' and 'value'!" if type == 4 else ""
		string += "\n\tPersonnel Name:{:} Value:{:} add to model!".format(data[0],data[1]) if type == 5 else ""
		string += "\n\tDelete Name:{:} from model".format(data) if type == 6 else ""
		
		string += "\n\tPlease Enter correct command\t" if type == 7 else ""
		string += "\n\tadd\t: to add a new personnel in model ."if type == 7 else ""
		string += "\n\tdelete\t: to delete a personnel from model ."if type == 7 else ""
		string += "\n\tupdate\t: to update already exist personnel's value ."if type == 7 else ""
		string += "\n\tprint\t: to print detail from model ." if type == 7 else ""
		
		string += "\n\tError! the Name is not exist" if str(type).upper() == "ENAME" else ""
		string += "\n"
		return print(string)
	