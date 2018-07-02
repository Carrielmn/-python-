 #-*- coding: utf-8 -*-
"""
Created on Tue Jun 26 16:11:25 2018
题目十二：使用re爬取天气信息
1.天气描述，天气温度，天气气压

@author: Administrator
"""

import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
import re
lss=re.compile('"dt_txt":"(.*?)"').findall(data)
ls=re.compile('"description":"(.*?)"').findall(data)
ls1=re.compile('"temp":(.*?),').findall(data)
ls2=re.compile('"pressure":(.*?),').findall(data)
for i in range(0,37):
    print('时间：{}\t天气情况：{}\t天气温度:{}\t天气气压:{}'.format(lss[i],ls[i],ls1[i],ls2[i]))
    

