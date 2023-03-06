from django.test import TestCase, Client

c = Client()

# Create your tests here.

# Test posts
class Post_TestCase(TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    def test_get_posts_invalid_author(self):
        """GET /authors/-1/posts/ (get posts from invalid author should return 404 code)"""
        response = c.get(f'/authors/-1/posts/')
        self.assertEqual(response.status_code, 404)

    def test_get_invalid_post_invalid_author(self):
        """GET /authors/-1/posts/-1 (get invalid post from invalid author should return 404 code)"""
        response = c.get('/authors/-1/posts/-1')
        self.assertEqual(response.status_code, 404)

    def test_get_posts_no_posts(self):
        """GET /authors/bob/posts/ (should return 404 code)"""
        response = c.post('/authors/', {"id": "bob"})
        response = c.get('/authors/bob/posts/')
        self.assertEqual(response.status_code, 404)

    def test_view_all_posts(self):
        """GET /posts/ (should return 200 code)"""
        response = c.get('/posts/')
        self.assertEqual(response.status_code, 200)

    def test_create_post(self):
        """POST /posts/ (should return 201 code)"""
        response = c.post('/authors/', {"id": "bob"})
        response = c.post('/posts/', {"id": "somepost", "author_id": "bob"})
        self.assertEqual(response.status_code, 201)

    def test_view_post_after_creating(self):
        """GET /authors/bob/posts/somepost (should return 200 code)"""
        response = c.post('/authors/', {"id": "bob"})
        response = c.post('/posts/', {"id": "somepost", "author_id": "bob"})
        response = c.get('/authors/bob/posts/somepost')
        self.assertEqual(response.status_code, 200)

    def test_view_all_author_posts_after_creating(self):
        """GET /authors/bob/posts/ (should return 200 code)"""
        response = c.post('/authors/', {"id": "bob"})
        response = c.post('/posts/', {"id": "somepost", "author_id": "bob"})
        response = c.get('/authors/bob/posts/')
        self.assertEqual(response.status_code, 200)
