from arth import *
import unittest
class arthtest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(15,5),10)
    def test_sub(self):
        self.assertEqual(sub(10,5),5)
    def test_mul(self):
        self.assertEqual(mul(10,5),50)
if __name__=="__main__":
    unittest.main()