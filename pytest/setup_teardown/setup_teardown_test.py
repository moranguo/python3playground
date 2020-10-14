import pytest


def setup_module(module):
    """
    module级别的setup，直接定义为一个module里的函数
    在本module里所有test执行之前，被调用一次
    """
    ## 你的set up代码，例如：
    print("\n------ set up for module ------")

def teardown_module(module):
    """
    module级别的setup，直接定义为一个module里的函数
    在本module里所有test执行之后，被调用一次
    """
    ## 你的tear down代码，例如：
    print("\n------ tear down for module ------")

def setup_function():
    print("\n------ set up for function ------")

def teardown_function():
    print("\n------ tear down for function ------")

def test_function1():
    assert 1 == 1


class TestSample(object):
    @classmethod
    def setup_class(cls):
        """
        仅在当前测试类下的所有test执行之前，被调用一次
        注意它必须以@classmethod装饰
        """
        ## 你的set up代码，例如：
        print("\n------ set up for class------")
    @classmethod
    def teardown_class(cls):
        """
        仅在当前测试类下的所有test执行之后，被调用一次
        注意它必须以@classmethod装饰
        """
        ## 你的tear down代码，例如：
        print("\n------tear down for class------")

    def setup_method(self, method):
        """
        在当前测试类里，每一个test执行之前，被调用一次
        """
        ## 你的set up代码，例如：
        print("\n------set up for method------")

    def teardown_method(self, method):
        """
        在当前测试类里，每一个test执行之前，被调用一次
        """
        ## 你的tear down代码，例如：
        print("\n------tear down for method------")

    def test_method1(self):
        assert 1==1

    def test_method2(self):
        assert 1==1

def test_function2():
    assert 1 == 1

# 打印出setup和teardown的过程
# pytest -s -v setup_teardown_test.py