from django.db import models
from apps.authors.models import Author
import uuid

# # Create your models here.

# class Like(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=False, null=False)
#     obj = models.URLField(max_length=255, blank=False, null=False)



class Like(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=False, blank=False)
    object = models.URLField(blank=False)


