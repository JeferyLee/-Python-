"""
-*- coding:utf-8 -*-
@author : jerry
@time : 2019/4/16 17:15

"""

"""
读取文件
    读取文件后索引与标题行处理
    缺失值处理

"""

import pandas as pd
import numpy as np

df=pd.read_csv('c:/users/lenovo/desktop/exmp1/ex1.csv')

#不是所有的文件或表格都有标题行，如果直接读取，则自动取第一行作为标题行
#以下方法可以读取该类型文件
pd.read_csv('examples/ex2.csv', header=None)    #自动分配标题行
pd.read_csv('examples/ex2.csv', names=['a', 'b', 'c', 'd', 'message'])  #自定义标题行


#缺失值处理
# 缺失数据经常是要么没有（空字符串），要么用某个标记值表示
result=pd.read_csv('c:/users/lenovo/desktop/exmp1/ex5.csv')
#read_csv/read_table函数的参数
#path,sep,header,index_col,names,skiprows

df2=pd.read_csv('c:/users/lenovo/desktop/exmp1/ex5.csv')

#json数据
# JSON（JavaScript Object Notation的简称）已经成为通过HTTP请求在Web浏览器和其他应用程序之间发送数据的标准格式之一
pd.read_json()  #读取json类型文件

#二进制数据格式
# 实现数据的高效二进制格式存储最简单的办法之一是使用Python内置的pickle序列化
#将frame类型写入pickle
# frame.to_pickle()
pd.read_pickle()
# pickle仅建议用于短期存储格式。其原因是很难保证该格式永远是稳定的

"""
使用HDF5格式

HDF5是一种存储大规模科学数组数据的非常好的文件格式。
它可以被作为C标准库，带有许多语言的接口，如Java、Python和MATLAB等。
HDF5中的HDF指的是层次型数据格式（hierarchical data format）。
每个HDF5文件都含有一个文件系统式的节点结构，它使你能够存储多个数据集并支持元数据

"""
frame=pd.DataFrame({'a':np.random.randn(100)})
store=pd.HDFStore('c:/users/lenovo/desktop/exmp1/mydata.h5')

store['obj1']=frame
store['obj1_col']=frame['a']


"""
读取Microsoft excel 文件
pd.read_excel()
pd.read_csv()
frame.to_excel()
"""

# 如果要将pandas数据写入为Excel格式，你必须首先创建一个ExcelWriter

# writer=pd.ExcelWriter(path)
# frame.to_excel(writer,'Sheet1')
# writer.save()


#或者直接
# frame.to_excel(path)
