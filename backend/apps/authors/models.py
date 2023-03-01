from django.db import models
from django.urls import reverse
# Create your models here.


class Author(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
