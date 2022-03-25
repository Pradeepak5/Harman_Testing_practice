import unittest

def myList():
    list=[1,3,5,"pradeep"]
    return list
class Checklist(unittest.TestCase):
    def test_list_present(self):
        element=5
        self.assertIn(element,myList())

    def test_list_not_present(self):
        element=2
        self.assertNotIn(element,myList())

if __name__=="__main__":
    unittest.main()