#coding:utf-8
'''
Created on 2017-09-25

@author: lenovo
'''
import urllib
import re
class GetIMG:
    def __init__(self):
        self.url="https://www.yyfax.com/"
    def getHtml(self):
        page = urllib.urlopen(self.url)
        html = page.read()
        return html

    def getImg(self,html):
        reg = r'src="(.+?\.jpg)"'
        imgre = re.compile(reg)
        imglist = re.findall(imgre,html)
        x = 0
        for imgurl in imglist:
            newimgurl=self.url+imgurl
            print newimgurl
            urllib.urlretrieve(newimgurl,'%s.jpg' % x)
            x+=1

if __name__=='__main__':
    getIMG=GetIMG()
    html = getIMG.getHtml()
    print getIMG.getImg(html)