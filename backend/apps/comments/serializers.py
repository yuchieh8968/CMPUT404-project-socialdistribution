from rest_framework import serializers
from .models import Comment
from django.conf import settings


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField('build_id')
    type = serializers.CharField(max_length=10, default="comment", read_only=True)
    author = serializers.SerializerMethodField('build_author_id')


    def build_author_id(self, comment):
        host = settings.HOST
        return f"{host}/api/authors/{str(comment.author)}"

    def build_id(self, comment):
       host = settings.HOST
       return f"{host}/api/authors/{str(comment.author)}/posts/{str(comment.post)}/comments/{str(comment.id)}"

    class Meta:
        model = Comment
        fields = '__all__'
