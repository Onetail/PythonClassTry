import Global 
import random

class Test:
    def __init__(self):
        pass
    
    def rAndom(self,number = 10):
        number_list = [random.randint(0,999) for i in range(number)]
        return number_list

    def sWitch(self,type = 0):
        #   try to use switch function in python dictory
        switch = {
            3: self.rAndom()
        }
        
        return switch.get(type)