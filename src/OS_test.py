# coding: utf-8
'''
Created on Created on 2017-09-21

@author: lenovo
'''
class Os_test:
    def run_test(self):
        import os

        print os.listdir(r'E:\\')
        os.chdir(r'E:\\')
        #os.removedirs('0921')
        #os.mkdir('0921')
        print os.listdir(r'E:\\')
        rs = os.listdir(r'E:\\')
        for x in rs:
            print x
        #os.rename('111', '09211')
        dir1 = os.path.join('E:\\', rs[1])
        print dir1
        os.chdir(dir1)
        print os.getcwd()
        #print os.getenv('JAVA_HOME')
        filename = '1.txt'
        #f = open(filename, 'a')
        #f.write('dsdsd'+'\n')
        lines_list=[]
        with open(filename, 'r') as file_to_read:
            lines = file_to_read.readlines()
            for a in lines:
                print a
                lines_list.append(a)
                #f.close()
        f2 = open('2.txt','w')
        l=lines
        f2.writelines(l)
        f2.close()
           
if __name__ == "__main__":
#    os_test=Os_test()
#    os_test.run_test()
    pass
    



        