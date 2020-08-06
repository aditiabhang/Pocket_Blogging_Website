import unittest
import os
import json
from pocket_blog import create_app, db
from pocket_blog.models import User, Post


class BasicBlogTests(unittest.TestCase):
    """This class represents the basicpocketblog test cases"""

    # executed prior to each test
    def setUp(self):
        self.app = create_app(config_class="testing")
        self.client = self.app.test_client
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

        resp = self.client().post(
            '/post/new', follow_redirects=False,
            data=self.new_post)
        self.assertEqual(resp.status_code, 302)

    def test_get_post(self):
        """Test API can get a created blog post (GET request)"""
        resp = self.client().get(
            '/home'
        )
        self.assertEqual(resp.status_code, 200)

    # def test_delete_post(self):

    #     resp1 = self.client().post(
    #         '/post/new', follow_redirects=True,
    #         data=self.new_post)

    #     resp2 = self.client().get(
    #         '/home')

    #     self.assertEqual(resp2.status_code, 200)

    #     resp3 = self.client().post(
    #         '/post/{}/delete'.format(resp2)
    #     )
    #     print("PRINT HERE: ", resp3.status_code)
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
