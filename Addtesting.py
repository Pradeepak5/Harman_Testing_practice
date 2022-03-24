import unittest

def add(x,y):
    return x+y

class Myapp(unittest.TestCase):
    def test_add(self):
        a=12
        b=23
        c=add(a,b)
        self.assertEqual(a+b,c)

    def test_add1(self):
        a = 13.35
        b = 1
        c = add(a, b)
        self.assertEqual(a + b, c)

    def test_add2(self):
        a = -12
        b = 1
        c = add(a, b)
        self.assertEqual(a + b, c)


if __name__ == "__main__":
        unittest.main()