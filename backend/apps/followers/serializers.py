from rest_framework import serializers
from .models import Follow
from django.conf import settings


class FollowSerializer(serializers.ModelSerializer):
    type = serializers.CharField(
        max_length=10, default="Follow", read_only=True)
    summary = serializers.SerializerMethodField('summary')
    actor = serializers.SerializerMethodField('build_author_id')

    def summary(self, follow):
        return f"{follow.author.displayName} wants to follow you."

    def build_author_it(self, follow):
        host = settings.HOST
        return f"{host}/api/authors/{str(follow.author.id)}"

    class Meta:
        model = Follow
        fields = '__all__'


# class FollowersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Author_Follows
#         fields = ("id", "author_id", "created")
