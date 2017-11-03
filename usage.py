import sys
import Global
import factory as ft 
import testexample as tse

class Main:
	def __init__(self):
		#   build a linkedlist 
		#   aDd for new a node 
		#   oUtput for see list
		#   uPdate for update node value 
		#   dElete for delete node 
		if len(sys.argv) < 2:
			self.uSage()
		else:
			test = tse.Test()
			model = tse.Model()
			if sys.argv[1][1:].strip().upper() == "MODEL":
				if len(sys.argv) == 3:
					#	for some type doing some thing
					if sys.argv[2][:].strip().upper() == "BUILD":
							pass
					else:
							pass
				else:
						model.mOdelenvironment(ft)	#	normal running type

			elif sys.argv[1][1:].strip().upper() == "OPENURL":
				if len(sys.argv)== 3:
					test.oPensystem(sys.argv[2])
				else:
					self.eRror(1)
			elif sys.argv[1][1:].strip().upper() == "MAKE":
					test.mAkedir()
			else:
				self.uSage()
			# test.mAkedir()

	def uSage(self):
		#	help message
		string =  "\n\t -model\t\t: for use list to control data\t"
		string += "\n\t -openurl\t: for open url brower\t"
		string += "\n\t -make\t\t: build a new dir || overwrite 'data' dir "
		string += "\n"
		return print(string)
	
	def eRror(self,type):
		#	error message
		string = "\n\tError!\t"
		string += "\n\tValue is not enough\t" if type ==1 else None
		string += "\n"
		return print(string)

	# def sUccess(self,type):
	# 	string = "\n"
	# 	string += "\n\t已建立 Linkedlist model.\t" if type == 1 else None
	# 	string += "\n"
	# 	return print(string)
		