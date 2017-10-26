import Global 
# class first upper 
# function second upper
# variable all lower
# global varialbe all upper

class Factory:
        def __init__(self,uid,name="None"):
                self.uid = Global.UID
                self.name = name
                Global.UID += 1
                
        def oUtput(self,text=""):
                text += "\t"+str(self.uid)+"\t\n"
                text += "\t"+self.name+"\t\n"
                return print(text)
class ProductA(Factory):
        def __init__(self,name,value):
                super(self,ProductA).__init__(name)
                self.name = name
                self.value = value
                self.next = null
        
        def uPdate(self,name=self.name,value=self.value):
                self.name = name
                self.value =  value 
        
        def 
                
                

