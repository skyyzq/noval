#coding:GBK
'''
#��ѧ��,С˵���� ==> .txt
#https://www.wenxuemi.com/files/article/html/23/23636/
#https://www.wenxuemi.com/files/article/html/23/23636/11370428.html
'''
import re
import requests as REQ
from bs4 import BeautifulSoup as SP
print("\n��ѧ��:  https://www.wenxuemi.com \n")
url='http://www.sikushu.org/book/134282/'
url=input("������С˵��ַ:")
try:
    r = REQ.get(url)
except:
    print("��ַ����:"+url)
    input()
    quit()

encode='GBK'
r.encoding = encode
s = r.text
h = SP(s,'lxml')
novel=h.find(id = 'info')
fname =novel.find('h1').string.strip()
novel=h.find(id = 'intro')

���=novel.text.strip()
print(fname,���)
urls=[]
li=h.find(id= 'list')
i=0
for aa in li.find_all('a'):
    #print(aa)
    #i+=1
    #if i<10:continue
    urls.append((aa['href'],re.sub('^(\d+)','��\\1�� ',aa.string)))
#urls=set(urls)
#urls=list(urls)
#urls.sort()
f=open(fname+'.txt','wb')
f.write( bytes(fname+'\n\n'+���+'\n','utf-8'))

j=input("\n\t��ʼҳ����ҳ��%d��:"%len(urls))
jj=input("\n\t����ҳ����ҳ��%d��:"%len(urls))

j=int(j) if j.isdigit() else 0
jj=int(jj) if jj.isdigit() else len(urls)
print(j,jj)
jj+=1
url=url[:url.rfind('/files')]
i=0
for ur in urls:
    i+=1

    if i<j:
        #print(i,end='\t');
        continue
    if i==jj:break
    print(fname+":\t"+re.sub('^(��.+��)(.+)',r'\1 \2',ur[1]))    
    u = url+ur[0]
    try:
        r = REQ.get(u)
    except:
        print("Try again...")
        print("...."+fname+":\t"+ur[1])
        r = REQ.get(u)
    if not r.ok : r = REQ.get(u)
    r.encoding = encode
    s = r.text
    txt=SP(s,'lxml')
    t=txt.find(id="content")
    if t==None: continue
    t=t.text
    t=t.replace('\xa0',' ') #�ո� \xa0
    t=t.replace("    ",'\n\t')
    t=t.replace('\r',"")
    t=t.replace('(�Ŀ��� www.sikushu.org)','')
    t=t.replace('(�Ŀ���С˵�� www.sikushu.org)chaptererror()','\n')
    t=t.replace('(�Ŀ���С˵�� www.sikushu.org)','')
    t=t.replace('\t\t',"")
    t=t.replace('\t\t',"\t")
    re.sub(r'\t��\w+��.+','\n',t)
    t=t.replace('\n\n',"\n")
    f.write( bytes('\n\n'+re.sub('^(��.+��)(.+)',r'\1 \2',ur[1])+'\n'+t,'utf-8'))
f.close()

#the End
