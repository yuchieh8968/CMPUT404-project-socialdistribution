from django.db import models
from django.urls import reverse

from apps.authors.models import Author
from django.contrib.postgres.fields import ArrayField
# Create your models here.


# class Post(models.Model):

#     # Fields
#     id = models.CharField(primary_key=True, max_length=255, unique=True)
#     title = models.CharField(max_length=250, blank=True)
#     source = models.CharField(max_length=50, blank=True)
#     origin = models.CharField(max_length=50, blank=True)
#     description = models.CharField(max_length=250, blank=True)

#     CONTENT_CHOICES = (
#         ("text/plain", "text/plain"),
#         ("text/markdown", "text/markdown"),
#         ("application/base64", "application/base64"),
#         ("image/png;base64", "image/png;base64"),
#         ("image/jpeg;base64", "image/jpeg;base64")
#     )
#     contentType = models.CharField(
#         choices=CONTENT_CHOICES, max_length=20, default="text/plain")
    
#     content = models.CharField(max_length=1000, blank=True)
    
#     author_id = models.ForeignKey(Author, on_delete=models.CASCADE)

#     categories = ArrayField(models.CharField(max_length=20, blank=True))

#     # count = models.PositiveBigIntegerField(default=0)
#     published = models.DateTimeField(auto_now_add=True)
#     VISIBIILTY_CHOICES = (
#         ("PUBLIC", "PUBLIC"),
#         ("PRIVATE", "PRIVATE"),
#     )
#     visibility = models.CharField(max_length=10, choices=VISIBIILTY_CHOICES, default="PUBLIC")
    
#     unlisted = models.BooleanField(blank=True, default=False)

#     def __str__(self):
#         return self.title
    
#     class Meta:
#         ordering = ['published']
