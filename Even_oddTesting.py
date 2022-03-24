import unittest

def check_even_odd(x):
    if x%2==0:
        return "even"
    else:
        return "odd"

class My_Even_or_odd_app(unittest.TestCase):
    def test_case_even(self):
        result = check_even_odd(2)
        self.assertEqual("even",result)

    def test_case_odd(self):
        result = check_even_odd(5)
        self.assertNotEqual("even",result)

if __name__ == "__main__":
        unittest.main()