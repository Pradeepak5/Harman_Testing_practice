import unittest

class MyApp2(unittest.TestCase):
    def test_case3(self):
        self.assertEqual("hello","hello")
class MyApp(unittest.TestCase):
    def test_case1(self):
        a=0
        b=22
        c=a+b
        self.assertEqual(32,c)

    def test_case2(self):
        self.assertNotEqual("hello","hello")

if __name__=="__main__":
    unittest.main()