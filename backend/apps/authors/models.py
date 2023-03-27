from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from urllib.parse import quote
import uuid
# Create your models here.

# class AllowedRemotes(models.Model):
#     username = models.CharField(primary_key=True, max_length=10, unique=True)
#     password = models.CharField(max_length=10, blank=False, null= False)

# https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#custom-users-admin-full-example
class MyUserManager(BaseUserManager):
    def create_user(self, username, displayName, password=None):
        """
        Creates and saves an Author with an id, url, host, displayName, and password
        """
        if not username:
            raise ValueError('Users must have a username')
        
        if not displayName:
            raise ValueError('Users must have a displayName')

        user = self.model(
            username = username,
            displayName=displayName,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, displayName, password=None):
        """
        Creates and saves a superuser with the given id, url, host, displayName, and password
        """
        user = self.create_user(
            username=username,
            displayName=displayName,
            password=password,
        )

        
        user.is_admin = True
        user.save(using=self._db)
        return user


class Author(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    username = models.CharField(max_length=20, blank=False, null=False, unique=True)
    displayName = models.CharField(max_length=20, blank=False, null=False)
    github = models.URLField(max_length=255, blank=True, null=True)
    profileImage = models.URLField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['displayName']

    # def friendlist_template():
    #     return {"friend_id": "[]"}
    # friend_list = models.JSONField(blank=True, default=friendlist_template)

    def __str__(self):
        return str(self.id)
    
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
