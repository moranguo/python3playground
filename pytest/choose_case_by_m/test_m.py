import pytest


# mark on class
@pytest.mark.samplea
class TestSampleA(object):
    def test_a_method1(self):
        assert 1 == 1

    def test_a_method2(self):
        assert 1 == 1


@pytest.mark.sampleb
class TestSampleB(object):
    def test_b_method1(self):
        assert 1 == 1

    def test_b_method2(self):
        assert 1 == 1


class TestSampleC(object):
    # mark on method
    @pytest.mark.samplea
    def test_c_method1(self):
        assert 1 == 1

    @pytest.mark.sampleb
    def test_c_method2(self):
        assert 1 == 1

    @pytest.mark.samplea
    @pytest.mark.sampleb
    def test_c_method3(self):
        assert 1 == 1

# 运行所有用例
# pytest -v
# choose case by mark
# pytest -v -m "samplea" test_m.py
# pytest -v -m "sampleb" test_m.py
# 不同标签之间的分割要使用and或者or关键字。
# 选择同时具有mark samplea和sampleb的case, 比如test_c_method3
# pytest -v -m "samplea and sampleb" test_m.py