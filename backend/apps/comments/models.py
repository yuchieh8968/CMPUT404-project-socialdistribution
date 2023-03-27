# from django.db import models
# from apps.authors.models import Author
# from apps.posts.models import Post
# # from apps.posts.models import Post
# # Create your models here.


# class Comment(models.Model):
#     MARKDOWN = 'text/markdown'
#     PLAIN = 'text/plain'
#     contentTypeChoices = [
#         (MARKDOWN, 'text/markdown'),
#         (PLAIN, 'text/plain'),
#     ]


#     id = models.URLField(primary_key=True, max_length=255, )
#     author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=False, null=False)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=False, null=False)
#     comment = models.CharField(max_length=280, blank=False, null=False)
#     contentType = models.CharField(max_length=30, choices=contentTypeChoices, default=PLAIN, blank=False, null=False)
#     published = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         self.comment