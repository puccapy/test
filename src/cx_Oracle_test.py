# coding:utf-8
'''
Created on 2017年9月18日

@author: lenovo
'''
import cx_Oracle
import os
#import OS_test
def main():
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

    db = cx_Oracle.connect('yjstmp', 'ssi123', '172.29.2.35:1522/YYFAX')

    print "数据库版本：" + db.version
    print db.password
    cr = db.cursor()  

    pr = {'serialno':'LA20160428000002'}
    sql = 'select  * from  ph_loanplan  where serialno=:serialno order by repaydate asc'
    cr.execute(sql, pr)

##print "\n打印全部："

    rs = cr.fetchall() 

    print "print all:%s" % rs

    print "语句%s" % sql + "的查询结果打印:"

    for x in rs:
# print "备注：%s"%x[10]
        print x
    print "%s"%__name__
#OS_test.Os_test().run_test()
#os_test.run_test()
if __name__ == "__main__":
# main()
    import Login_Jira
    print Login_Jira.Login().print_jira()