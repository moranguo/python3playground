import pytest


@pytest.fixture(scope='class')
def test1():
    b = '男'
    print('fixture 传出了%s, 且只在class里所有用例开始前执行一次！！！' % b)
    return b


# 当类外部的函数使用scope=class的fixture时，这个fixture等同于scope=function的fixture
def test2(test1):
    assert '男' == test1
    print("test2 使用了scope为class的fixture")


def test5(test1):
    assert '男' == test1
    print("test5 使用了scope为class的fixture")


class TestCase:
    def test3(self, test1):
        name = '男'
        print('找到name')
        assert test1 == name

    def test4(self, test1):
        sex = '男'
        print('找到sex')
        assert test1 == sex


if __name__ == '__main__':
    pytest.main(["-s", "-v", "fixture_scope_class_test.py"])
