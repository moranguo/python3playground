#coding:utf-8
from multiprocessing import Pool, freeze_support
import os,time,random


def worker(msg):
    t_start = time.time()
    print("%s 开始执行，进程号为%d"%(msg,os.getpid()))
# random.random()随机生成0-1之间的浮点数
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg,"执行完毕，耗时%0.2f" % (t_stop-t_start))

'''
大致就是windows创建进程没有fork方法，默认是spawn，而linux创建进程默认是fork方法。
为了什么进程保护，代码必须放在if __name__ == '__main__':下面。
'''
if __name__ == '__main__':
    # 必须要加上freeze_support,
    freeze_support()
    po = Pool(3)
    #定义一个进程池，最大进程数3
    for i in range(0,10):
        po.apply_async(worker,(i,))
    print("---start----")
    po.close()
    po.join()
    print("----end----")