'''
fixture的作用范围
fixture里面有个scope参数可以控制fixture的作用范围：session>module>class>function
-function：每一个函数或方法都会调用
-class：每一个类调用一次，一个类中可以有多个方法
-module：每一个.py文件调用一次，该文件内又有多个function和class
-session：是多个文件调用一次，可以跨.py文件调用，每个.py文件就是module
'''
import pytest


# @pytest.fixture（）如果不写参数，参数就是scope="function"
@pytest.fixture()
def test1():
    a = 'leo'
    print('\nfixture 传出a')
    return a


@pytest.fixture(scope='function')
def test2():
    b = '男'
    print('\nfixture 传出b')
    return b


def test3(test1):
    name = 'leo'
    print('找到name')
    assert test1 == name


def test4(test2):
    sex = '男'
    print('找到sex')
    assert test2 == sex


class TestCase:
    def test5(self, test1):
        name = 'leo'
        print('找到name')
        assert test1 == name

    def test6(self, test2):
        sex = '男'
        print('找到sex')
        assert test2 == sex


if __name__ == "__main__":
    pytest.main(["-s", "-v", "fixture_scope_function_test.py"])
