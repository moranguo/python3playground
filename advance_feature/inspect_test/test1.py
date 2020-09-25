import inspect
import os
import sys
# 将上两级目录也就是advance_feature加入到sys.path中
sys.path.append(os.path.abspath(os.path.dirname(__file__) + os.path.sep + ".."))
from inspect_test.test2 import hello


class KevinTest():
    def __init__(self):
        print('i am eric huang')

    def say_hello(self, name):
        hello()
        return 'Hello {name}'.format(name=name)


if __name__ == "__main__":
    # 取到当前模块名
    print(inspect.getmodulename(__file__))

    # inspect.getmodule(object) 用来返回object定义在哪个module中
    print(inspect.getmodule(hello))

    # inspect.getfile(object)用来返回object定义在哪个 file 中。
    test = KevinTest()
    print(inspect.getfile(test.say_hello))

    # inspect.getmembers(object) 用来返回object的所有成员列表（为(name, value)的形式）。
    # 输出test里的所有是方法的成员变量。
    print(inspect.getmembers(test, inspect.ismethod))


