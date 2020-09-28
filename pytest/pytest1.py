# -*- coding:utf-8 -*-
import pytest

@pytest.fixture(scope='function')
def setup_function(request):
    def teardown_function():
        print("teardown_function called.")
    request.addfinalizer(teardown_function)  # 此内嵌函数做teardown工作
    print('setup_function called.')

@pytest.fixture(scope='module')
def setup_module(request):
    def teardown_module():
        print("teardown_module called.")
    request.addfinalizer(teardown_module)
    print('setup_module called.')

@pytest.mark.website
@pytest.mark.backend
def test_1(setup_function):
    print('Test_1 called.')

@pytest.mark.website
def test_2(setup_module):
    print('Test_2 called.')

def test_3(setup_module):
    print('Test_3 called.')
    assert 2==1+1              # 通过assert断言确认测试结果是否符合预期


# pytest -m "not website" pytest1.py
# pytest -m website pytest1.py

# 覆盖率测试
# pip install pytest-cov # 计算pytest覆盖率，支持输出多种格式的测试报告
# pytest  --cov-report=html --cov=./ pytest1.py
