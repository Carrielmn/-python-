# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 17:11:30 2018

@author: Administrator
"""

import urllib.request as r#导入联网工具包，命令为r
url='https://s.taobao.com/search?q=%E8%80%B3%E7%8E%AF&imgfile=&js=1&stats_click=search_radio_all:1&initiative_id=staobaoz_20180622&ie=utf8&loc=%E5%8E%A6%E9%97%A8&ajax=true'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
f=open('./c.csv','a',encoding='utf-8')
for i in range(0,36):
    a=data['mods']['itemlist']['data']['auctions'][i]['raw_title']
    b=data['mods']['itemlist']['data']['auctions'][i]['view_price']
    c=data['mods']['itemlist']['data']['auctions'][i]['view_sales']
    d=data['mods']['itemlist']['data']['auctions'][i]['nick']
    e=data['mods']['itemlist']['data']['auctions'][i]['item_loc']
#    print(a,b,c,d,e)
    f.write('商品名:{},价格:{},付款人数:{},店铺名:{},地址:{}\n'.format(a,b,c,d,e))
f.close()
    





for i in range(1,100):
    a=44*i
    import urllib.request as r#导入联网工具包，命令为rurl='https://s.taobao.com/search?q=%E8%80%B3%E7%8E%AF&imgfile=&js=1&stats_click=search_radio_all:1&initiative_id=staobaoz_20180622&ie=utf8&loc=%E5%8E%A6%E9%97%A8'
    url='https://s.taobao.com/search?q=%E8%80%B3%E7%8E%AF&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180622&ie=utf8&loc=%E5%8E%A6%E9%97%A8&bcoffset=4&p4ppushleft=1%2C48&ntoffset=4&s={}&ajax=true'.format(a)
    data=r.urlopen(url).read().decode('utf-8')
    #讲str类型转换为dict
    import json
    data=json.loads(data)
    f=open('./c.csv','a',encoding='utf-8')
    for j in range(0,44):
        a=data['mods']['itemlist']['data']['auctions'][j]['raw_title']
        b=data['mods']['itemlist']['data']['auctions'][j]['view_price']
        c=data['mods']['itemlist']['data']['auctions'][j]['view_sales']
        d=data['mods']['itemlist']['data']['auctions'][j]['nick']
        e=data['mods']['itemlist']['data']['auctions'][j]['item_loc']
        f.write('商品名:{},价格:{},付款人数:{},店铺名:{},地址:{}\n'.format(a,b,c,d,e))
f.close()
