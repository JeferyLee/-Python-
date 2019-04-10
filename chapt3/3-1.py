"""
-*- coding:utf-8 -*-
@author : jerry
@time : 2019/4/10 20:31

"""

import numpy as np
"""
NumPy最重要的一个特点就是其N维数组对象（即ndarray），
该对象是一个快速而灵活的大数据集容器。你可以利用这种数组对整块数据执行一些数学运算，
其语法跟标量元素之间的运算一样

    常用函数：
    array,arange,zeros
    array:将输入数据（列表、元组、数组）转换为ndarray
    arange:与内置函数range类似，但该函数返回的是ndarray而不是列表
    zeros:产生全0数组
"""
data=np.random.randn(2,3)       #randn函数返回一个或一组样本，具有标准正态分布。

# 创建ndarray
# 创建数组最简单的办法就是使用array函数。
# 它接受一切序列型的对象（包括其他数组），
# 然后产生一个新的含有传入数据的NumPy数组

data1=[6,7.5,8,0,1]
arr1=np.array(data1)
# array([ 6. ,  7.5,  8. ,  0. ,  1. ])

# NumPy数组的运算

arr=np.array([[1,2,3],[4,5,6]])
arr*arr
# array([[ 1,  4,  9],
#        [16, 25, 36]])

# 基本的索引和切片

