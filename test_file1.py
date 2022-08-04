import unittest

class TestString(unittest.TestCase):

    def test_string1(self):
        a = "hello world"
        b = "Hello World"
        self.assertEqual(a, b.lower())

    def test_string2(self):
        a = "Python"
        b = "PYTHON"
        self.assertEqual(a.upper(), b)

    