import unittest
from run import app


class MyTestCase(unittest.TestCase):
    def test_one(self):
        tester = app.test_client(self)
        response = tester.get('/home', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Log In' in response.data)


if __name__ == '__main__':
    unittest.main()
