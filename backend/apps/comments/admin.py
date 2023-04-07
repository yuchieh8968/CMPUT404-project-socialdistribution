from django.contrib import admin
from .models import Comment
from django.conf import settings


class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ['url', 'id', 'get_author']

    def get_author(self, comment):
        return comment.author
    get_author.short_description = 'author_id'

    def url(self, comment):
        host = settings.HOST
        return f"{host}/api/authors/{comment.post.author.id}/posts/{comment.post.id}"


# Register your models here.
admin.site.register(Comment, CommentAdmin)
