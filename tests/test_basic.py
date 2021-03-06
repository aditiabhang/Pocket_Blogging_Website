import unittest
from pocket_blog import create_app, db


class BasicBlogTests(unittest.TestCase):
    """This class represents the basicpocketblog test cases"""

    # executed prior to each test
    def setUp(self):
        self.app = create_app(config_class="testing")
        self.client = self.app.test_client
        self.create_new_user = {"username": "testuser", "email": "testuser@test.com", "password": "fakepassword"}
        self.new_post = {"title": "testing post", "content": "This is a test blog"}

        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.session.close()
            db.drop_all()
            db.create_all()

    def register_user(self, username="testuser", email="user@test.com", password="test1234"):
        user_data = {
            'username': username,
            'email': email,
            'password': password
        }
        return self.client().post('/register', data=user_data)

    def login_user(self, email="user@test.com", password="test1234"):
        user_data = {
            'email': email,
            'password': password
        }
        return self.client().post('/login', data=user_data)

    def test_create_post(self):
        """Test API can create a blog post (POST request)"""
        self.register_user()
        result = self.login_user()

        resp = self.client().post(
            '/post/new', follow_redirects=True,
            data=self.new_post)
        self.assertEqual(resp.status_code, 200)

    def test_get_post(self):
        self.register_user()
        result = self.login_user()

        resp = self.client().get(
            '/home'
        )
        self.assertEqual(resp.status_code, 200)

    # def test_delete_post(self):
    #     # self.register_user()
    #     # result = self.login_user()
    #     resp1 = self.client().post(
    #         '/post/new', follow_redirects=True,
    #         data=self.new_post)
    #     # self.assertEqual(resp.status_code, 200)
    #     # print("POST RESP IN DELETE: ", resp1.json())
    #
    #     resp2 = self.client().get(
    #         '/home'
    #     )
    #     self.assertEqual(resp2.status_code, 200)
    #
    #     resp3 = self.client().post(
    #         '/post/{}/delete'.format(resp2)
    #     )
    #     # print("PRINT HERE: ", resp3.status_code.json())
    #     self.assertEqual(resp3.status_code, 200)

    # executed after each test
    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()


if __name__ == "__main__":
    unittest.main()
