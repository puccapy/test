#coding: utf-8
'''
Created on 2017-09-21

@author: lenovo
'''
import Login_Jira
import json  
  

def format_json():
    jsonstr=Login_Jira.Login().get()
    length = len(jsonstr)  
    print "=================================="  
    if length > 1:  
        try:  
            jsonObj = json.loads(jsonstr)  
            formatJsonStr = json.dumps(jsonObj,indent=4,ensure_ascii=False,sort_keys=True)  
            print formatJsonStr
            print type(formatJsonStr)
            print type(jsonObj)           
        except Exception, e:  
            print e  
            print "json parse error."  
        else :  
            print "描述：%s"%jsonObj['fields'][u'description']
            return formatJsonStr
    else:
        print 'no data'
        
if __name__=='__main__':        
    format_json()
    