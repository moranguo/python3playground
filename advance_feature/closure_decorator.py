import time


def outer():
    cheer = 'hello '

    def inner(name):
        return cheer + name
    return inner


def record_time(func):
    some_thing = 'some_thing'

    def wrapper(*kwargs):
        print('%s is print in wrapper' % some_thing)
        print('function start at {}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        result = func(*kwargs)
        print('function end at {}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        return result
    return wrapper


#注意这一行，我们把record_time这个函数装饰到sum函数上。
@record_time
def sum(*kwargs):
    total = 0
    # 模拟长时间运行的函数
    time.sleep(5)
    for ele in kwargs:
        total = total + ele
    return total


if __name__ == "__main__":
    print(outer()('Eric'))

    print(sum(1, 2, 3, 4, 5))