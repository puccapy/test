#coding:utf-8
'''
Created on 2017-09-25

@author: lenovo
'''
import urllib
import re
class GetIMG:
    def __init__(self):
        self.url="https://www.ricequant.com/community/topic/2855/"
    def getHtml(self):
        page = urllib.urlopen(self.url)
        html = page.read()
        return html

    def getImg(self,html):
        reg = r'src="(.+?\.jpg|.+?\.gif|.+?\.png)"'
        imgre = re.compile(reg)
        imglist = re.findall(imgre,html)
        x = 0
        for imgurl in imglist:
            if imgurl.find('http')<0:
                newimgurl=self.url+imgurl
            else:              
                newimgurl=imgurl
            print newimgurl
            if newimgurl.find('jpg')>0:
                urllib.urlretrieve(newimgurl,'%s.jpg' % x)
            elif newimgurl.find('gif')>0:
                urllib.urlretrieve(newimgurl,'%s.gif' % x)
            else:
                urllib.urlretrieve(newimgurl,'%s.png' % x)
            x+=1

if __name__=='__main__':
    getIMG=GetIMG()
    html = getIMG.getHtml()
    print getIMG.getImg(html)