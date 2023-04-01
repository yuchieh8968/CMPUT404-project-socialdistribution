from rest_framework import serializers
from .models import Follow
from django.conf import settings
from rest_framework.fields import URLField, CharField



class FollowSerializer(serializers.ModelSerializer):
    type = serializers.CharField(max_length=10, default="Follow", read_only=True)
    author_id = serializers.UUIDField(source = "actor")

    def summary(self, follow):
        return f"{follow.author.displayName} wants to follow you."

    def build_author_id(self, follow):
        host = settings.HOST
        return f"{host}/api/authors/{str(follow.author.id)}"

    class Meta:
        model = Follow
        fields = ('type', 'object', 'author_id')



# class FollowersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Author_Follows
#         fields = ("id", "author_id", "created")
