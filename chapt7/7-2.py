"""
-*- coding:utf-8 -*-
@author : jerry
@time : 2019/5/12 16:20

"""

'''
数据清洗和准备
    排列和随机采样
    

'''

import pandas as pd
import numpy as np

#利用numpy.random.permutation函数可以轻松实现对Series或DataFrame的列的排列工作
# （permuting，随机重排序）

df=pd.DataFrame(np.arange(20).reshape(5,4))
sampler = np.random.permutation(5)
df.take(sampler)

#计算指标/哑变量

df=pd.DataFrame({'key':['b', 'b', 'a', 'c', 'a', 'b'],'data1':range(6)})
pd.get_dummies(df['key'])

#字符串对象方法
#内置字符串方法split()
#对于处理字符串，split方法常与strip()方法一起
val='a,b,  guido'
pieces=[x.strip() for  x in val.split(',')]


