#coding: utf-8
'''
Created on Created on 2017-09-21

@author: lenovo
'''
from jira import JIRA
import urllib, urllib2
import json

class Login:

    def __init__(self):
        #登录jira
        self.username = 'huangdxb'
        self.password = '831292puccatb'
        self.jira = JIRA("http://172.29.2.140:8001", basic_auth=(self.username, self.password))
        self.ISSUE_ID = '24086'
        
    def print_jira(self):
        try:
            issue = self.jira.issue(self.ISSUE_ID)
        except Exception,e:
            print e
        else :
            print issue.fields.summary + '\n'
            print issue.fields.description + '\n'
            print issue.fields.security.id+ '\n'
            print issue.fields.priority.id
            print type(issue.fields.description)
            print str(issue.fields.issuetype) + '\n'
            print type(issue.fields.issuetype)
            print issue.fields.project.name + '\n'
            print issue.fields.creator.displayName + '\n'
            
            issue_dict = {
                   'project': {'id': 10603},
                   'summary': '【'+issue.fields.project.name+'】'+'【生产缺陷】'+'New issue from jira-python7',
                   'description': 'Look into this one',
                   'issuetype': {'name': '生产缺陷'},
                   'security':{'id': '10101'},
                   'priority':{'id':'2'}
                         }
            new_issue = self.jira.create_issue(fields=issue_dict)
            print type(new_issue)
    
    def get(self):
        try :
            url = 'http://172.29.3.241/rest/api/2/issue/' + self.ISSUE_ID
            textmod = {'os_username':self.username, 'os_password':self.password,'fields':'summary,priority,assignee,updated,description,versions,issuetype，status'}
            textmod = urllib.urlencode(textmod)
            print(textmod)
            req = urllib2.Request(url='%s%s%s' % (url, '?', textmod))
            res = urllib2.urlopen(req)
            res = res.read()
        except Exception ,e:
            print e
        else :
            print res
            return res
        #print(res_dict[u'fields'])

if __name__ == '__main__':
    login = Login()
    login.print_jira()
    #login.get()
