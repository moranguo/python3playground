import threading
import time
def thread():
    time.sleep(2)
    print('---子线程结束---')
def main():
    t1 = threading.Thread(target=thread)
    t1.setDaemon(True)#设置子线程守护主线程
    t1.start()
    print('---主线程结束---')

if __name__ =='__main__':
    main()
# 执行结果
# ---主线程结束--- #只有主线程结束，子线程来不及执行就被强制结束