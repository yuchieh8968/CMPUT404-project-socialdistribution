from rest_framework import serializers
from .models import Like
from django.conf import settings


class LikeSerializer(serializers.ModelSerializer):
    type = serializers.CharField(max_length=10, default="Like", read_only=True)
    author = serializers.SerializerMethodField('build_id')


    def build_id(self, like):
       host = settings.HOST
       return f"{host}/api/authors/{like.author.id}"
    
    class Meta:
        model = Like
        fields = '__all__'