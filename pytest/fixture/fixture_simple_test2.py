import pytest


@pytest.fixture()
def test1():
    a = 'test_a'
    print('\n传出test_a')
    return a


@pytest.fixture()
def test2(test1):
    a = 'test_b'
    print('\n传出test_b')
    assert test1 == 'test_a'
    return a


# 对于fixture的嵌套调用，以及多次调用，test1只会执行一次
def test(test1, test2):
    assert 'test_a' == test1
    assert 'test_b' == test2
    assert 1 == 1


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'fixture_simple_test2.py'])
