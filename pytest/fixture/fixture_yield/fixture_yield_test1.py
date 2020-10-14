import pytest


@pytest.fixture(scope="module")
def open_browser():
    print("\n打开浏览器，并且打开百度首页")
    # 如果在setup就异常了，那么是不会去执行yield后面的teardown内容了
    wd = "driver"
    # fixture里面的teardown用yield来唤醒teardown的执行, yield后面的参数还可以传递出来
    yield wd
    print("\n执行teardown!")
    print("关闭浏览器")


def test_s1(open_browser):
    print("用例1：搜索python-1")
    assert "driver" == open_browser
    # 如果第一个用例异常了，不影响其他的用例执行
    raise NameError  # 模拟异常


def test_s2(open_browser):
    print("用例2：搜索python-2")
    assert "driver" == open_browser


def test_s3(open_browser):
    assert "driver" == open_browser
    print("用例3：搜索python-3")


# 如果test_s1不调用,test_s2（调用open）,test_s3不调用，运行顺序会是怎样的？
# module级别的fixture在当前.py模块里，只会在用例（test_s2）第一次调用前执行一次
if __name__ == "__main__":
    pytest.main(["-s", "-v", "fixture_yield_test1.py"])
