from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from urllib.parse import quote
# Create your models here.

# https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#custom-users-admin-full-example
class MyUserManager(BaseUserManager):
    def create_user(self, id, url, host, displayName, password=None):
        """
        Creates and saves an Author with an id, url, host, displayName, and password
        """
        if not id:
            raise ValueError('Users must have an id')
        
        if not url:
            raise ValueError('Users must have a url')
        
        if not host:
            raise ValueError('Users must have a host')
        
        if not displayName:
            raise ValueError('Users must have a displayName')

        user = self.model(
            id = id,
            url=url,
            host=host,
            displayName=displayName,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, id, url, host, displayName, password=None):
        """
        Creates and saves a superuser with the given id, url, host, displayName, and password
        """
        user = self.create_user(
            id=id,
            url=url,
            host=host,
            displayName=displayName,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Author(AbstractBaseUser):
    id = models.URLField(primary_key=True, max_length=255, unique=True)
    url = models.URLField(max_length=255, blank=True, unique=True)
    host = models.URLField(max_length=200, blank=True)
    displayName = models.CharField(max_length=200, blank=False, null=False, unique=True, editable=True)
    github = models.URLField(max_length=255, blank=True, null=True)
    profileImage = models.URLField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()
    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['url', 'host', 'displayName']

    # def friendlist_template():
    #     return {"friend_id": "[]"}
    # friend_list = models.JSONField(blank=True, default=friendlist_template)

    def __str__(self):
        return self.id
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
    # def save(self, *args, **kwargs):
    #     if self._state.adding:
    #         self.id = quote(self.id, safe='')
    #         super(Author, self).save(*args, **kwargs)

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
    # def get_absolute_url(self):
    #     # return reverse('Single author', args=[str(self.id)])
    #     return self.url
    
    class Meta:
        ordering = ['displayName']
