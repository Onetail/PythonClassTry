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
        
        #       to print class value
        def oUtput(self,text=""):
                text += "\t"+str(self.uid)+"\t\n"
                text += "\t"+self.name+"\t\n"
                return print(text)
class ProductA(Factory):
        
        def __init__(self,name,value):
                super(ProductA,self).__init__(name)
                self.name = name
                self.value = value
                ProductA.next = None 
        
        def uPdate(self,name=None,value=None):
                self.name = name if name is None else self.name
                self.value = value  if value is None else self.value
        
        #       to overwrite print
        def oUtput(self,text=""):
                text+= "\t" +str(self.uid)+"\t\n"
                text+= "\t" +str(self.name)+"\t\n"
                text+= "\t" +str(self.value)+"\t\n"
                return print(text)
        
                

class LinkedList(ProductA):
        def __init__(self,name,value):
                super(LinkedList,self).__init__(name,value)
                self.name = name 
                self.value = value 
                ProductA.first = None 
                ProductA.last = None 
                self.aDd(self.name,self.value)
        
        def aDd(self,name,value):
                newnode = ProductA(name,value)
                if ProductA.first == None:
                        ProductA.first = newnode
                else:
                        ProductA.last.next = newnode
                ProductA.last = newnode
        
        def uPdate(self,name,value):
                tmp = ProductA.first 
                while tmp != None:
                        tmp.value = value if tmp.name == name else tmp.value
                        tmp = tmp.next

        def dElete(self):
                pass 

        def oUtput(self):
                ProductA.tmp = ProductA.first 
                while ProductA.tmp != None:
                        print("{:}\t{:}\t{:}".format(ProductA.tmp.uid,ProductA.tmp.name,ProductA.tmp.value))
                        ProductA.tmp = ProductA.tmp.next