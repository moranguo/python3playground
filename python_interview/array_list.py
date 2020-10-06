'''
list和array的区别
list和array都可以根据索引来取其中的元素。
list是列表，list中的元素的数据类型可以不一样。array是数组，数组中的元素的数据类型必须一样。
list不可以进行四则运算，array可以进行四则运算。
'''

x = [1,2,'a']   #x是一个list，list里面的元素的数据类型可以不同
print(x[0])     #可以根据索引取x的元素
y = x + x       #列表无法运算，+号只能将两个list拼接
print(y)        #拼接后的list

import numpy as np
a = np.array([1,2])  #a是一个数组
print(a[0])         #可以根据索引来取a中的元素
b = a + a           #数组可以运算
print(b)            #运算后得到的数组
