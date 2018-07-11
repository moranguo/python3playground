#!/usr/bin/env python
# -*- coding:utf-8 -*-

from myThread import MyThread
from time import ctime, sleep


def fib(x):
    """求斐波那契数列之和"""
    sleep(0.005)
    if x < 2:
        return 1
    return fib(x-2) + fib(x-1)


def fac(x):
    """求阶乘"""
    sleep(0.1)
    if x < 2:
        return 1
    return x * fac(x-1)


def sum_(x):
    """自然数累加和"""
    sleep(0.1)
    if x < 2:
        return 1
    return x + sum_(x-1)

funcs = [fib, fac, sum_]  # 将三个函数放到列表中
n = 12


def main():
    nfuncs = range(len(funcs))  # nfuncs = range(3)

    print('*** SINGLE THREAD')  # 单线程计算三个函数
    for i in nfuncs:
        print('staring', funcs[i].__name__, 'at:', ctime())  # 打印出函数名称，开始运行时间
        print(funcs[i](n))  # 打印计算结果
        print(funcs[i].__name__, 'finished at:', ctime())  # 打印出函数名称，结束运行时间

    print('\n*** MULTIPLE THREADS')  # 多线程计算三个函数
    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (n,), funcs[i].__name__)  # 实例化三个MyThread对象
        threads.append(t)  # 将三个对象放到列表中

    for i in nfuncs:
        threads[i].start()  # 启动三个线程

    for i in nfuncs:
        threads[i].join()  # join()会等到线程结束或超时，即允许主线程等待线程结束
        print(threads[i].getResult())  # 调用对象的getResult()方法

    print('all DONE')

if __name__ == '__main__':  # 独立运行脚本，即在此脚本在直接运行时，才会调用main()函数
    main()