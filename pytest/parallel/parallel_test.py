import pytest
import time


class TestSample(object):
    def test_equal(self):
        assert 1 == 1
        time.sleep(1)

    def test_not_equal(self):
        assert 1 != 0
        time.sleep(1)

    def test3(self):
        assert 1 == 1
        time.sleep(1)


if __name__ == "__main__":
    # pip install pytest-parallel
    # –workers (optional)  X, 多进程运行， X 是进程数，默认值 1。
    # –tests-per-worker (optional)   X, 多线程运行， X 是每个 worker 运行的最大并发线程数， 默认值1。
    # 注意：这个插件仅仅支持 python 3.6 版本及以上，而且如果你想多进程并发，必须跑在 Unix 或者 Mac 机器上，
    # windows 环境仅仅支持多线程运行。

    # ERROR: file not found: –-tests-per-worker
    # 使用命令行方式运行，pytest -s -v --tests-per-worker 3 parallel_test.py
    pytest.main(["-s", "-v", "–-tests-per-worker", "3", "parallel_test.py"])

    # 从理论上来说，pytest-parallel 要更好一些，因为 pytest-xdist 有以下缺点：
    #   非线程安全
    #   多线程时性能不佳
    #   需要状态隔离
    # 但是实际应用中，pytest-parallel 有时会出现如下运行错误：BrokenPipeError: [WinError 109] 管道已结束。
    # 而且这个错误发生的原因不确定，官方暂时没有修复， 如果你在测试中发现这个错误，那么可以使用 pytest-xdist 来进行并发测试。