"""
-*- coding:utf-8 -*-
@author : jerry
@time : 2019/4/12 16:03

"""

"""
pandas 是Python中重要的数据分析库
    1.它含有使数据清洗和分析工作变得更快更简单的数据结构和操作工具
    2.pandas与Numpy相似，但两者不同之处在于pandas是专门为处理表格和混杂数据设计的，
    3.而NumPy更适合处理统一的数值数组数据。

pandas中两种重要的数据结构
    Series和DataFrame

"""
import pandas as pd
import numpy as np
from pandas import  Series,DataFrame
#Series是一种类似于一维数组的对象，
# 它由一组数据（各种NumPy数据类型）以及一组与之相关的数据标签（即索引）组成

obj=pd.Series([4,7,-5,3],index=['d','b','a','c'])

# 普通NumPy数组相比，你可以通过索引的方式选取Series中的单个或一组值
# 如果数据被存放在一个Python字典中，也可以直接通过这个字典来创建Series
sdata={'Ohio':35000,'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj2=pd.Series(sdata)

# Series的索引可以通过赋值的方式就地修改：
obj2.index=['Bob', 'Steve', 'Jeff', 'Ryan']

"""
DataFrame
DataFrame是一个表格型的数据结构，它含有一组有序的列，
每列可以是不同的值类型（数值、字符串、布尔值等）。

"""

#通过传入一个由等长列表或NumPy数组组成的字典
data={'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
 'year': [2000, 2001, 2002, 2001, 2002, 2003],
 'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}

frame=pd.DataFrame(data)

#通过类似字典标记的方式或属性的方式，可以将DataFrame的列获取为一个Series：
frame['state']
frame.year

#(重要)如果指定了列序列，则DataFrame的列就会按照指定顺序进行排列
#可以把列按指定顺序排列。
pd.DataFrame(data,columns=['year', 'state', 'pop'])

#将列表或数组赋值给某个列时，其长度必须跟DataFrame的长度相匹配
#删除DataFrame中某一列，使用del
del frame['debt']

#转置
frame.T
# 跟Series一样，values属性也会以二维ndarray的形式返回DataFrame中的数据
frame.values

"""
索引对象
pandas的索引对象负责管理轴标签和其他元数据（比如轴名称等）。

"""
obj=pd.DataFrame(range(3),index=['a','b','c'])

# Index对象是不可变的，因此用户不能对其进行修改
labels=pd.Index(np.arange(3))

"""
基本功能
    重新索引


"""

#重新索引，pandas对象的一个重要方法是reindex
#用该Series的reindex将会根据新索引进行重排。如果某个索引值当前不存在，就引入缺失值。
obj1=pd.DataFrame([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
obj2=obj1.reindex(['a', 'b', 'c', 'd', 'e'])

# In [94]: obj2
# Out[94]:
# a   -5.3
# b    7.2
# c    3.6
# d    4.5
# e    NaN
# dtype: float64

#对于时间序列这样的有序数据，重新索引时可能需要做一些插值处理
obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
obj3.reindex(range(6),method='ffill')

#(重要)借助DataFrame，reindex可以修改（行）索引和列。只传递一个序列时，会重新索引结果的行。
#如果重新赋值的index,原来表格中没有的index对应的值将赋值为NAN
frame3=pd.DataFrame(np.arange(9).reshape(3,3),index=['a','b','c'],
                   columns=['Ohio','Texas','California'])
frame3.reindex(['a', 'b', 'c', 'd'])

#列可以用columns关键字重新索引
states = ['Texas', 'Utah', 'California']
frame3.reindex(index=states)   #对列进行重新索引，也可以直接赋值，frame3.columns=[]

#丢弃指定轴上的项
#DataFrame对象的drop()方法返回的是一个在指定轴上删除了指定值的新对象。

new_obj=obj2.drop('c')   #默认删除行，即axis=0，通过传递axis=1或axis='columns'可以删除列的值：

data=pd.DataFrame(np.arange(16).reshape(4,4),
                  index=['Ohio', 'Colorado', 'Utah', 'New York'],
                  columns=['one', 'two', 'three', 'four'])

data.drop(['Utah','Colorado'])   #默认删除行
data.drop(['three','one'],axis=1)   #删除列

#索引、选取和过滤

obj5=pd.Series(np.arange(4),index=['a', 'b', 'c', 'd'])
obj5[obj<5]

#索引切片
obj5[2:4]
#利用标签切片
obj5['b':'c']

# 用一个值或序列对DataFrame进行索引其实就是获取一个或多个列
data['two']

data[['one','two']]

#（重要）利用列标签选取某一范围内列表
data[data['three']>5]











