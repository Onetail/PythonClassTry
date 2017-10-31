import Global 
import random
import os 

class Test:
    def __init__(self):
        pass
    
    def rAndom(self,number = 10):
        number_list = [random.randint(0,999) for i in range(number)]
        return number_list

    def sWitch(self,type = 0,data = ""):
        #   try to use switch function in python dictory
        switch = {
            2: self.oPensystem(data),
            3: self.rAndom()
        }
        
        return switch.get(type)

    def oPensystem(self,url = ""):
        #   start 'url' in command line
        data = os.system("start " + url) if url != "" else None
        return  data