from django.db import models
from apps.authors.models import Author
# from apps.posts.models import Post
# Create your models here.


# class Comment(models.Model):
#     MARKDOWN = 'text/markdown'
#     contentTypeChoices = [
#         (MARKDOWN, 'text/markdown'),
#     ]


#     id = models.CharField(primary_key=True, max_length=255)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     comment = models.CharField(max_length=280)
#     contentType = models.CharField(max_length=30, choices=contentTypeChoices, default=MARKDOWN)
#     published = models.DateTimeField(auto_now_add=True)


#     def get_comment_id(self):
#         return self.id

#     def __str__(self):
#         self.comment