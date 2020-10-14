import pytest
import time
from multiprocessing import cpu_count


class TestSample(object):
    def test_equal(self):
        assert 1 == 1
        time.sleep(2)

    def test_not_equal(self):
        assert 1 != 0
        time.sleep(2)

    def test3(self):
        assert 1 == 1
        time.sleep(2)


if __name__ == "__main__":
    print("CPU的核数为：{}".format(cpu_count()))
    print(type(cpu_count()))

    # pip install pytest-xdist
    # 语法：
    # pytest -n NUMCPUS
    # 以下为2个进程并行运行
    # pytest -n 2
    # 使用与CPU内核一样多的进程来并发
    # pytest -n auto
    # gw0 I / gw1 I / gw2 I / gw3 I / gw4 I / gw5 I / gw6 I / gw7 I， 说明有CPU有8核
    pytest.main(["-s", "-v", "-n", "auto", "xdist_test.py"])
    # 3 passed in 3.44s

    # 没有并发，顺序执行
    pytest.main(["-s", "-v", "xdist_test.py"])
    # 3 passed in 6.02s


