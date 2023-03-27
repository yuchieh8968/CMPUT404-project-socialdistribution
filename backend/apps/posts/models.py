from django.db import models
from django.urls import reverse

from apps.authors.models import Author
from django.contrib.postgres.fields import ArrayField
from urllib.parse import quote
import uuid
# Create your models here.


class Post(models.Model):

    # Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=256, blank=False, null=False)
    source = models.CharField(max_length=256, blank=True, null=True)
    origin = models.CharField(max_length=256, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)

    CONTENT_CHOICES = (
        ("text/plain", "text/plain"),
        ("text/markdown", "text/markdown"),
        ("application/base64", "application/base64"),
        ("image/png;base64", "image/png;base64"),
        ("image/jpeg;base64", "image/jpeg;base64")
    )
    contentType = models.CharField(
        choices=CONTENT_CHOICES, max_length=20, default="text/plain")
    
    content = models.CharField(max_length=1000, blank=False, null=False)
    
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    categories = ArrayField(models.CharField(max_length=20, blank=True), blank=True)

    # count = models.PositiveBigIntegerField(default=0)
    published = models.DateTimeField(auto_now_add=True)
    VISIBIILTY_CHOICES = (
        ("PUBLIC", "PUBLIC"),
        ("PRIVATE", "PRIVATE"),
    )
    visibility = models.CharField(max_length=10, choices=VISIBIILTY_CHOICES, default="PUBLIC")
    
    unlisted = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return self.title
    
    # def save(self, *args, **kwargs):
    #     if self._state.adding:
    #         self.id = quote(self.id, safe='')
    #         super(Post, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ['published']
