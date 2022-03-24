import unittest

def Largest_of_twonum(x,y):
    if x>y:
        return True
    else:
        return False

class Chech_Largest_of_num(unittest.TestCase):
    def test_largest_1(self):
        num1=10
        num2=20
        result=Largest_of_twonum(num1,num2)
        self.assertTrue(num2)

    def test_largest_2(self):
        num1 = 20
        num2 = 10
        result = Largest_of_twonum(num1, num2)
        self.assertTrue(num1)

if __name__ == "__main__":
        unittest.main()