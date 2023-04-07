from django.test import TestCase, Client

c = Client()

# Create your tests here.

# Test /docs/api/
class api_docs_TestCase(TestCase):
    def setUp(self) -> None:
        self.response = c.get('/api/docs/')
        return super().setUp()
    
    def test_api_docs_endpoint(self):
        """/api/docs/ returns a 200 code"""
        self.assertEqual(self.response.status_code, 200)


    def test_api_docs_content(self):
        """/api/docs/ contains swagger docs"""
        self.assertContains(self.response, "Swagger")
