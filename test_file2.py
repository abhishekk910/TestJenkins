import unittest 

class TestList(unittest.TestCase):

    def test_list1(self):
        a = [1, 2, 3]
        b = [1, 2, 3]
        self.assertEqual(a, b) 

    def test_list2(self):
        a = [1, 2, 3] * 3
        b = [1, 2, 3, 1, 2, 3, 1, 2, 3]
        self.assertEqual(a, b) 