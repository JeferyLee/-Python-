import pandas as pd
import numpy as np

df1=pd.DataFrame(np.arange(20).reshape(4,5),index=[1,2,3,4],columns=list('abcde'))

#常用描述
des=df1.describe()

#替换索引 index
df1.index=['a','b','c','d']
#替换列表名
df1.columns=['q','w','e','r','f']
#选取行
row=df1.loc['a',:]

#选取列
col=df1.loc[:,'q']

#选取单个数
cr=df1.iloc[2,1]
#获取行数
lenth_row=len(df1)
lenth_row1=df1.shape[0]

#获取列数
lenth_col=df1.shape[1]

# for i in range(0,df1.shape[0]):
#     for j in range(0,df1.shape[1]):
#         print(df1.iloc[i,j])
'''
range()与np.arange()的区别

'''
#新建df
df2=pd.DataFrame(np.arange(12).reshape(4,3),columns=list('upt'))
df2.index=['a','b','c','d']
df3=pd.concat([df1,df2],axis=1)    #横向连接
df4=pd.concat([df1,df2],axis=0)   #纵向连接




