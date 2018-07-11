#!/usr/bin/env python
# -*- coding: utf8 -*-

from random import randint  # randint随机进行生产和消耗
from time import sleep
#from Queue import Queue
import queue
from myThread import MyThread


def writeQ(queue):
    print('producing object for Q...', queue.put('xxx', 1))  # 把xxx对象放进队列中，并等待队列中有空间为止
    print("size now", queue.qsize())  # 返回队列大小


def readQ(queue):
    val = queue.get(1)  # 从队列中取出一个对象（消耗）
    print('consumed object form Q... size now', queue.qsize())  # 返回队列大小


def writer(queue, loops):
    """一次往队列中放进一个对象，等待一会，然后再做给定次数的相同的事"""
    for i in range(loops):
        writeQ(queue)  # 调用writeQ,放进一个对象
        sleep(randint(1, 3))  # 随机睡眠1~3秒


def reader(queue, loops):
    """一次从队列中取出一个对象，等待一会，然后做给定次数的相同的事"""
    for i in range(loops):
        readQ(queue)
        sleep(randint(2, 5))  # 睡眠时间比 write 中的长，以使 reader 在取数据的时候能够拿到数据

funcs = [writer, reader]
nfuncs = range(len(funcs))


def main():
    nloops = randint(2, 9)
    q = queue.Queue(32)  # 创建一个大小为32的对象，和 q 绑定

    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (q, nloops), funcs[i].__name__)  # 实例化 writer, reader 这两个对象
        threads.append(t)  # 放入空列表中

    for i in nfuncs:
        threads[i].start()  # 启动线程

    for i in nfuncs:
        threads[i].join()  # join()会等到线程结束或超时，即允许主线程等待线程结束

    print('all DONE')

if __name__ == '__main__':  # 独立运行脚本
    main()