import pytest


@pytest.fixture(scope='session')
def test_session():
    sex = '男'
    print('\n fixture传出了%s, 且在当前session下执行一次！！！' % sex)
    return sex

"""
一个工程下可以建多个conftest.py的文件，一般在工程根目录下设置的conftest文件起到全局作用。
在不同子目录下也可以放conftest.py的文件，作用范围只能在改层级以及以下目录生效。
"""