#!/usr/bin/env python
# -*- coding:utf-8 -*-

import thread
from time import sleep, ctime

loops = [4, 2]
# 1储存每个循环的睡眠时间
# 2间接说明了循环的个数


def loop(nloop, nsec, lock):
    """记录循环的号码和睡眠时间，并添加锁"""
    print 'start loop', nloop, 'at:', ctime()
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()
    lock.release()  # 当sleep()时间结束，释放锁用以通知主线程，此子线程已结束


def main():
    """包含三个循环：创建锁；创建线程并分配锁；线程结束并解锁"""
    print 'Starting at:', ctime()
    locks = []
    nloops = range(len(loops))  # 利用列表元素个数说明循环次数

    for i in nloops:
        lock = thread.allocate_lock()  # allocate_lock()函数分配锁对象
        lock.acquire()  # 获取锁对象
        locks.append(lock)  # 创建锁列表

    for i in nloops:
        thread.start_new_thread(loop, (i, loops[i], locks[i]))  # 创建循环线程

    for i in nloops:
        while locks[i].locked():  # 主线程对锁对象进行检查（暂停主线程）。当有线程结束，解锁，主线程才执行下条语句
            pass

    print 'all DONE at:', ctime()

if __name__ == '__main__':
    main()