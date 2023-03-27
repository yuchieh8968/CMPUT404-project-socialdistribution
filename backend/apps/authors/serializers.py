from rest_framework import serializers
from .models import Author

class AuthorSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField('build_id')
    url = serializers.SerializerMethodField('build_id')
    host = serializers.URLField(default="http://127.0.0.1:8000", read_only=True)
    type = serializers.CharField(max_length=10, default="author", read_only=True)



    def build_id(self, author):
       host = "http://127.0.0.1:8000"
       return f"{host}/api/authors/{author.id}"


    

    class Meta:
        model = Author
        fields = ['type', 'id', 'url', 'host', 'displayName', 'github', 'profileImage']

