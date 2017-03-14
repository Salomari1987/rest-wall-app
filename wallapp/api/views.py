from rest_framework import generics
from api.serializers import MessageSerializer
from api.models import Message

class MessageView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new message."""
        serializer.save()
