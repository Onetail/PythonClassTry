import assets.python.Global as Global
import re
import assets.python.filesystem as fs
import os	


class Model:
	def mOdelenvironment(self,model):
			#	build a environment in command line
		data = ""
		Global.LOOPMODEL = True
		test = fs.Test()
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
					elif data.strip().upper() == "PRINT" or data.strip().upper() == "LIST" or data.strip().upper() == "LS":
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
					elif data.split(" ")[0].upper() == "SAVE":
						#	save model to file and filename can change
						savedata = model.sAvetofile()
						if os.path.exists(Global.ADDRESS):
							result = test.sAvefile(savedata) if len(data.split(" "))==1 else test.sAvefile(savedata,savefile=data.split(" ")[1])
						else:
							test.mAkedir()
							result = test.sAvefile(savedata) if len(data.split(" "))==1 else test.sAvefile(savedata,savefile=data.split(" ")[1])
						self.mOdelmessage(10) if result else self.mOdelmessage(8)

					elif data.strip().upper() == "RANDOM":
							#	can random 10 number into build model
							randomname = test.rAndom()
							randomvalue = test.rAndom(type="noint")
							for i in range(len(randomname)):
									model.aDd(randomname[i],randomvalue[i])
							self.mOdelmessage(9)
					elif data.strip().upper() == "W" or data.strip().upper() == "WRITE":
							#	input line word save to file
							savefile = input(">>Send you want to save filename(not space): ")
							savefile = savefile.split(" ")[0]
							while 1:
								data = input(">>> ")
								if data.strip().upper() == "EXIT":
									self.mOdelmessage(11)
									break
								elif data.split(" ")[0].upper() == "SAVE":
									self.mOdelmessage(8)
									test.sAvefile(savefile=savefile,type="a+",data="",pack=True) if len(data.split(" "))==1 else test.sAvefile(savefile=savefile,type="a+",data="",pack=True,style=data.split(" ")[1])
								elif  data.strip().upper() == "LIST" or data.strip().upper() =="PRINT" or data.strip().upper() =="LS":
									self.mOdelmessage(12,data = test.rEadfile(readfile=savefile,type="r"))
								elif data.strip().upper() == "UPPER":
									# can remove end line in file and print it 
									self.mOdelmessage(12,data = test.rEadfile(readfile=savefile,type="r",model="endline"))
								elif data.strip().upper() == "HELP":
									#	to help you any feature
									self.mOdelmessage(14)
								
								else:
									test.sAvefile(savefile=savefile,type="a+",data=data,pack=False)
								
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
		string += "\n\tsave (name)\t: to save the file in data ." if type == 7 else ""
		string += "\n\trandom\t: to random 10 number in linkedlist ." if type == 7 else ""
		string += "\n\twrite\t: to write line into file and save it ." if type == 7 else ""

		string += "\n\tAlready save data in file . \t" if type == 8 else ""
		string += "\n\tInsert into 10 random number . \t" if type == 9 else ""
		string += "\n\tCannot use Package to filename . \t" if type == 10 else ""
		string += "\n\tExit write line model . \t" if type == 11 else ""
		string += "\n  {:10} \t".format(data) if type == 12 else ""

		string += "\n\tlist\t: to read file content ." if type == 14 else ""
		string += "\n\tsave\t: to save to Package in Browser ." if type == 14 else ""
		string += "\n\tupper\t: remove end line in file and print it ." if type == 14 else ""


		string += "\n\tError! the Name is not exist" if str(type).upper() == "ENAME" else ""
		string += "\n"
		return print(string)
	