"""
-*- coding:utf-8 -*-
@author : jerry
@time : 2019/4/14 16:55

"""


"""
pandas基础
行和列的索引
用loc和iloc进行选取
对于DataFrame的行的标签索引，我引入了特殊的标签运算符loc和iloc。它们可以让你用类似NumPy的标记，
使用轴标签（loc）或整数索引（iloc），从DataFrame选择行和列的子集

"""

import pandas as pd
import numpy as np

data=pd.DataFrame(np.arange(16).reshape(4,4,),
                  index=['Ohio', 'Colorado', 'Utah', 'New York'],
                  columns=['one', 'two', 'three', 'four'])

#利用标签选取行和多列
data.loc['Colorado',['two','three']]

#利用iloc和整数进行行和列的选取
data.iloc[2,[2,3]]

#算术运算和数据对齐

"""
pandas最重要的一个功能是，它可以对不同索引的对象进行算术运算。
在将对象相加时，如果存在不同的索引对，则结果的索引就是该索引对的并集
"""

df1=pd.DataFrame(np.arange(9).reshape(3,3),
                 columns=list('bcd'),
                 index=['Ohio', 'Texas', 'Colorado'])

df2=pd.DataFrame(np.arange(12).reshape(4,3),
                 columns=list('bde'),
                 index=['Utah', 'Ohio', 'Texas', 'Oregon'])

df1+df2
#两个表格中没有共同的序列，则以缺省值呈现

# 在算术方法中填充值

df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)),
              columns=list('abcd'))
df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)),
            columns=list('abcde'))

df1.add(df2,fill_value=0)    #两者相同序列的位置直接相加，不同序列填充各自表格内的值

# DataFrame和Series之间的运算

arr=np.arange(12).reshape(3,4)
arr[0]
arr-arr[0]   #当多维数组减去数组中某一行时，每一行都会执行这个操作，这就叫做广播

# 函数应用和映射
# NumPy的ufuncs（元素级数组方法）也可用于操作pandas对象

frame=pd.DataFrame(np.arange(12).reshape(4,3),
                   columns=list('bde'),
                   index=['Utah', 'Ohio', 'Texas', 'Oregon'])

np.abs(frame)

#使用DataFrame的apply方法将函数应用到由各列或行所形成的一维数组上

format=lambda x: '%.2f'%x   #将frame中各元素改为浮点值
frame.applymap(format)     #跟apply方法有所区别，apply(func)函数可添加axis参数决定行或列的运算

"""
根据条件对数据集排序（sorting）也是一种重要的内置运算
对行或列索引进行排序（按字典顺序），
可使用sort_index方法，它将返回一个已排序的新对象：

"""

obj = pd.Series(range(4), index=['d', 'a', 'b', 'c'])
obj.sort_index()    #返回一个已排序的新对象

# 对于DataFrame，则可以根据任意一个轴上的索引进行排序：
frame=pd.DataFrame(np.arange(8).reshape(2,4),
                   index=['three', 'one'],columns=list('dabc'))

frame.sort_index()
frame.sort_index(axis=1)   #对行或列进行排序，默认为升序排列

frame.sort_index(by='b')   #根据某一列进行排序

# 带有重复标签的轴索引

# 汇总和计算描述统计
# pandas对象拥有一组常用的数学和统计方法。它们大部分都属于约简和汇总统计，
# 用于从Series中提取单个值（如sum或mean）或从DataFrame的行或列中提取一个Series

df=pd.DataFrame(np.arange(12).reshape(4,3),index=[1,2,3,4],columns=list('abc'))
df.sum()  #调用DataFrame的sum方法将会返回一个含有列的和的Series
df.sum(axis=1)  #传入axis='columns'或axis=1将会按行进行求和运算

#describe()函数一次返回多个汇总统计
#（重要）常用描述和汇总统计
#count,describe,min,max,sum,mean,var,std


#相关系数与协方差
# Series的corr方法用于计算两个Series中重叠的、非NA的、按索引对齐的值的相关系数。与此类似，cov用于计算协方差
# DataFrame的corr和cov方法将以DataFrame的形式分别返回完整的相关系数或协方差矩阵

# 唯一值、值计数以及成员资格
obj = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
obj.unique()
# array(['c', 'a', 'd', 'b'], dtype=object)

# value_counts用于计算一个Series中各值出现的频率
obj.value_counts()