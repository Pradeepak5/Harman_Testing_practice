import unittest

def Login_chech(username,password):
    if username=="admin" and password=="1234":
        return True
    else:
        return False

class Login_check_app(unittest.TestCase):
    def test_login_page(self):
        username="admin"
        password="1234"
        result=Login_chech(username,password)
        self.assertTrue(result)

if __name__=="__main__":
    unittest.main()
