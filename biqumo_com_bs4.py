#coding:GBK
'''
#��Ȥ��,С˵���� ==> .txt
#http://www.biquge.lu/book/27659/
http://www.biqumo.com/10_10779/
'''
import re
import requests as REQ
from bs4 import BeautifulSoup as SP
head={"User-Agent":'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 QIHU 360EE'}
#���С˵��
url='http://www.sikushu.org/book/134282/'
url=input("http://www.biqumo.com/\n\t��Ȥ��.com\n������С˵��ַ:")
try:
    r = REQ.get(url,headers=head)
except:
    print("��ַ����:"+url)
    input()
    quit()

encode='GBK'
r.encoding = encode
s = r.text
h = SP(s,'lxml')
novel=h.find(class_ = 'info')
fname =novel.find('h2').string.strip()
novel=h.find(class_ = 'intro')

���=novel.text.strip()
print(fname,���)
urls=[]
li=h.find(class_= 'listmain')
i=0
for aa in li.find_all('a'):
    #print(aa)
    i+=1
    if i<=0:continue
    urls.append((aa['href'],re.sub('^(\d+)','��\\1�� ',aa.string)))
#urls=set(urls)
#urls=list(urls)
#urls.sort()
f=open(fname+'.txt','wb')
f.write( bytes(fname+'\n\n'+���+'\n','utf-8'))
ii=len(urls)
j=input("\n\t��ʼҳ����ҳ��%d��:"%len(urls))
jj=input("\n\t����ҳ����ҳ��%d��:"%len(urls))

j=int(j) if j.isdigit() else 0
jj=int(jj) if jj.isdigit() else len(urls)
print(j,jj)
jj+=1
print(url)
if url[-1]=='/':url=url[:url.rfind('/')]
    
url=url[:url.rfind('/')]

#url='http://www.biqumo.com'
print(url)
i=0
for ur in urls:
    i+=1

    if i<j:
        #print(i,end='\t');
        continue
    if i==jj:break
    print(fname+"[%04d:%04d"%(ii,i)+"]:\t"+ur[1])    
    u = url+ur[0]
    try:
        r = REQ.get(u,headers=head)
    except:
        print("Try again...")
        print("...."+fname+":\t"+ur[1])
        r = REQ.get(u,headers=head)
    if not r.ok : r = REQ.get(u,headers=head)
    r.encoding = encode
    s = r.text
    txt=SP(s,'lxml')
    t=txt.find(id="content")
    if t==None: continue
    t=t.text
    t=t.replace('\xa0',' ') #�ո� \xa0
    t=t.replace("    ",'\n\t')
    t=t.replace('\r',"")
    t=t.replace('\t\n)','')
    t=t.replace('*','_')
    t=t.replace('���һ���ס��վ��ַ��www.biqumo.com����Ȥ���ֻ����Ķ���ַ��m.biqumo.com','')
    t=t.replace('\t\t',"")
    t=t.replace('\t\t',"\t")
    t=t.replace('\t\n','')
    t=t.replace('\t ','\t')
    t=t.replace('o','0')
    re.sub(r'\t��\w+��.+','\n',t)
    t=t.replace('\n\n',"\n")
    f.write( bytes('\n'+ur[1]+t,'utf-8'))
f.close()

#the End
