# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 09:19:32 2018
《当》动力火车
当山峰没有棱角的时候
当河水不再流
当时间停住日夜不分
当天地万物化为虚有
...
当太阳不再上升的时候
当地球不再转动
当春夏秋冬不再变换
当花草树木全部凋残

练习七:全球天气未来3天
1.使用多选其一，完成天气的提醒
2.一定要多ci使用到for循环,偶尔用一次while循环
3.初步学会使用debug，知道里面的设置断点，下一步执行，下一个断点执行。
4.《闪屏的制作》进入我们天气程序的时候，有一个温馨图形的提示。使用循环实现，
  要知道是什么意思，照抄网上代码不行。

    

@author: Administrator
"""


import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=chongqing,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
#第一问
for i in range(0,37):
    description=data['list'][i]['weather'][0]['description']
    day=data['list'][i]['dt_txt']
    if description=='小雨':
       print(day,'出门记得带伞')
    elif description=='多云':
        print(day,'天气较好，适当运动')
    elif description=='中雨':
        print(day,'适当添加衣物，不建议出行')
    elif description=='阴，多云':
        print(day,'注意适当添加衣物')
    else:
        print(day,'适宜运动，补充喝水')
#第二问
for i in range(0,37):
    description=data['list'][i]['weather'][0]['description']
    day=data['list'][i]['dt_txt']
    if description=='小雨':
       print(day,'出门记得带伞')
    elif description=='多云':
        print(day,'天气较好，适当运动')
    elif description=='中雨':
        print(day,'适当添加衣物，不建议出行')
    elif description=='阴，多云':
        print(day,'注意适当添加衣物')
    else:
        print(day,'适宜运动，补充喝水')
    for i in ['实时天气提示']:
        print(i)
        
        
#第四问
ls=['欢','迎','来','到','实','时','天','气','预','报']
for i in ls:
    if i=='欢':
        print('*'*10,i,'*'*10)
    elif i=='迎':
        print('@','*'*9,i,'*'*9,'@')
    elif i=='来':
        print('@'*2,'*'*8,i,'*'*8,'@'*2)
    elif i=='到':
        print('@'*3,'*'*7,i,'*'*7,'@'*3)
    elif i=='实':
        print('@'*4,'*'*6,i,'*'*6,'@'*4)
    elif i=='时':
        print('@'*5,'*'*5,i,'*'*5,'@'*5)
    elif i=='天':
        print('@'*6,'*'*4,i,'*'*4,'@'*6)
    elif i=='气':
        print('@'*7,'*'*3,i,'*'*3,'@'*7)
    elif i=='预':
        print('@'*8,'*'*2,i,'*'*2,'@'*8)
    elif i=='报':
        print('@'*9,'*',i,'*','@'*9)