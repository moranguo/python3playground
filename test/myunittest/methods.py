import unittest
import logging
from testdata import Point


class Number():
    def __init__(self, num):
        self.num = num

class TestUTMethods(unittest.TestCase):
    def test_001assert_logs(self):
        with self.assertLogs('foo', level='INFO') as cm:
            logging.getLogger('foo').info('first message')
            logging.getLogger('foo.bar').error('second message')
        self.assertEqual(cm.output, ['INFO:foo:first message',
                                     'ERROR:foo.bar:second message'])

    def test_002assert_count_equal(self):
        a = [1, 2, 3, 4, 1]
        b = [3, 4, 2, 1, 1]
        self.assertCountEqual(a, b, msg='the count of elements is not equal')

    def test_003list_equal(self):
        a = [1, 2]
        b = [1, 2]
        #
        self.assertListEqual(a, b)

    def test_004object_equal(self):
        a = Point(1, 2)
        b = Point(1, 2)
        self.assertEqual(a, b)

    def test_005object_equal_func(self):
        a = Number(10)
        b = Number(11)

        def compare_number(x, y, msg=None):
            if x.num == y.num:
                return True
            else:
                raise unittest.TestCase.failureException(msg)
        self.addTypeEqualityFunc(Number, compare_number)
        self.assertEqual(a, b, msg="a is not equal to b")


if __name__ == "__main__":
    unittest.main(verbosity=2)
