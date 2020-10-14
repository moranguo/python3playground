import pytest


@pytest.fixture()
def test1():
    a = 'leo'
    return a


# fixture可以当做参数传入
def test2(test1):
    assert test1 == 'leo'


@pytest.fixture()
def test3():
    a = 'leo'
    b = '123456'
    print('\n传出a,b')
    return a, b


# fixture返回多个结果
def test4(test3):
    u = test3[0]
    p = test3[1]
    assert u == 'leo'
    assert p == '123456'
    print('fixture返回多个结果，元祖形式正确')


@pytest.fixture()
def test5():
    a = 'leo'
    print('\n传出a')
    return a


@pytest.fixture()
def test6():
    b = '123456'
    print('传出b')
    return b


def test7(test5, test6):
    u = test5
    p = test6
    assert u == 'leo'
    assert p == '123456'
    print('传入多个fixture参数正确')


@pytest.fixture()
def test8():
    print("\nfixture test8 is running")

# usefixtures与传fixture区别
# 如果fixture有返回值，那么usefixturex就无法获取到返回值，这个是装饰器usefixturex与用例直接传fixture参数的区别。
# 可以混用usefixtures和直接传fixture
@pytest.mark.usefixtures('test8')
def test9(test6):
    p = test6
    assert p == '123456'
    print('传入多个fixture参数正确')


@pytest.fixture()
def test10():
    print("\nfixture test10 is running")


# usefixtures可以同时指定多个fixture，注意userfixtures的参数是字符串
@pytest.mark.usefixtures('test8', 'test10')
def test11():
    print('传入多个fixture参数正确')


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'fixture_simple_test1.py'])
