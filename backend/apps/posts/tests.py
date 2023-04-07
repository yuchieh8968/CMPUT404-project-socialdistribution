from django.test import TestCase, Client
from apps.authors.models import Author
import uuid

c = Client()

# Create your tests here.

# Test posts
class Post_TestCase(TestCase):
    def setUp(self) -> None:
        username = 'team24'
        displayName = 'Team 24'
        password = 'team24'
        admin = Author.objects.create_superuser(username, 'Team 24', password)

        c.login(username = username, password = password)
        return super().setUp()
    
    def get_my_id(self):
        response = c.get("/api/utils/me/")
        d = dict(response.json())
        return d['id']

    
    def test_get_posts_valid_author(self):
        """GET /authors/id/posts/ (get posts from valid author should return 200 code)"""
        response = c.get(f'/api/authors/{self.get_my_id()}/posts/')
        self.assertEqual(response.status_code, 200)

    def test_get_invalid_post_valid_author(self):
        """GET /authors/id/posts/id (get invalid post from valid author should return 404 code)"""
        response = c.get(f'/api/authors/{self.get_my_id()}/posts/{self.get_my_id()}/')
        self.assertEqual(response.status_code, 404)

    def test_get_posts_no_posts(self):
        """GET /authors/id/posts/ (should return 200 code)"""
        response = c.get(f'/api/authors/{self.get_my_id()}/posts/')
        self.assertEqual(response.status_code, 200)

    def test_view_all_posts(self):
        """GET /posts/ (should return 200 code)"""
        response = c.get('/api/utils/posts/')
        self.assertEqual(response.status_code, 200)

    def test_create_post(self):
        """POST /posts/ (should return 201 code)"""
        response = c.post(f'/api/authors/{self.get_my_id()}/posts/', {
                                                                        "title": "string",
                                                                        "source": "string",
                                                                        "origin": "string",
                                                                        "description": "string",
                                                                        "contentType": "text/plain",
                                                                        "content": "string",
                                                                        "categories": [
                                                                            "string"
                                                                        ],
                                                                        "visibility": "PUBLIC",
                                                                        "unlisted": True
                                                                        }, content_type="application/json")
        self.assertEqual(response.status_code, 201)


    def test_create_invalid_post(self):
        """POST /posts/ (should return 400 code)"""
        response = c.post(f'/api/authors/{self.get_my_id()}/posts/', {
                                                                        "title": "",
                                                                        "source": "string",
                                                                        "origin": "string",
                                                                        "description": "string",
                                                                        "contentType": "text/plain",
                                                                        "content": "string",
                                                                        "categories": [
                                                                            "string"
                                                                        ],
                                                                        "visibility": "PUBLIC",
                                                                        "unlisted": "NOT A BOOL"
                                                                        }, content_type="application/json")
        self.assertEqual(response.status_code, 400)

    def test_put_invalid_post(self):
        """POST /posts/ (should return 400 code)"""
        response = c.put(f'/api/authors/{self.get_my_id()}/posts/{self.get_my_id()}/', {
                                                                        "title": "",
                                                                        "source": "string",
                                                                        "origin": "string",
                                                                        "description": "string",
                                                                        "contentType": "text/plain",
                                                                        "content": "string",
                                                                        "categories": [
                                                                            "string"
                                                                        ],
                                                                        "visibility": "PUBLIC",
                                                                        "unlisted": "NOT A BOOL"
                                                                        }, content_type="application/json")
        self.assertEqual(response.status_code, 400)

    def test_put_valid_post(self):
        """POST /posts/ (should return 201 code)"""
        response = c.put(f'/api/authors/{self.get_my_id()}/posts/{self.get_my_id()}/', {
                                                                        "title": "string",
                                                                        "source": "string",
                                                                        "origin": "string",
                                                                        "description": "string",
                                                                        "contentType": "text/plain",
                                                                        "content": "string",
                                                                        "categories": [
                                                                            "string"
                                                                        ],
                                                                        "visibility": "PUBLIC",
                                                                        "unlisted": True
                                                                        }, content_type="application/json")
        self.assertEqual(response.status_code, 201)


    def get_post_we_created(self):
        response = c.get(f'/api/authors/{self.get_my_id()}/posts/{self.get_my_id()}/')
        self.assertEqual(response.status_code, 200)

    def get_post_we_didnt_create(self):
        response = c.get(f'/api/authors/{self.get_my_id()}/posts/{str(uuid.uuid1())}/')
        self.assertEqual(response.status_code, 404)

