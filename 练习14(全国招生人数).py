# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 09:08:13 2018

@author: Administrator
"""
import urllib.request as r
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
data='id=2948&type=2&city=50&state=1'.encode()
req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
d=r.urlopen(req).read().decode('utf-8','ignore')

f=open('./all_school2.txt','r',encoding='utf-8')
data=f.read()
print(data)
import re
ls1=re.compile('http://www.gaokaopai.com/daxue-jianjie-(.*?).html',re.S).findall(data)
print(ls1)
    
    
    
import urllib.request as r
url='http://www.gaokaopai.com/daxue-0-0-0-0-0-0-0.html'
data='id=2948&type=2&city=50&state=1'.encode()
req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
d=r.urlopen(req).read().decode('utf-8','ignore')  
ls2=re.compile('<span><a href="http://www.gaokaopai.com/daxue-(.*?)-0-0-0-0-0-0.html">',re.S).findall(d)
ls3=re.compile('<span><a href="http://www.gaokaopai.com/daxue-..-0-0-0-0-0-0.html">(.*?)</a>',re.S).findall(d)
for i in range(len(ls3)):
    print('城市是：{}\t编号是：{}'.format(ls3[i],ls2[i]))
    
    


f=open('./all_school(1).txt','r',encoding='utf-8')
data=f.read()
import re
ls1=re.compile('http://www.gaokaopai.com/daxue-jianjie-(.*?).html',re.S).findall(data)
ls=[]
import urllib.request as r
ff=open('./a.txt','w',encoding='utf-8')  
for i in range(2300):
    url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
    data='id={}&type=1&city=43&state=1'.format(ls1[i]).encode()
    req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
    d=r.urlopen(req).read().decode('utf-8','ignore')
    ls.append(d)
    if ls[i].startswith('{'):
        print('ok{}'.format(i))
    else:
        url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
        data='id={}&type=1&city=43&state=1'.format(ls1[i]).encode()
        req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
        d=r.urlopen(req).read().decode('utf-8','ignore')
        ls[i]=d    
    ff.write(ls[i]+'\n')
ff.close()


f=open('./湖南文科1.txt','r',encoding='utf-8')  
data=f.read()
import re
lss=re.compile('"plan":"(.*?)"').findall(data)
a=0
for i in range(len(lss)):
    a=a+int(lss[i])
print('湖南文科人数是:{}'.format(a))
ff=open('./湖南理科1.txt','r',encoding='utf-8')  
dataa=ff.read()
import re
lss1=re.compile('"plan":"(.*?)"').findall(dataa)
b=0
for i in range(len(lss1)):
    b=b+int(lss1[i])4
print('湖南理科人数是:{}'.format(b))


fff=open('./河南文科.txt','r',encoding='utf-8')  
dataaa=fff.read()
import re
lss2=re.compile('"plan":"(.*?)"').findall(dataaa)
c=0
for i in range(len(lss2)):
    c=c+int(lss2[i])
print('河南文科人数是:{}'.format(c))

ffff=open('./河南理科.txt','r',encoding='utf-8')  
dataaaa=ffff.read()
import re
lss3=re.compile('"plan":"(.*?)"').findall(dataaaa)
d=0
for i in range(len(lss3)):
    d=d+int(lss3[i])
print('河南理科人数是:{}'.format(d))

fffff=open('./湖北文科.txt','r',encoding='utf-8')  
dataaaaa=fffff.read()
import re
lss4=re.compile('"plan":"(.*?)"').findall(dataaaaa)
e=0
for i in range(len(lss4)):
    e=e+int(lss4[i])
print('湖北文科人数是:{}'.format(e))

ffffff=open('./湖北理科.txt','r',encoding='utf-8')  
dataaaaaa=ffffff.read()
import re
lss5=re.compile('"plan":"(.*?)"').findall(dataaaaaa)
g=0
for i in range(len(lss5)):
    g=g+int(lss5[i])
print('湖北理科人数是:{}'.format(g))

ls=[a,b,c,d,e,g]
h=0
for i in range(len(ls)):
    h=h+int(ls[i])
print('华中地区招生人数是:{}'.format(h))

f=open('./fdg.txt','a',encoding='utf-8')
f1=open('./湖南文科1.txt','r',encoding='utf-8')
d1=f1.read() 
f2=open('./湖南理科1.txt','r',encoding='utf-8')
d2=f2.read()  
f3=open('./河南文科.txt','r',encoding='utf-8')
d3=f3.read()  
f4=open('./河南理科.txt','r',encoding='utf-8') 
d4=f4.read() 
f5=open('./湖北文科.txt','r',encoding='utf-8')  
d5=f5.read()
f6=open('./湖北理科.txt','r',encoding='utf-8')  
d6=f6.read()
f.write('{}{}{}{}{}{}\n'.format(d1,d2,d3,d4,d5,d6))
f.close()