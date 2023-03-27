from django.contrib import admin
from .models import Post

# https://stackoverflow.com/questions/163823/can-list-display-in-a-django-modeladmin-display-attributes-of-foreignkey-field
class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ['title', 'id', 'get_author']

    def get_author(self, obj):
        return obj.author_id
    get_author.short_description = 'author_id'



# Register your models here.
admin.site.register(Post, PostAdmin)

