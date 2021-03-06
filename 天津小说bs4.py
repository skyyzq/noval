#! /usr/bin/evn python3
# -*- coding: GBK -*-
'''
#天津小说网,小说下载 ==> .txt
'''
import re
import requests as REQ
from bs4 import BeautifulSoup as SP
#天津小说网
url='https://www.tmetb.net/220/220865/'
url=input("\n\t天津小说网\n\n请输入小说网址:")
try:
    r = REQ.get(url)
except:
    print("网址错误:"+url)
    input()
    quit()

r.encoding = "GBK"
s = r.text
h = SP(s,'lxml')
novel=h.find(class_ = 'commend')
fname =novel.find('h1').string
commend =novel.find('ul')
简介=commend.contents[0]
print(fname,简介)
urls=[]
li=h.find(class_ = 'box-item')
for aa in li.find_all('a'):
    #print(aa)
    urls.append((aa['href'],re.sub('^(\d+)','第\\1章 ',aa.string)))
f=open('txt\\'+fname+'.txt','wb')
f.write( bytes(fname+'\n\n'+简介+'\n','utf-8'))

j=input("\n\t起始页（总页数%d）:"%len(urls))
jj=input("\n\t结束页（总页数%d）:"%len(urls))

j=int(j) if j.isdigit() else 0
jj=int(jj) if jj.isdigit() else len(urls)
print(j,jj)
jj+=1
i=0
ii=len(urls)
for ur in urls:
    i+=1

    if i<j:
        #print(i,end='\t');
        continue
    if i==jj:break
    print("%s[%s-%s]:\t%s"%(fname,ii,i,ur[1]))
    u = url+ur[0]
    try:
        r = REQ.get(u)
    except:
        print("Try again...")
        print("....%s[%s]:\t%s"%(fname,i,ur[1]))
        r = REQ.get(u)
    if not r.ok : r = REQ.get(u)
    r.encoding = 'GBK'
    s = r.text
    txt=SP(s,'lxml')
    t=txt.find(id='text_area')
    if t==None: continue
    t=t.text
    t=t.replace('\xa0',' ') #空格 \xa0
    t=t.replace("    ",'\n\t')
    t=t.replace('(天津小说网https://www.tmetb.net)','')
    t=t.replace('恋上你看书网 630bookla ，最快更新大明厂督最新章节！','')
    t=t.replace('\r',"")
    t=t.replace('\t\t',"")
    t=t.replace('\t\t',"\t")
    t=t.replace('\n\n',"\n")
    f.write( bytes('\n'+ur[1]+t,'utf-8'))
f.close()

#the End
