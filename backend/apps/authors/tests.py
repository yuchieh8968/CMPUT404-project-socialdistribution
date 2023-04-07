from django.test import TestCase, Client
from apps.authors.models import MyUserManager, Author


c = Client()

# Create your tests here.


# Test authors
class Author_TestCase(TestCase):
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

    
    def test_get_nonexisting_author(self):
        """GET /authors/-1/ (trying to get a non-existant author should return a 404 code)"""
        response = c.get('/api/authors/-1/')
        self.assertEqual(response.status_code, 404)

    def test_get_all_authors(self):
        """GET /authors/ (get all authors should return a 200 code)"""
        response = c.get('/api/authors/')
        self.assertEqual(response.status_code, 200)

    def test_post_invalid_author(self):
        """POST /authors/ (trying to edit an invalid author should return a 400 code)"""
        # github and profile image needs to be a url
        response = c.post(f'/api/authors/{self.get_my_id()}/', {"displayName": "Team 24", "github": "not a url", "profileImage": "not a url"}, content_type="application/json")
        self.assertEqual(response.status_code, 400)

    def test_post_author(self):
        """POST /authors/ (updating a valid author should return a 200 code)"""
        response = c.post(f'/api/authors/{self.get_my_id()}/', {"displayName": "Team 24", "github": "http://google.ca", "profileImage": "http://google.ca"}, content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_get_author(self):
        """GET /authors/id/ (should return 200 code)"""
        response = c.get(f'/api/authors/{self.get_my_id()}/')
        self.assertEqual(response.status_code, 200)
