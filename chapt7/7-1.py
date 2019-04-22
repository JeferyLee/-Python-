"""
-*- coding:utf-8 -*-
@author : jerry
@time : 2019/4/18 19:50

"""

"""
数据清洗
    处理缺失数据
    滤除缺失数据
    填充缺失数据
数据转换
    移除重复数据
    替换值
    重命名轴索引
    


"""

import pandas as pd
import numpy as np


#处理缺失数据
# pandas使用浮点值NaN（Not a Number）表示缺失数据
#dropna()   根据各标签的值中是否存在缺失数据对轴标签进行过滤。
#fillna()   用指定值或插值方法填充缺失数据
string_data=pd.Series(['aardvark', 'artichoke', np.nan, 'avocado'])
string_data.isnull()

#滤除缺失数据
# dropna()

data=pd.DataFrame(np.arange(12).reshape(3,4))
data.dropna()   #对于DataFrame对象，dropna默认丢弃任何含有缺失值的行。
data.dropna(how='all')   #删除只有NA的行

#填充缺失数据
#在不想对空值进行滤除的情况下，可以通过赋值进行处理
from numpy import nan as NA
df=pd.DataFrame(np.random.randn(7,3))
df.iloc[:4,2]=NA
df.fillna(0)


#移除重复数据
data=pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'],
              'k2': [1, 1, 2, 3, 3, 4, 4]})

# DataFrame的duplicated方法返回一个布尔型Series
data.duplicated()
# drop_duplicates方法，它会返回一个DataFrame，重复的数组会标为False：
data.drop_duplicates()


# 利用函数或映射进行数据转换
data=pd.DataFrame({'food':['bacon', 'pulled pork', 'bacon',
                           'Pastrami', 'corned beef', 'Bacon',
                           'pastrami', 'honey ham', 'nova lox'],
                   'ounces':[4, 3, 12, 6, 7.5, 8, 3, 5, 6]})



meat_to_animal = { 'bacon': 'pig', 'pulled pork': 'pig', 'pastrami': 'cow',
                   'corned beef': 'cow', 'honey ham': 'pig', 'nova lox': 'salmon' }

# Series的map方法可以接受一个函数或含有映射关系的字典型对象
lowercased=data['food'].str.lower()

#替换值
data=pd.Series([[1,-999,3,-999,-1000,2]])
#替换为NaN
data.replace([-999,-1000],np.nan)   #可以一次替换为多个
# 要让每个值有不同的替换值，可以传递一个替换列表
data.replace([-999,-1000],[np.nan,0])

#重命名轴索引
data=pd.DataFrame(np.arange(12).reshape((3,4)),
                  index=['Ohio', 'Colorado', 'New York'],
             columns=['one', 'two', 'three', 'four'])

transform=lambda x :x[:4].upper()
data.index.map(transform)  #返回修改后的序列

#或者赋值给index
data.index=data.index.map(transform)

#使用rename()创建数据集的转换版（不修改原始数据）
data.rename(index=str.title,columns=str.upper)

# rename可以结合字典型对象实现对部分轴标签的更新
data.rename(index={'OHIO':'INDIANA'},
            columns={'three':'peekaboo'})




