from rest_framework import serializers
from rest_framework.fields import URLField, CharField
from .models import Inbox

class InboxSerializer(serializers.ModelSerializer):
    object = URLField(source='url')
    author = URLField(source = "sender")
    type = CharField(source = "contentType")

    class Meta:
        model = Inbox
        fields = ('author', "object",'type', 'summary')

    def build_id(self, inbox):
        print(str(inbox.sender)) 