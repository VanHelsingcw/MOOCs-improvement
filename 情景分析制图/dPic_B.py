# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 17:00:14 2021

@author: User01
"""



"""绘制折线图"""

import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from matplotlib.font_manager import FontProperties
font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=12)
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

data111=[-0.235, -0.110, 0, 0.192, 0.589]

# 绘制最终 决策变量tm的取值图
plt.plot(data111,marker='o')
plt.ylabel('Growth rate of student satisfaction', fontsize=12)
plt.xlabel('Different Budget Scenarios', fontsize=12)

scale_ls = range(5)
index_ls = ['SB1','SB2','S','SB3','SB4']
plt.xticks(scale_ls,index_ls, fontproperties = 'Times New Roman') ## 可以设置坐标字体
plt.yticks(fontproperties = 'Times New Roman') ## 可以设置坐标字体
plt.tick_params(labelsize=11)# 设置横纵坐标刻度值的大小以及刻度值的字体



y_major_locator=MultipleLocator(0.2)#把y轴的刻度间隔设置为10，并存在变量里
ax=plt.gca() #ax为两条坐标轴的实例
ax.yaxis.set_major_locator(y_major_locator)#把y轴的主刻度设置为10的倍数
plt.ylim(-0.3, 0.7) #设置纵坐标的起始刻度

plt.show() 


