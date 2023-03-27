from rest_framework import serializers
from .models import Author_Follows


class FollowingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author_Follows
        fields = ("id", "following_author_id", "created")


class FollowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author_Follows
        fields = ("id", "author_id", "created")