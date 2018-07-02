# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 14:39:54 2018
函数：
变量(生命周期)
全局变量，局部变量(函数内)
练习五:实现练习四，
1.使用函数写出来。定义函数，输出每一天6:00,12:00,18:00的天气信息
2.打印折线图,使用字符串的*号操作
10----------
5-----
@author: Administrator
"""
import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=chongqing,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
print('在{}'.format(data['list'][0]['dt_txt']),'{}'.format(data['city']['name']),'温度是{}'.format(data['list'][0]['main']['temp']),
 '天气情况是{}'.format(data['list'][0]['weather'][0]['description']),'天气气压是{}'.format(data['list'][0]['main']['pressure']),
 '最高温度是{}'.format(data['list'][0]['main']['temp_max']),'最低温度是{}'.format(data['list'][0]['main']['temp_min']))


def msg(x):
    a=data['list'][x]['dt_txt']
    b=data['list'][x]['main']['temp']
    c=data['list'][x]['main']['temp_max']
    d=data['list'][x]['main']['temp_min']
    e=data['list'][x]['weather'][0]['description']
    f=data['list'][x]['main']['pressure']
    print('今天是:{},温度是：{},最高温度是：{},最低温度是：{},天气情况是：{},天气气压是：{}'.format(a,b,c,d,e,f))
    
msg(0)
msg(2)
msg(6)
msg(8)
msg(10)
msg(14)
msg(16)
msg(18)
msg(22)
msg(24)
msg(26)
msg(30)
msg(32)
msg(34)
def msg(x):
    a=data['list'][x]['dt_txt']
    b=data['list'][x]['main']['temp']
    print(a,int(b)*'-',b)
msg(0)
msg(2)
msg(6)
msg(8)
msg(10)
msg(14)
msg(16)
msg(18)
msg(22)
msg(24)
msg(26)
msg(30)
msg(32)
msg(34)



"""
def 函数名称(变量,...):
    指令的集合
"""
