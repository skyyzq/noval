#coding:GBK
'''
#http://www.shuge.net/  �����,С˵���� ==> .txt
#http://www.shuge.net/html/3/3725/
'''
import re
import requests as REQ
from bs4 import BeautifulSoup as SP
#�����
url='http://www.shuge.net/html/3/3725/'
url=input("\n�������http://www.shuge.net/ \n\n������С˵��ַ:")
try:
    r = REQ.get(url)
except:
    print("��ַ����:"+url)
    input()
    quit()

encode='UTF-8'
r.encoding = encode
s = r.text
h = SP(s,'lxml')
novel=h.find(id = 'info')
fname =novel.find('h1').string.strip()
novel=h.find(id = 'intro')

���=novel.text.strip()
print(fname,���)

url=url[:url.find('html')]

urls=[]
li=h.find(id= 'list')
i=0
for aa in li.find_all('a'):
    #print(aa)
    i+=1
    if i<=12:continue
    urls.append((aa['href'],re.sub('^(\d+)','��\\1�� ',aa.string)))
#urls=set(urls)
#urls=list(urls)
#urls.sort()
f=open('txt\\'+fname+'.txt','wb')
f.write( bytes(fname+'\n\n'+���+'\n','utf-8'))

j=input("\n\t��ʼҳ����ҳ��%d��:"%len(urls))
jj=input("\n\t����ҳ����ҳ��%d��:"%len(urls))

j=int(j) if j.isdigit() else 0
jj=int(jj) if jj.isdigit() else len(urls)
print(j,jj)
jj+=1
url=url[:url.rfind('/b')]
i=0
for ur in urls:
    i+=1

    if i<j:
        #print(i,end='\t');
        continue
    if i==jj:break
    print(fname+":["+str(i)+"]"+"\t"+ur[1])    
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
    t=t.replace("����",'\n\t')
    t=t.replace('\r',"")
    t=t.replace('chaptererror();','')
    t=t.replace('ҼС˵���רQ�ף��סܣ��Q�����ة��ɩ����ܣϩ��ӡܣȣ��թ��ϡܣ��Q�é��ϨQ��','')
    t=t.replace('\t\t',"")
    t=t.replace('\t\t',"\t")
    t=re.sub('\t��\w+��.+','',t)
    t=t.replace('\n\n',"\n")
    f.write( bytes('\n'+ur[1]+t,'utf-8'))
f.close()

#the End
