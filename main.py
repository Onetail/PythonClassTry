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
    newadd.uPdate("wayne",500)
    number_list = {}
    name_list = {}
    test = tse.Test()
    number_list = test.rAndom()
    name_list = test.rAndom()
    # print(number_list)
    print("Output:")
    for i in range(len(number_list)):
        newadd.aDd(number_list[i],name_list[i])
    newadd.oUtput()
    
    # test.sWitch(2,"http://www.google.com")
    test.mAkedir()