# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 08:57:33 2018
12306.cn火车票余票查询
中国铁路火车票上的车次，有以C（读作“城”）打头的车次、
以D（读作“动车”）打头的车次、
以G（读作“高”）打头的车次、-------------------------------OK
以N（读作“内”）打头的车次、
以Z（读作“直”）打头的车次、
以T（读作“特”）打头的车次、
以K（读作“快”）打头的车次、
以L（读作“临”）打头的车次、
以Y（读作“游”）打头的车次和不带字母打头的车次等十余种。
题目九：余票查询组项目
1.查询某种火车的余票，动车，高铁，直达，特快....
2.组长将各组员功能汇总

@author: Administrator
"""
import urllib.request as r#导入联网工具包，命令为r
url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-06-26&leftTicketDTO.from_station=CQW&leftTicketDTO.to_station=BJP&purpose_codes=ADULT'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
data=data['data']['result']


p='  '
title='日期{}车次{}出发站/到达站{}出发时间/到达时间{}历时{}商务座/特等座{}一等座{}二等座{}高级软卧{}软卧{}动卧{}硬卧{}软座{}硬座{}无座{}其他{}备注'.format(p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p)
title=title.split(p)
for j in title:
    print(j.center(11),end='')
len([p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p])
print()  
for i in range(0,9):
    s=data[i]
    ls=s.split('|')
    ls1=[ls[13],ls[3],[ls[6],ls[7]],[ls[8],ls[9]],ls[10],ls[32],ls[31],ls[30],'--',ls[23],'--',ls[28],'--',ls[29],ls[26],'--',ls[1]]
    for i in ls1:
        print(str(i).center(14).replace('[','').replace(']',''),end='')

        
        
