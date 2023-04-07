from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Comment
from apps.authors.models import Author
from apps.posts.models import Post
from .serializers import CommentSerializer, CommentPostSerializer
from .views import CommentView

c = Client()

# Create your tests here.


class CommentTestCases(TestCase):
    def setUp(self):
        return super().setUp

    def test_post_successful(self):
        response = c.post('/authors/', {"id": "bob"})
        response = c.post('/posts/', {"id": "somepost", "author_id": "bob"})
        response = c.post(
            '/comments/', {"id": "someComment", "author": "bob", "post": "somepost"})
        self.assertEqual(response, 201)

    def test_get_successful(self):
        response = c.post('/authors/', {"id": "bob"})
        response = c.post('/posts/', {"id": "somepost", "author_id": "bob"})
        response = c.post(
            '/comments/', {"id": "someComment", "author": "bob", "post": "somepost"})
        response = c.get('authors/bob/posts/somepost/comments/someComment')
        self.assertEqual(response.status_code, 200)

    def tests_get_invalid_author(self):
        response = c.get(f'/authors/-1/posts/somepost/comments')
        self.assertEqual(response.status_code, 404)

    def test_get_invalid_posts(self):
        response = c.get(f'/authors/bob/posts/-1/comments')
        self.assertEqual(response.status_code, 404)

    def test_get_invalid_comments(self):
        response = c.get(f'/authors/bob/posts/somepost/comments/-1/')
        self.assertEqual(response.status_code, 404)
