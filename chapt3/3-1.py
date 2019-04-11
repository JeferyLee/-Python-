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

arr=np.arange(10)
arr_slice=arr[5:8]
#跟列表最重要的区别在于，数组切片是原始数组的视图。
# 这意味着数据不会被复制，视图上的任何修改都会直接反映到源数组上。

#l利用切片[:]方法可以给数组中所有值赋值。
arr_slice[:]=10
print(arr_slice,arr)
# [10 10 10] [ 0  1  2  3  4 10 10 10  8  9]

#多维数组
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# array([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]])
arr2d[2]
arr2d[2,1]

# 切片索引
arr2d[:2,1:]
# ([2,3],[5,6])

"""
通用函数
通用函数（即ufunc）是一种对ndarray中的数据执行元素级运算的函数

"""

arr=np.arange(10)
np.sqrt(arr)
np.exp(arr)

#二元函数
#add 将数组中对应的元素相加
#subtract 将从第一个数组中减去第二个数组


#数学和统计方法
"""
以通过数组上的一组数学函数对整个数组或某个轴向的数据进行统计计算。
sum、mean以及标准差std等聚合计算（aggregation，通常叫做约简（reduction））
既可以当做数组的实例方法调用，也可以当做顶级NumPy函数使用。
基本的数组统计方法
sum  对数组中全部或轴向的元素求和。
mean   算术平均值
std、var  标准差和方差
cumsum   所有元素的累积和
"""

arr=np.random.randn(5,4)
arr.mean()
arr.sum()

#唯一化以及其它的集合逻辑
#np.unique()函数
#它用于找出数组中的唯一值并返回已排序的结果
names=np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
np.unique(names)
# array(['Bob', 'Joe', 'Will'], dtype='<U4')

# unique(x)  #计算x中的唯一元素，并返回有序结果
# intersect1d(x,y)  计算x和y中的公共元素，并返回有序结果

#线性代数
#Numpy通过一个用于矩阵乘法的dot函数

x=np.array([[1., 2., 3.], [4., 5., 6.]])
y=np.array([[6., 23.], [-1, 7], [8, 9]])
x.dot(y)

#常用的线性代数函数
#diag   以一维数组的形式返回方阵的对角线元素。
#dot   矩阵乘法
#trace   计算对角线元素的和
#det计算矩阵行列式

#伪随机数生成
#numpy.random模块对Python内置的random进行了补充，
# 增加了一些用于高效生成多种概率分布的样本值的函数。
samples=np.random.normal(size=(4,4))

#常用numpy.random函数
#rand()产生均匀分布的样本值
#randint()从给定的上下限范围内随机选取整数
#randn()产生正太分布（平均值为0，标准差为1）的样本值

#随机漫步
import random
position=0
walk=[position]
steps=1000
for i in range(steps):
    step=1 if random.randint(0,1) else -1
    position+=step
    walk.append(position)

import matplotlib.pyplot as plt
plt.plot(walk[:100])

print(walk)

i=0
step=0
while i<1000:
    if random.randint(0, 1):
        step = 1
        print(step)
        #使用random.randint(0,1) 来模拟True和False
    else:
        step = 0
        print(step)
    i+=1