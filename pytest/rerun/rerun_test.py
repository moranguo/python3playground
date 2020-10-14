import pytest


class TestSample(object):
    def test_equal(self):
        # 在这里，让这个case失败，来演示re-run
        assert 1 == 0

    def test_not_equal(self):
        assert 1 != 0


if __name__ == "__main__":
    # pip install -U pytest-rerunfailures
    pytest.main(["-s", "-v", "rerun_test.py", "--reruns", "2"])
