"""
-*- coding:utf-8 -*-
@author : jerry
@time : 2019/4/7 19:48

列表、集合和字典推导式
一些迭代函数，sorted(),zip(),reverse()
map()函数

"""

# 给出一个“被压缩的”序列，zip可以被用来解压序列
pitchers = [('Nolan', 'Ryan'), ('Roger', 'Clemens'),
         ('Schilling', 'Curt')]

first_name,last_name=zip(*pitchers)


#列表推导式
#列表推导式可以让代码更加简洁，逻辑更清晰
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']

[x.upper() for x in strings if len(x)>2]

# Out[14]: ['BAT', 'CAR', 'DOVE', 'PYTHON']
#map()函数
x=map(len,strings)
#获取列表中每个x的长度
len_list=[len(x) for x in strings]


"""
函数
1.函数是Python中最主要也是最重要的代码组织和复用手段。
    作为最重要的原则，如果你要重复使用相同或非常类似的代码，就需要写一个函数
2.函数使用def关键字声明，用return关键字返回值
3.函数可以有一些位置参数（positional）和一些关键字参数（keyword）。

"""
#，x和y是位置参数，而z则是关键字参数
def my_function(x,y,z=0.5):
    if z>1:
        return z*(x+y)
    else:
        return z/(x+y)

#上述函数可以通过以下形式调用
my_function(5, 6, z=0.7)
my_function(3.14, 7, 3.5)
my_function(10, 20)

"""
命名空间、作用域，和局部函数
1.函数可以访问两种不同作用域中的变量：全局（global）和局部（local）。
2.Python有一种更科学的用于描述变量作用域的名称，即命名空间（namespace）。
3.任何在函数中赋值的变量默认都是被分配到局部命名空间（local namespace）中的。
4.局部命名空间是在函数被调用时创建的，函数参数会立即填入该命名空间。在函数执行完毕之后，局部命名空间就会被销毁


"""

#调用func()之后，首先会创建出空列表a，然后添加5个元素，最后a会在该函数退出的时候被销毁。
def func():
    a=[]
    for i in range(5):
        a.append(i)
    return a

#返回多个值
def f():
    a = 5
    b = 6
    c = 7
    return {'a' : a, 'b' : b, 'c' : c}

import re

def clean_strings(strings):
    result=[]
    for value in strings:
        value=value.strip()   #去除首位空格
        value=re.sub('[!#?]','',value)   #正则表达式
        value=value.title()  #首字母大写
    return result

#或者将函数集成到列表中
def remove_punctuation(value):
    return re.sub('[!#?]','',value)


#匿名函数 (lambda)函数
def  short_function(x):
    return x*2

eq1=lambda x:x*2

def apply_to_list(some_list,f):
    return [f(x) for x in some_list]

ints=[4,0,1,5,6]
apply_to_list(ints,lambda x:x*2)