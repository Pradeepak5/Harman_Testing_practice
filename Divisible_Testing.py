import unittest

def Divisible_or_not(x):
    if x%7==0:
        return True
    else:
        return False

class CheckDivisible(unittest.TestCase):
    def test_Divisible(self):
        result=Divisible_or_not(14)
        self.assertTrue(result)

    def test_Divisible1(self):
        result=Divisible_or_not(13)
        self.assertFalse(result)

if __name__ == "__main__":
        unittest.main()