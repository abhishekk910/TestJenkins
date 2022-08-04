import unittest

class TestClass(unittest.TestCase):

    def test_func1(self):
        a = 10
        b = 10
        self.assertEqual(id(a), id(b)) 

    def test_func2(self):
        a = "100"
        b = 100
        self.assertEqual(int(a), b) 