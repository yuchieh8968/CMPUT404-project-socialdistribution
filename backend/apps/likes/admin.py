from django.contrib import admin
from .models import Like


class LikeAdmin(admin.ModelAdmin):
    model = Like
    list_display = ['id', 'author', 'object']

    def get_author(self, like):
        return like.author
    get_author.short_description = 'author_id'


# Register your models here.
admin.site.register(Like, LikeAdmin)