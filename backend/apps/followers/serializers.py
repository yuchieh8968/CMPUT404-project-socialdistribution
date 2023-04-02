from rest_framework import serializers
from .models import Follow
from django.conf import settings
from rest_framework.fields import URLField, CharField, UUIDField



class FollowSerializer(serializers.ModelSerializer):
    type = CharField(max_length=10, default="Follow", read_only=True)

    def build_author_id(self, follow):
        host = settings.HOST
        return f"{host}/api/authors/{str(follow.author.id)}"

    class Meta:
        model = Follow
        fields = ('type', 'object', 'actor')



# class FollowersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Author_Follows
#         fields = ("id", "author_id", "created")
