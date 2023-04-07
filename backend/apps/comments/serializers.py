from rest_framework import serializers
from .models import Comment
from django.conf import settings


class CommentSerializer(serializers.ModelSerializer):
    type = serializers.CharField(
        max_length=10, default="comment", read_only=True)
    author = serializers.SerializerMethodField('build_author_id')
    id = serializers.SerializerMethodField('build_id')

    def build_author_id(self, comment):
        host = settings.HOST
        return f"{host}/api/authors/{str(comment.author)}"

    def build_id(self, comment):
        host = settings.HOST
        print(str(comment.post))
        return f"{host}/api/authors/{str(comment.author.id)}/posts/{str(comment.post.id)}/comments/{str(comment.id)}"

    class Meta:
        model = Comment
        fields = '__all__'

        read_only_fields = ['type', 'published']
        extra_kwargs = {
            'post': {'write_only': True}
        }


class CommentPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'author', 'comment',
                  'contentType', 'published', 'post']

        read_only_fields = ['published']
