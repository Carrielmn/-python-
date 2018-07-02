# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 10:40:04 2018
题目十六：高考派2300数据统计
1.根据2300下载的两百多M文件，统计招生总人数
2.统计7各地域的人数各是多少
3.计算比例
@author: Administrator
"""
f=open('./西南地区.txt','a',encoding='utf-8')
f1=open('./贵州理科.txt','r')
d1=f1.read() 
f2=open('./贵州文科.txt','r')
d2=f2.read()  
f3=open('./四川理科.txt','r')
d3=f3.read()  
f4=open('./四川文科.txt','r') 
d4=f4.read() 
f5=open('./西藏文理科.txt','r')  
d5=f5.read()
f6=open('./云南理科.txt','r')  
d6=f6.read()
f7=open('./云南文科.txt','r')  
d7=f7.read()
f8=open('./重庆理科.txt','r')  
d8=f8.read()
f9=open('./重庆文科.txt','r')  
d9=f9.read()
f.write('{}{}{}{}{}{}{}{}{}\n'.format(d1,d2,d3,d4,d5,d6,d7,d8,d9))
f.close()



f=open('./全国招生计划表0206C正确.txt','r')
d=f.read()
import re
lss=re.compile('"plan":"(.*?)"').findall(d)
a=0
for i in range(len(lss)):
    a=a+int(lss[i])
print('全国招生人数是:{}'.format(a))



f1=open('./东北地区.txt','r')
d1=f1.read() 
f2=open('./华东地区.txt','r')
d2=f2.read()  
f3=open('./华中地区招生.txt','r')
d3=f3.read()  
f4=open('./华北地区.txt','r') 
d4=f4.read() 
f5=open('./华南地区.txt','r')  
d5=f5.read()
f6=open('./西北地区.txt','r')  
d6=f6.read()
f7=open('./西南地区.txt','r',encoding='utf-8')  
d7=f7.read()
import re
ls1=re.compile('"plan":"(.*?)"').findall(d1)
import re
ls2=re.compile('"plan":"(.*?)"').findall(d2)
import re
ls3=re.compile('"plan":"(.*?)"').findall(d3)
import re
ls4=re.compile('"plan":"(.*?)"').findall(d4)
import re
ls5=re.compile('"plan":"(.*?)"').findall(d5)
import re
ls6=re.compile('"plan":"(.*?)"').findall(d6)
import re
ls7=re.compile('"plan":"(.*?)"').findall(d7)
a=0
for i in range(len(ls1)):
    a=a+int(ls1[i])
print('东北地区招生人数是:{}'.format(a))
b=0
for i in range(len(ls2)):
    b=b+int(ls2[i])
print('华东地区招生人数是:{}'.format(b))
c=0
for i in range(len(ls3)):
    c=c+int(ls3[i])
print('华中地区招生人数是:{}'.format(c))
d=0
for i in range(len(ls4)):
    d=d+int(ls4[i])
print('华北地区招生人数是:{}'.format(d))
e=0
for i in range(len(ls5)):
    e=e+int(ls5[i])
print('华南地区招生人数是:{}'.format(e))
f=0
for i in range(len(ls6)):
    f=f+int(ls6[i])
print('西北地区招生人数是:{}'.format(f))
g=0
for i in range(len(ls7)):
    g=g+int(ls7[i])
print('西南地区招生人数是:{}'.format(g))











area={'黑龙江':'东北','吉林':'东北','辽宁':'东北','上海':'华东','江苏':'华东','浙江':'华东','安徽':'华东','福建':'华东','江西':'华东','山东':'华东','北京':'华北','天津':'华北','山西':'华北','河北':'华北','内蒙古':'华北','河南':'华中','湖南':'华中','湖北':'华中','广东':'华南','广西':'华南','海南':'华南','西藏':'西南','四川':'西南','贵州':'西南','云南':'西南','重庆':'西南','陕西':'西北','甘肃':'西北','青海':'西北','新疆':'西北','宁夏':'西北'}
areaplan={'东北':0,'华东':0,'华北':0,'华南':0,'华中':0,'西南':0,'西北':0}
ls=[]
import urllib.request as r#导入联网工具包，命令为r
url='file:///C:/Users/Administrator/全国招生计划表0206C正确.txt'
data=r.urlopen(url).read().decode('utf-8')
data=data.split('\n')
import json
for i in range(len(data)):
    x=json.loads(data[i])
    ls.append(x)
for j in range(len(ls)):
    if ls[j]['status']==0:
        continue
    lss=ls[j]['data']
    for school in lss:
        city=school['city']
        areaplan[area[city]]=areaplan[area[city]]+int(school['plan'])
a=areaplan['东北']+areaplan['华东']+areaplan['华北']+areaplan['华南']+areaplan['华中']+areaplan['西南']+areaplan['西北']
print('全国各地区招生总人数:{}\n东北地区招生人数:{}\n华东地区招生人数:{}\n华北地区招生人数:{}\n华南地区招生人数:{}\n华中地区招生人数:{}\n西南地区招生人数:{}\n西北地区招生人数:{}'.format(a,areaplan['东北'],areaplan['华东'],areaplan['华北'],areaplan['华南'],areaplan['华中'],areaplan['西南'],areaplan['西北']))