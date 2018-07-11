#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
1.单独化子类，让Thread的子类更加通用。
2.加上getResult()函数译返回函数的运行结果。

"""
import threading
from time import ctime
#python3 没有全局函数apply(), 可以安装apply module
import apply as apply


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def getResult(self):
        return self.res

    def run(self):
        print('starting', self.name, 'at:', ctime())
        self.res = apply.apply(self.func, self.args)
        print(self.name, 'finished at:', ctime())