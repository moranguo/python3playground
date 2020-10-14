import pytest


@pytest.mark.toRun
class TestSampleD(object):
    def test_d_method1(self):
        assert 1 == 1

    @pytest.mark.notToRun
    def test_d_method2(self):
        assert 1 == 1


# 选中两个用例，test_d_method1 和 test_d_method2
# pytest -v -m "toRun" test_m2.py

# 选中一个用例，test_d_method2
# pytest -v -m "notToRun" test_m2.py
# pytest -v -m "toRun and notToRun" test_m2.py

# 选中一个用例，test_d_method1
# pytest -v -m "toRun and not notToRun" test_m2.py

# 没有选中的用例
# pytest -v -m "notToRun and not toRun" test_m2.py