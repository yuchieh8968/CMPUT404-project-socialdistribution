from django.db import models
from apps.authors.models import Author
from apps.posts.models import Post
import uuid
# Create your models here.


class Comment(models.Model):
    MARKDOWN = 'text/markdown'
    PLAIN = 'text/plain'
    contentTypeChoices = [
        (MARKDOWN, 'text/markdown'),
        (PLAIN, 'text/plain'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, to_field='id', on_delete=models.CASCADE)
    comment = models.CharField(max_length=280)
    contentType = models.CharField(max_length=30, choices=contentTypeChoices, default=PLAIN)
    published = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return str(self.comment)
