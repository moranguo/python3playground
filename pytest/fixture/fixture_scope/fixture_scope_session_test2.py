import pytest


class TestCase:
    def test4(self, test_session):
        sex = '男'
        print('找到sex')
        assert test_session == sex


if __name__ == '__main__':
    pass