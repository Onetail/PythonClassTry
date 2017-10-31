import Global
import factory as ft 
import testexample as tse

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
    # newadd.oUtput()
    # print("Update:")
    newadd.uPdate("wayne",500)
    # newadd.oUtput()`
    # print("Delete:")
    # newadd.dElete("wayne")
    # newadd.oUtput()
    
    number_list = {}
    name_list = {}
    test = tse.Test()
    number_list = test.sWitch(3)
    name_list = test.sWitch(3)
    # print(number_list)
    print("Output:")
    for i in range(len(number_list)):
        newadd.aDd(number_list[i],name_list[i])
    newadd.oUtput()
    