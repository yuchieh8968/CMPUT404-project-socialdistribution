from rest_framework import serializers
from .models import Author
from django.conf import settings


class AuthorSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField('build_id')
    url = serializers.SerializerMethodField('build_id')
    host = serializers.URLField(default=settings.HOST, read_only=True)
    type = serializers.CharField(max_length=10, default="author", read_only=True)



    def build_id(self, author):
       host = settings.HOST
       return f"{host}/api/authors/{author.id}"


    

    class Meta:
        model = Author
        fields = ['type', 'id', 'url', 'host', 'displayName', 'github', 'profileImage']

