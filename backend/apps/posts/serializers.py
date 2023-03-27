from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField('build_id')
    type = serializers.CharField(max_length=10, default="post", read_only=True)
    author = serializers.SerializerMethodField('build_author_id')


    def build_author_id(self, post):
        host = "http://127.0.0.1:8000"
        return f"{host}/api/authors/{post.author_id}"

    def build_id(self, post):
       host = "http://127.0.0.1:8000"
       return f"{host}/api/authors/{post.author_id}/posts/{post.id}"

    class Meta:
        model = Post
        fields = '__all__'
