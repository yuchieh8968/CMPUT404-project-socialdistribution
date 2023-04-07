from rest_framework import serializers
from .models import Post
from django.conf import settings


class PostSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField('build_id')
    type = serializers.CharField(max_length=10, default="post", read_only=True)
    author = serializers.SerializerMethodField('build_author_id')


    def build_author_id(self, post):
        host = settings.HOST
        return f"{host}/api/authors/{str(post.author)}"

    def build_id(self, post):
       host = settings.HOST
       return f"{host}/api/authors/{str(post.author)}/posts/{str(post.id)}"

    class Meta:
        model = Post
        fields = '__all__'
