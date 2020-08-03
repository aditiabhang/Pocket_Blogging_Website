import unittest
from run import app


class MyTestCase(unittest.TestCase):
    # ensuring the flask app is set up
    def test_one(self):
        tester = app.test_client(self)
        response = tester.get('/home', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # ensuring login page loads correctly
    def test_login_page(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Log In' in response.data)

    # ensuring that the login page behaves correctly given the correct credentials
    def test_login_correct(self):
        tester = app.test_client(self)
        response = tester.post('/login',
                               data=dict(email='tomthecat@gmail.com', password='password'),
                               follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # ensuring login page loads correctly
    def test_logout_page(self):
        tester = app.test_client(self)
        tester.post('/login',
                    data=dict(email='tomthecat@gmail.com', password='password'),
                    follow_redirects=True)
        response = tester.get('/home', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # ensuring correct user updates posts
    def test_post_edit(self):
        tester = app.test_client(self)
        response = tester.get('/post/19/update HTTP/1.1', follow_redirects=True)
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
