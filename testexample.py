import Global 
import random
import os 



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
        
        fopen = open(Global.ADDRESS,"w",encoding = "utf-8")
    
    def mAkedir(self):
        #   try 'data' is exist? if yes do remove else if no do build
	    if os.path.exists(Global.ADDRESS):
		    self.rEmovedir()
	    else:
    		for address,Dir,File in os.walk('.\\'):
			    print(".\\"+Global.ADDRESS)
			    os.makedirs(".\\"+Global.ADDRESS)

    def rEmovedir(self,address = os.getcwd()+'\\data'):	
        #   remove dir 'data'
        command = "rmdir %s /s /q"
        try:
            command = command % address
            result = os.system(command)
            if result == 0:
                print("\n已刪除: "+os.getcwd()+"\\data")
                print("***********************************")
            else:
                print("\nWARN:刪除失敗")
                print("***********************************")
        except:
            pass