import pytest


def test3(test_session):
    name = '男'
    print('找到name')
    assert test_session == name


if __name__ == '__main__':
    pytest.main(["-s", "-v", "fixture_scope_session_test1.py", "fixture_scope_session_test2.py"])
