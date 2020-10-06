import threading
import time

def thread():
    print('---子线程开始---')
    time.sleep(2)
    print('---子线程结束---')

def main():
    print('---主线程开始---')
    t1 = threading.Thread(target=thread)
    t1.setDaemon(True)
    t1.start()
    #1 线程同步，主线程堵塞1s 然后主线程结束，子线程继续执行
    #2 如果不设置timeout参数就等子线程结束主线程再结束
    t1.join(timeout=1)#3 如果设置了setDaemon=True和timeout=1主线程等待1s后会强制杀死子线程，然后主线程结束
    print('---主线程结束---')

if __name__=='__main__':
    main()