# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 09:48:02 2018
爬取百度网页数据，用http:// 而不是其他
题目十一：爬取百度网页数据
1.爬取百度搜索标题
2.爬取标题下的描述
3.搜索的标题的网站
题目十二：使用re爬取天气信息
1.天气描述，天气温度，天气气压

@author: Administrator
"""
import urllib.request as r#导入联网工具包，命令为r
url='http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=matlab&rsv_pq=8387e25400058322&rsv_t=329fBr%2BXFJyxg3BZOKavAgccANZ5Co0DL%2FDxx5rhskustC7TPr0ZLzhhGrA&rqlang=cn&rsv_enter=0&rsv_sug3=9&rsv_sug1=9&rsv_sug7=101&inputT=11936&rsv_sug4=33935'
data=r.urlopen(url).read().decode('utf-8')
print(data)
import re
ls=re.compile('"title":"(.*?)"').findall(data)
print(ls)
ls1=re.compile('"title":"(.*?)"').findall(data)