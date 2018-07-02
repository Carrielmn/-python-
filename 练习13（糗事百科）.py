# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 14:26:02 2018
URL(Uniform Resource Locator,统一资源定位符)本地、网络 路径
baidu.com
www.baidu.com
http://www.baidu.com-----------------------标准的URL
读我.txt
d:/qqyu/读我.txt
file:///d:/qqyu/读我.txt-------------------标准的URL

打开网页有几种可能性：
正常情况--OK（200）
对方挂了
自己网络问题
data=r.urlopen(url).read().decode('utf-8')#简单粗暴的方式，会出现很多问题

############题目
题目十三：糗事百科数据爬取
1.爬取作者和内容
2.爬取13页
3.下载图片。想做就做


@author: Administrator
"""





import urllib.request as r#导入URL工具包 并且命令为r
req=r.Request('https://www.qiushibaike.com/',headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'})
myurl=r.urlopen(req)
print(myurl.getcode())
data=myurl.read().decode('utf-8')
import re
lss=re.compile('<h2>\n(.*?)\n</h2>',re.S).findall(data)
lss1=re.compile('<h2>(.*?)</h2>',re.S).findall(data)
if lss==re.compile('<h2>\n(.*?)\n</h2>',re.S).findall(data):
    print(lss)
else:
    print(lss1)
ls1=re.compile('<span>\n\n(.*?)\n</span>',re.S).findall(data)
print(ls1)
for i in range(0,25):
    print("作者:{}\n内容：{}".format(lss1[i],ls1[i]))

import urllib.request as r
for i in range(1,14):
    req=r.Request('https://www.qiushibaike.com/8hr/page/{}/'.format(i),headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'})
    myurl=r.urlopen(req)
    print(myurl.getcode())
    data=myurl.read().decode('utf-8')
    import re
    ls=re.compile('<h2>\n(.*?)\n</h2>',re.S).findall(data)
    ls2=re.compile('<h2>(.*?)</h2>',re.S).findall(data)
    if ls==re.compile('<h2>\n(.*?)\n</h2>',re.S).findall(data):
        print(ls)
    else:
        print(ls2)
    ls3=re.compile('<span>\n\n(.*?)\n</span>',re.S).findall(data)
    print(ls3)
    for j in range(0,25):
        print("作者:{}\n内容：{}".format(ls2[j],ls3[j]))






























import urllib.request as r#导入URL工具包 并且命令为r
myconn=r.urlopen('http://www.baidu.com')
if myconn.getcode()==200:
    data=myconn.read().decode('utf-8')
    print(data)
else:
    print('无法访问此网站')
myconn.close()


"""
raise RemoteDisconnected("Remote end closed connection without"
RemoteDisconnected: Remote end closed connection without response
爬虫里面非常关键的：反爬虫
1.直接屏蔽程序爬取数据
2.如果访问对方服务器次数过大，对方会屏蔽你的IP/屏蔽十分钟....

"""
req=r.Request('https://www.qiushibaike.com/',headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'})
myurl=r.urlopen(req)
print(myurl.getcode())
data=myurl.read().decode('utf-8')

pat='<div class="content">(.*?)</div>'
import re
ls=re.compile(pat,re.S).findall(data)

url='https://pic.qiushibaike.com/system/pictures/11292/112920206/medium/app112920206.jpg'
r.urlretrieve(url,'./tmp.jpg')#retrieve下载文件










