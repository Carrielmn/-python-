# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 13:40:37 2018

@author: Administrator
"""
print('您的无忧选择')
print('              --------             / \          ---------')
print('             |                    /   \             |      ')
print('             |                   /     \            |')
print('             |--------          /-------\           |')
print('             |                 /         \          |')
print('             |                /           \         |')
print('              --------       /             \        |')
print()
print(' \            /\            /    |           |       / \      ----------')   
print('  \          /  \          /     |           |      /   \          |')
print('   \        /    \        /      |           |     /     \         | ')
print('    \      /      \      /       |-----------|    /-------\        | ')
print('     \    /        \    /        |           |   /         \       |  ')
print('      \  /          \  /         |           |  /           \      | ')  
print('       \/            \/          |           | /             \     |')


import urllib.request as r
import re
import random
d=r.urlopen('http://home.meishichina.com/recipe-menu.html')
data=d.read().decode('utf-8')
c1=re.compile('href="https://www.meishichina.com/mofang/(.*?)/" target="_blank">(.*?)</a></li>').findall(data)
items=[]      
for i in range(len(c1)):
    items.append(c1[i][1])    
a="不满意" 
while a=="不满意":
    print("为客官推荐:"+random.choice(items))
    print('温馨提示：如果想小吃继续为您推荐的美食，请输入"不满意",结束请输入任意词')  
    a=input("-->：")   
print('              ｜    ')
print('           ｜     ｜')
print('             /  \ ')
print('           /      \ ')
print('         /    欢    \ ')
print('       /      迎      \ ')
print('     /        下        \ ')
print('    ---------------------- ')
print('    \         次          /')
print('     \        使         /')  
print('      \       用        /')
print('       \               / ')
print('        \             /')
print('         -------------  ')

