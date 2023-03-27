from rest_framework import serializers
from rest_framework.fields import URLField
from .models import Inbox

class InboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inbox
        fields = ('id','source','origin', 'contentType','author_id')