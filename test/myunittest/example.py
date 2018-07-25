import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

# python example.py
# python example.py -v
# The unittest module can be used from the command line to run tests from modules, classes or even individual test methods
# python -m unittest example.py
# python -m unittest example.TestStringMethods
# python -m unittest example.TestStringMethods.test_upper
# python -m unittest example.py -v
if __name__ == '__main__':
    unittest.main()