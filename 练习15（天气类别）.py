# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 10:37:50 2018
题目十五：未来三天 天气类天气对象
1.定义一个天气类Weather 静态的属性(temp,description,pre) 动态属性(msg打印当前天气属性)
2.创建3天的天气对象，并调用msg方法
@author: Administrator
"""

###########################15题
########方法一
class Weather:
    def __init__(self,temp,description,pressure):
        self.temp=temp
        self.description=description
        self.pressure=pressure
    def msg(self):
        print('温度是:{}\n天气是:{}\n气压是:{}\n'.format(self.temp,self.description,self.pressure))
a=Weather('34.77','多云','995.33')
b=Weather('33.12','晴，少云','995.69')
c=Weather('34.27','小雨','994.72')
a.msg()
b.msg()
c.msg()
#########方法二
import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=chongqing,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
class Weather:
    def __init__(self,dt_txt,temp,description,pressure):
        self.dt_txt=dt_txt
        self.temp=temp
        self.description=description
        self.pressure=pressure
    def msg(self):
        print('时间是:{}温度是:{}\n天气是:{}\n气压是:{}\n'.format(self.dt_txt,self.temp,self.description,self.pressure))
for i in (0,8,16):
    dt_txt=temp=data['list'][i]['dt_txt']
    temp=data['list'][i]['main']['temp']
    description=data['list'][i]['weather'][0]['description']
    pressure=data['list'][i]['main']['pressure']
    a=Weather(dt_txt,temp,description,pressure)
    a.msg()