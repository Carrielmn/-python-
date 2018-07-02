# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 15:52:44 2018
练习六：获取淘宝数据并且展示(只要第一页的商品44个)
1.每一行显示4个商品信息(商品名，价格，付款，店铺名,地址，)
2.列出12排商品
3.给商品排序，从价格高到低
4.给商品排序，按照销量排序
5.商品过滤，只要15天退款的商品，包邮的商品

@author: Administrator
"""

import urllib.request as r#导入联网工具包，命令为r
url='https://s.taobao.com/search?q=%E8%A3%A4%E5%AD%90&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=44&ajax=true'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
#data字典-》mods 字典-》itemlist 字典-》data字典-》auctions 列表-》index 0 字典-》raw_title 变量
data['mods']['itemlist']['data']['auctions'][0]['raw_title']
#第一问
for i in range(0,44):
    print('商品名:{}'.format(data['mods']['itemlist']['data']['auctions'][i]['raw_title']),'价格:{}'.format(data['mods']['itemlist']['data']['auctions'][i]['view_price']),
          '付款人数:{}'.format(data['mods']['itemlist']['data']['auctions'][i]['view_sales']),'店铺名:{}'.format(data['mods']['itemlist']['data']['auctions'][i]['nick']),
          '地址:{}'.format(data['mods']['itemlist']['data']['auctions'][i]['item_loc']))
    if (i+1)%4==0:
        print('***************')
#第二问     
for i in range(0,44,4):
    print('商品名:{}'.format(data['mods']['itemlist']['data']['auctions'][i]['raw_title']),'价格:{}'.format(data['mods']['itemlist']['data']['auctions'][i]['view_price']),
          '付款人数:{}'.format(data['mods']['itemlist']['data']['auctions'][i]['view_sales']),'店铺名:{}'.format(data['mods']['itemlist']['data']['auctions'][i]['nick']),
          '地址:{}'.format(data['mods']['itemlist']['data']['auctions'][i]['item_loc']))
#第三问
ls=[]
for i in range(0,44):
    a=data['mods']['itemlist']['data']['auctions'][i]['view_price']
    b=float(a)
    ls.append(b)
lss=sorted(ls)
ls1=reversed(lss)
for j in ls1:
   print(j,end='\t')

#第四问
import re   
xiaoshou=[]
for i in range(0,44):
    x=data['mods']['itemlist']['data']['auctions'][i]['view_sales']
    y=re.sub('\D','',x)
    z=int(y)
    xiaoshou.append(z)
xiaoshou1=sorted(xiaoshou)
xiaoshou2=reversed(xiaoshou1)
for j in xiaoshou2:
   print(j,end='\t')
 
   
   
 #第五问 

for i in range(0,44):
    a=data['mods']['itemlist']['data']['auctions'][i]['raw_title']
    y=data['mods']['itemlist']['data']['auctions'][i]['view_fee']
    if y=='0.00':
        try:
            x=data['mods']['itemlist']['data']['auctions'][i]['icon'][0]['iconPopupComplex']['subIcons'][0]['icon_content']
            if (x=="15天退货"):
                print(i,a,'15天退货','包邮')
        except Exception as err:
            continue
for j in range(0,44):
    a=data['mods']['itemlist']['data']['auctions'][j]['raw_title']
    y=data['mods']['itemlist']['data']['auctions'][j]['view_fee']
    if y=='0.00':
        print(a,'包邮')
    else:
        print(a,'不包邮')