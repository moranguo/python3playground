#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""创建一个Thread实例，传给它一个可调用的类对象"""


import threading
from time import sleep, ctime

loops = [4, 2]
# 1储存每个列表的循环时间
# 2间接说明循环的个数


class ThreadFunc(object):
    """
    想让这个类在调用函数方面尽量地通用，并不局限与loop()函数。
    这个类保存了函数本身，函数的参数，以及函数名字的字符串。
    构造函数__init__()中做了这些值的赋值操作。
    """

    def __init__(self, func, args, name=''):
        super(ThreadFunc, self).__init__()
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):  # 用来执行类中的函数
        self.func(*self.args)


def loop(nloop, nsec):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())


def main():
    print('starting at:', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=ThreadFunc(loop, (i, loops[i]), loop.__name__))
        # 1.实例化Thread对象时，同时也会实例化ThreadFunction对象，即实例化了两个对象
        # 2.由于已经有了要用的参数，就不用额外添加参数到Thread()的构造器中
        # 3.这里时传送类对象，而18.4中传送的是函数

        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('all DONE at:', ctime())

if __name__ == '__main__':
    main()