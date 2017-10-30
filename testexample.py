import Global 
import random

class Test:
    def __init__(self):
        pass
    
    def rAndom(self,number = 10):
        number_list = [random.randint(0,999) for i in range(number)]
        return number_list

    def sWitch(self):
        #   try to use switch function in python dictory
        score = int(input("Enter: "))
        switch = score
        {
            1: lambda : print("test1"),
            2: lambda : print("test2")
        }.setdefault(switch,lambda:print("none"))()
        return switch