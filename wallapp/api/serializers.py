from rest_framework import serializers
from api.models import Message

class MessageSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Message
        fields = ('id', 'body', 'author', 'created_at', 'modified_at')
        read_only_fields = ('date_created', 'date_modified')
