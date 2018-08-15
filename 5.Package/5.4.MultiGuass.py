#!/usr/bin/python
#  -*- coding:utf-8 -*-

import numpy as np
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

#mpl.rcParams['axes.unicode_minus'] = False
#mpl.rcParams['font.sans-serif'] = 'SimHei'

if __name__ == '__main__':
    x1, x2 = np.mgrid[-5:5:51j, -5:5:51j]  #51j的意思是，把-5到5，一共划分成了51个数字，也就是50个间隔
    x = np.stack((x1, x2), axis=2)
    # print x1 #一共50个
    # print x2 #一共50个
    # print x  #一共2500个，这样子x就变成了 (x1,y1),(x1,y2),..(x1,y50),(x2,y1),(x2,y2)...(x50，y50)

    plt.figure(figsize=(9, 8), facecolor='w')
    sigma = (np.identity(2), np.diag((3,3)), np.diag((2,5)), np.array(((2,1), (2,5))))
    print sigma #我懂了，一共四个组成部分：第一个：np.identity(2)是一个array，就是一个
    #对角线是1的2x2向量，其实是array
    #第二个np.diag((3,3))#对角线是3的2x2向量，其实是array
    #第三个np.diag((2,5))，对角线分别是2，5，的2x2向量，其实是array
    #第四个np.array(((2,1), (2,5)))，第一行是[2,1]，第二行是【2，5】
    #接下来的：sigma[i]就是看取第几个了
    for i in np.arange(4):
        ax = plt.subplot(2, 2, i+1, projection='3d')
        norm = stats.multivariate_normal((0, 0), sigma[i]) #你可以看出来：mean是1X2, sigma是2x2
        y = norm.pdf(x)  #哦，因为一个x是一个（x1，y1）这样的向量，这里求的应该是那个norm下的标准的pdf值
        ax.plot_surface(x1, x2, y, cmap=cm.Accent, rstride=2, cstride=2, alpha=0.9, lw=0.3)
        ax.set_xlabel(u'X')
        ax.set_ylabel(u'Y')
        ax.set_zlabel(u'Z')
    #plt.suptitle(u'二元高斯分布方差比较', fontsize=18)
    plt.suptitle(u'ccc', fontsize=18)
    plt.tight_layout(1.5)
    #plt.show()
