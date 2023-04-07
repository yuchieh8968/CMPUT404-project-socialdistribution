from django.contrib import admin
from .models import Post
from django.conf import settings

# https://stackoverflow.com/questions/163823/can-list-display-in-a-django-modeladmin-display-attributes-of-foreignkey-field
class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ['title', 'url', 'id', 'get_author']

    def get_author(self, post):
        return post.author.id
    get_author.short_description = 'author_id'

    def url(self, post):
       host = settings.HOST
       return f"{host}/api/authors/{post.author.id}/posts/{post.id}"



# Register your models here.
admin.site.register(Post, PostAdmin)

