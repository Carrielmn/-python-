# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 10:48:22 2018
全球未来5天气预报
2018-06-21 03:00:00    按照3小时一次预报
2018-06-21 06:00:00
2018-06-21 09:00:00------当前时间
2018-06-21 12:00:00
2018-06-25 21:00:00

第四题：求出未来5天天气
1.打印每天的6:00,12:00,18:00的天气(城市,温度，情况，气压，最高温度，最低温度)
2.同上写出[英文版的]
3.根据天气的情况，给出建议：例如，今天下雨，提示带伞。今天温度高，穿衬衫...三个件以上
4.根据温度打印出问题折线图
    28——————————————————————————————
    30——————————————————————————————————
    10——————————————————
5.打印出其他10个城市的天气，计算出天气排名，按着大到小的顺序。



@author: Administrator
"""
import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=chongqing,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
#data字典-》list列表-》index 0 字典-》main字典-》temp变量
#2018-6-21
print('在{}'.format(data['list'][0]['dt_txt']),'{}'.format(data['city']['name']),'温度是{}'.format(data['list'][0]['main']['temp']),
 '天气情况是{}'.format(data['list'][0]['weather'][0]['description']),'天气气压是{}'.format(data['list'][0]['main']['pressure']),
 '最高温度是{}'.format(data['list'][0]['main']['temp_max']),'最低温度是{}'.format(data['list'][0]['main']['temp_min']))
print('在{}'.format(data['list'][2]['dt_txt']),'{}'.format(data['city']['name']),'温度是{}'.format(data['list'][2]['main']['temp']),
 '天气情况是{}'.format(data['list'][2]['weather'][0]['description']),'天气气压是{}'.format(data['list'][2]['main']['pressure']),
 '最高温度是{}'.format(data['list'][2]['main']['temp_max']),'最低温度是{}'.format(data['list'][2]['main']['temp_min']))
print('在{}'.format(data['list'][4]['dt_txt']),'{}'.format(data['city']['name']),'温度是{}'.format(data['list'][4]['main']['temp']),
 '天气情况是{}'.format(data['list'][4]['weather'][0]['description']),'天气气压是{}'.format(data['list'][4]['main']['pressure']),
 '最高温度是{}'.format(data['list'][4]['main']['temp_max']),'最低温度是{}'.format(data['list'][4]['main']['temp_min']))
print('At {}'.format(data['list'][0]['dt_txt']),'{}'.format(data['city']['name']),'Temperature is {}'.format(data['list'][0]['main']['temp']),
 'Weather condition is {}'.format(data['list'][0]['weather'][0]['main']),'Weather perssure is {}'.format(data['list'][0]['main']['pressure']),
 'Maximum temperature is {}'.format(data['list'][0]['main']['temp_max']),'Minimum temperature is {}'.format(data['list'][0]['main']['temp_min']))
print('At {}'.format(data['list'][2]['dt_txt']),'{}'.format(data['city']['name']),'Temperature is {}'.format(data['list'][2]['main']['temp']),
 'Weather condition is {}'.format(data['list'][2]['weather'][0]['main']),'Weather perssure is {}'.format(data['list'][2]['main']['pressure']),
 'Maximum temperature is {}'.format(data['list'][2]['main']['temp_max']),'Minimum temperature is {}'.format(data['list'][2]['main']['temp_min']))
print('At {}'.format(data['list'][4]['dt_txt']),'{}'.format(data['city']['name']),'Temperature is {}'.format(data['list'][4]['main']['temp']),
 'Weather condition is {}'.format(data['list'][4]['weather'][0]['main']),'Weather perssure is {}'.format(data['list'][4]['main']['pressure']),
 'Maximum temperature is {}'.format(data['list'][4]['main']['temp_max']),'Minimum temperature is {}'.format(data['list'][4]['main']['temp_min']))
print('今天是{}'.format(data['list'][0]['weather'][0]['description']),'不适宜运动',
      '今天是{}'.format(data['list'][0]['weather'][0]['description']),'出门记得带伞',
     '今天最高温度是{}'.format(data['list'][0]['main']['temp_max']),'注意添加衣物' )
#2018-6-22
print('在{}'.format(data['list'][8]['dt_txt']),'{}'.format(data['city']['name']),'温度是{}'.format(data['list'][8]['main']['temp']),
 '天气情况是{}'.format(data['list'][8]['weather'][0]['description']),'天气气压是{}'.format(data['list'][8]['main']['pressure']),
 '最高温度是{}'.format(data['list'][8]['main']['temp_max']),'最低温度是{}'.format(data['list'][8]['main']['temp_min']))
print('在{}'.format(data['list'][10]['dt_txt']),'{}'.format(data['city']['name']),'温度是{}'.format(data['list'][10]['main']['temp']),
 '天气情况是{}'.format(data['list'][10]['weather'][0]['description']),'天气气压是{}'.format(data['list'][10]['main']['pressure']),
 '最高温度是{}'.format(data['list'][10]['main']['temp_max']),'最低温度是{}'.format(data['list'][10]['main']['temp_min']))
print('在{}'.format(data['list'][12]['dt_txt']),'{}'.format(data['city']['name']),'温度是{}'.format(data['list'][12]['main']['temp']),
 '天气情况是{}'.format(data['list'][12]['weather'][0]['description']),'天气气压是{}'.format(data['list'][12]['main']['pressure']),
 '最高温度是{}'.format(data['list'][12]['main']['temp_max']),'最低温度是{}'.format(data['list'][12]['main']['temp_min']))
print('At {}'.format(data['list'][8]['dt_txt']),'{}'.format(data['city']['name']),'Temperature is {}'.format(data['list'][8]['main']['temp']),
 'Weather condition is {}'.format(data['list'][8]['weather'][0]['main']),'Weather perssure is {}'.format(data['list'][8]['main']['pressure']),
 'Maximum temperature is {}'.format(data['list'][8]['main']['temp_max']),'Minimum temperature is {}'.format(data['list'][8]['main']['temp_min']))
print('At {}'.format(data['list'][10]['dt_txt']),'{}'.format(data['city']['name']),'Temperature is {}'.format(data['list'][10]['main']['temp']),
 'Weather condition is {}'.format(data['list'][10]['weather'][0]['main']),'Weather perssure is {}'.format(data['list'][10]['main']['pressure']),
 'Maximum temperature is {}'.format(data['list'][10]['main']['temp_max']),'Minimum temperature is {}'.format(data['list'][10]['main']['temp_min']))
print('At {}'.format(data['list'][12]['dt_txt']),'{}'.format(data['city']['name']),'Temperature is {}'.format(data['list'][12]['main']['temp']),
 'Weather condition is {}'.format(data['list'][12]['weather'][0]['main']),'Weather perssure is {}'.format(data['list'][12]['main']['pressure']),
 'Maximum temperature is {}'.format(data['list'][12]['main']['temp_max']),'Minimum temperature is {}'.format(data['list'][12]['main']['temp_min']))
print('今天是{}'.format(data['list'][8]['weather'][0]['description']),'出门带伞',
      '风速是{}'.format(data['list'][8]['wind']['speed']),'注意关好门窗',
     '今天最高温度是{}'.format(data['list'][8]['main']['temp_max']),'注意添加衣物' )
#2018-6-23
print('在{}'.format(data['list'][16]['dt_txt']),'{}'.format(data['city']['name']),'温度是{}'.format(data['list'][16]['main']['temp']),
 '天气情况是{}'.format(data['list'][16]['weather'][0]['description']),'天气气压是{}'.format(data['list'][16]['main']['pressure']),
 '最高温度是{}'.format(data['list'][16]['main']['temp_max']),'最低温度是{}'.format(data['list'][16]['main']['temp_min']))
print('在{}'.format(data['list'][18]['dt_txt']),'{}'.format(data['city']['name']),'温度是{}'.format(data['list'][18]['main']['temp']),
 '天气情况是{}'.format(data['list'][18]['weather'][0]['description']),'天气气压是{}'.format(data['list'][18]['main']['pressure']),
 '最高温度是{}'.format(data['list'][18]['main']['temp_max']),'最低温度是{}'.format(data['list'][18]['main']['temp_min']))
print('在{}'.format(data['list'][20]['dt_txt']),'{}'.format(data['city']['name']),'温度是{}'.format(data['list'][20]['main']['temp']),
 '天气情况是{}'.format(data['list'][20]['weather'][0]['description']),'天气气压是{}'.format(data['list'][20]['main']['pressure']),
 '最高温度是{}'.format(data['list'][20]['main']['temp_max']),'最低温度是{}'.format(data['list'][20]['main']['temp_min']))
print('At {}'.format(data['list'][16]['dt_txt']),'{}'.format(data['city']['name']),'Temperature is {}'.format(data['list'][16]['main']['temp']),
 'Weather condition is {}'.format(data['list'][16]['weather'][0]['main']),'Weather perssure is {}'.format(data['list'][16]['main']['pressure']),
 'Maximum temperature is {}'.format(data['list'][16]['main']['temp_max']),'Minimum temperature is {}'.format(data['list'][16]['main']['temp_min']))
print('At {}'.format(data['list'][18]['dt_txt']),'{}'.format(data['city']['name']),'Temperature is {}'.format(data['list'][18]['main']['temp']),
 'Weather condition is {}'.format(data['list'][18]['weather'][0]['main']),'Weather perssure is {}'.format(data['list'][18]['main']['pressure']),
 'Maximum temperature is {}'.format(data['list'][18]['main']['temp_max']),'Minimum temperature is {}'.format(data['list'][18]['main']['temp_min']))
print('At {}'.format(data['list'][20]['dt_txt']),'{}'.format(data['city']['name']),'Temperature is {}'.format(data['list'][20]['main']['temp']),
 'Weather condition is {}'.format(data['list'][20]['weather'][0]['main']),'Weather perssure is {}'.format(data['list'][20]['main']['pressure']),
 'Maximum temperature is {}'.format(data['list'][20]['main']['temp_max']),'Minimum temperature is {}'.format(data['list'][20]['main']['temp_min']))
print('今天是{}'.format(data['list'][18]['weather'][0]['description']),'适宜运动',
      '风速是{}'.format(data['list'][8]['wind']['speed']),'适宜散步',
     '今天最高温度是{}'.format(data['list'][18]['main']['temp_max']),'注意添加衣物' )
#2018-6-24
print('在{}'.format(data['list'][24]['dt_txt']),'{}'.format(data['city']['name']),'温度是{}'.format(data['list'][24]['main']['temp']),
 '天气情况是{}'.format(data['list'][24]['weather'][0]['description']),'天气气压是{}'.format(data['list'][24]['main']['pressure']),
 '最高温度是{}'.format(data['list'][24]['main']['temp_max']),'最低温度是{}'.format(data['list'][24]['main']['temp_min']))
print('在{}'.format(data['list'][26]['dt_txt']),'{}'.format(data['city']['name']),'温度是{}'.format(data['list'][26]['main']['temp']),
 '天气情况是{}'.format(data['list'][26]['weather'][0]['description']),'天气气压是{}'.format(data['list'][26]['main']['pressure']),
 '最高温度是{}'.format(data['list'][26]['main']['temp_max']),'最低温度是{}'.format(data['list'][26]['main']['temp_min']))
print('在{}'.format(data['list'][28]['dt_txt']),'{}'.format(data['city']['name']),'温度是{}'.format(data['list'][28]['main']['temp']),
 '天气情况是{}'.format(data['list'][28]['weather'][0]['description']),'天气气压是{}'.format(data['list'][28]['main']['pressure']),
 '最高温度是{}'.format(data['list'][28]['main']['temp_max']),'最低温度是{}'.format(data['list'][28]['main']['temp_min']))
print('At {}'.format(data['list'][24]['dt_txt']),'{}'.format(data['city']['name']),'Temperature is {}'.format(data['list'][24]['main']['temp']),
 'Weather condition is {}'.format(data['list'][24]['weather'][0]['main']),'Weather perssure is {}'.format(data['list'][24]['main']['pressure']),
 'Maximum temperature is {}'.format(data['list'][24]['main']['temp_max']),'Minimum temperature is {}'.format(data['list'][24]['main']['temp_min']))
print('At {}'.format(data['list'][26]['dt_txt']),'{}'.format(data['city']['name']),'Temperature is {}'.format(data['list'][26]['main']['temp']),
 'Weather condition is {}'.format(data['list'][26]['weather'][0]['main']),'Weather perssure is {}'.format(data['list'][26]['main']['pressure']),
 'Maximum temperature is {}'.format(data['list'][26]['main']['temp_max']),'Minimum temperature is {}'.format(data['list'][26]['main']['temp_min']))
print('At {}'.format(data['list'][28]['dt_txt']),'{}'.format(data['city']['name']),'Temperature is {}'.format(data['list'][28]['main']['temp']),
 'Weather condition is {}'.format(data['list'][28]['weather'][0]['main']),'Weather perssure is {}'.format(data['list'][28]['main']['pressure']),
 'Maximum temperature is {}'.format(data['list'][28]['main']['temp_max']),'Minimum temperature is {}'.format(data['list'][28]['main']['temp_min']))
print('今天是{}'.format(data['list'][26]['weather'][0]['description']),'适宜运动',
      '今天是{}'.format(data['list'][26]['weather'][0]['description']),'注意防晒',
     '今天最高温度是{}'.format(data['list'][26]['main']['temp_max']),'建议穿T恤' )
#2018-6-25
print('在{}'.format(data['list'][32]['dt_txt']),'{}'.format(data['city']['name']),'温度是{}'.format(data['list'][32]['main']['temp']),
 '天气情况是{}'.format(data['list'][32]['weather'][0]['description']),'天气气压是{}'.format(data['list'][32]['main']['pressure']),
 '最高温度是{}'.format(data['list'][32]['main']['temp_max']),'最低温度是{}'.format(data['list'][32]['main']['temp_min']))
print('在{}'.format(data['list'][34]['dt_txt']),'{}'.format(data['city']['name']),'温度是{}'.format(data['list'][34]['main']['temp']),
 '天气情况是{}'.format(data['list'][34]['weather'][0]['description']),'天气气压是{}'.format(data['list'][34]['main']['pressure']),
 '最高温度是{}'.format(data['list'][34]['main']['temp_max']),'最低温度是{}'.format(data['list'][34]['main']['temp_min']))
print('在{}'.format(data['list'][36]['dt_txt']),'{}'.format(data['city']['name']),'温度是{}'.format(data['list'][36]['main']['temp']),
 '天气情况是{}'.format(data['list'][36]['weather'][0]['description']),'天气气压是{}'.format(data['list'][36]['main']['pressure']),
 '最高温度是{}'.format(data['list'][36]['main']['temp_max']),'最低温度是{}'.format(data['list'][36]['main']['temp_min']))
print('At {}'.format(data['list'][32]['dt_txt']),'{}'.format(data['city']['name']),'Temperature is {}'.format(data['list'][32]['main']['temp']),
 'Weather condition is {}'.format(data['list'][32]['weather'][0]['main']),'Weather perssure is {}'.format(data['list'][32]['main']['pressure']),
 'Maximum temperature is {}'.format(data['list'][32]['main']['temp_max']),'Minimum temperature is {}'.format(data['list'][32]['main']['temp_min']))
print('At {}'.format(data['list'][34]['dt_txt']),'{}'.format(data['city']['name']),'Temperature is {}'.format(data['list'][34]['main']['temp']),
 'Weather condition is {}'.format(data['list'][34]['weather'][0]['main']),'Weather perssure is {}'.format(data['list'][34]['main']['pressure']),
 'Maximum temperature is {}'.format(data['list'][34]['main']['temp_max']),'Minimum temperature is {}'.format(data['list'][34]['main']['temp_min']))
print('At {}'.format(data['list'][36]['dt_txt']),'{}'.format(data['city']['name']),'Temperature is {}'.format(data['list'][36]['main']['temp']),
 'Weather condition is {}'.format(data['list'][36]['weather'][0]['main']),'Weather perssure is {}'.format(data['list'][36]['main']['pressure']),
 'Maximum temperature is {}'.format(data['list'][36]['main']['temp_max']),'Minimum temperature is {}'.format(data['list'][36]['main']['temp_min']))
print('今天是{}'.format(data['list'][34]['weather'][0]['description']),'适宜运动',
      '今天是{}'.format(data['list'][34]['weather'][0]['description']),'注意保湿，多喝水',
     '今天最高温度是{}'.format(data['list'][34]['main']['temp_max']),'建议穿T恤' )



day1=data['list'][0]['main']['temp']
day2=data['list'][8]['main']['temp']
day3=data['list'][16]['main']['temp']
day4=data['list'][24]['main']['temp']
day5=data['list'][32]['main']['temp']
y1=data['list'][0]['dt_txt']
y2=data['list'][8]['dt_txt']
y3=data['list'][16]['dt_txt']
y4=data['list'][24]['dt_txt']
y5=data['list'][32]['dt_txt']
print(y1,int(day1)*'-',day1)
print(y2,int(day2)*'-',day2)
print(y3,int(day3)*'-',day3)
print(y4,int(day4)*'-',day4)
print(y5,int(day5)*'-',day5)




import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=chongqing,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)

chongqing=data['list'][0]['main']['temp']
chongqing

import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=beijing,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
beijing=data['list'][0]['main']['temp']

import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=chengdu,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
chengdu=data['list'][0]['main']['temp']

import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=liaoyang,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
liaoyang=data['list'][0]['main']['temp']

import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=tianjin,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
tianjin=data['list'][0]['main']['temp']

import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=shanghai,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
shanghai=data['list'][0]['main']['temp']

import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=jilin,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
jilin=data['list'][0]['main']['temp']


import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=dalian,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
dalian=data['list'][0]['main']['temp']

import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=xiamen,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
xiamen=data['list'][0]['main']['temp']

import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=nanjing,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
nanjing=data['list'][0]['main']['temp']


import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=lijiang,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
lijiang=data['list'][0]['main']['temp']
print(chongqing,chengdu,liaoyang,tianjin,shanghai,jilin,dalian,xiamen,nanjing,lijiang)




ls=[]
ls.append(chongqing)
ls.append(chengdu)
ls.append(liaoyang)
ls.append(tianjin)
ls.append(shanghai)
ls.append(jilin)
ls.append(dalian)
ls.append(xiamen)
ls.append(nanjing)
ls.append(lijiang)

print(ls)
ls=sorted(ls)
print(ls)

lss=reversed(ls)
print(lss)
for i in lss:
    print(i)
























def msg(a,b,c,d):
    print('姓名：{}'.format(a))
    print('性别：{}'.format(b))
    print('职业：{}'.format(c))
    print('爱好：{}'.format(d))
msg('石林','男','爸爸们的儿子','吃屎')






