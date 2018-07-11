#!usr/bin/env python
# -*- coding:utf-8 -*-

"""创建一个Thread（threading模块中的类）的实例，传给它一个函数"""


import threading
from time import sleep, ctime

loops = [4, 2]
# 1储存每个循环的睡眠时间
# 2间接说明了循环的个数


def loop(nloop, nsec):
    """1记录循环的号码 2记录睡眠时间"""
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())


def main():
    print('starting at:',  ctime())
    threads = []
    nloops = range(len(loops))  # 记录循环次数

    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        # 1实例化Thread类对象，将函数（target）和参数（args）传入，得到返回的Thread实例：线程对象t。
        # 2实例化（调用）Thread类时，不会像thread.star_new_thread那样，线程立即开始，这样可以更好的同步。
        threads.append(t)  # 创建对象列表

    for i in nloops:
        threads[i].start()  # 开始线程的执行

    for i in nloops:
        threads[i].join()
        # 1调用join()方法后，主线程会等到线程结束才执行下条语句，相比使用等待锁释放的无线循环（自旋锁）更为清楚。
        # 2若主线程除了等待线程结束外，还有其他事情要做（如处理或等待其他的客户请求），就不用调用join()。主线程
        #  依然会等待线程执行完毕。

    print('all DONE at:', ctime())

if __name__ == '__main__':
    main()