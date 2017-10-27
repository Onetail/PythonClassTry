import Global
import factory as ft 

if  __name__ == '__main__':
    
    #   build a linkedlist 
    #   aDd for new a node 
    #   oUtput for see list
    #   uPdate for update node value 
    #   dElete for delete node 
    
    newadd = ft.LinkedList("111","111")
    newadd.aDd("jjj","200")
    newadd.aDd("wayne","333")
    newadd.aDd("paoso","400")
    newadd.oUtput()
    print("Update:")
    newadd.uPdate("wayne",500)
    newadd.oUtput()
    print("Delete:")
    newadd.dElete("wayne")
    newadd.oUtput()
    
    
    