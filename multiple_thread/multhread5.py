#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""从Thread类中派生出一个子例，创建一个这个子类的实例"""

import threading
from time import sleep, ctime

loops = (4, 2)


class MyThread(threading.Thread):
    """
    1.子类化Thread类
    2.要先调用基类的构造器，进行显式覆盖
    3.重新定义run()函数
    """
    def __init__(self, func, args, name=''):
        super(MyThread, self).__init__()
        self.name = name
        self.func = func
        self.args = args

    def run(self):
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
        t = MyThread(loop, (i, loops[i]), loop.__name__)  # 创建子类的实例
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('all DONE at:', ctime())

if __name__ == '__main__':
    main()