'''
提示: 闭包，作用域 正确答案是[9,9,9,9]，而不是[0,3,6,9]产生的原因是Python的闭包的后期绑定导致的，
这意味着在闭包中的变量是在内部函数被调用的时候被查找的，因为，最后函数被调用的时候，for循环已经完成, i 的值最后是3,
因此每一个返回值的i都是3,所以最后的结果是[9,9,9,9]
这篇讲诉的很详细了 https://www.cnblogs.com/shiqi17/p/9608195.html
'''


def multi():
    return [lambda x: i*x for i in range(4)]


print([m(3) for m in multi()])