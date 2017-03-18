from rest_framework import serializers
from api.models import Message
from django.contrib.auth.models import User

class MessageSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Message
        fields = ('id', 'body', 'author', 'created_at', 'modified_at')
        read_only_fields = ('date_created', 'date_modified')


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User(email=validated_data['email'], username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('password', 'first_name', 'last_name', 'email', 'username')
        write_only_fields = ('password',)
