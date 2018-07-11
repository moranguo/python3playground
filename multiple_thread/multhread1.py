#!/usr/bin/env python
# -*- coding:utf-8 -*-
# python 3 has no module named 'thread'
import thread
from time import sleep,ctime


def loop0():
    print('start loop 0 at:', ctime())
    sleep(4)
    print('loop 0 done at:', ctime())


def loop1():
    print('start loop 1 at:', ctime())
    sleep(2)
    print('loop 1 done at:', ctime())


def main():
    print('starting at:', ctime())
    thread.start_new_thread(loop0, ())
    # 函数start_new_thread()产生一个新线程来运行函数loop0()

    thread.start_new_thread(loop1, ())
    # 同上，两个线程同同时运行

    sleep(6)  # 主线程睡眠等待；如果主线程（此程序本身）没有停下来，就会直接运行下一条语句，不会等待两个线程运行完毕
    print('all DONE at: ', ctime())

if __name__ == '__main__':
    main()