from rest_framework import generics
from api.serializers import MessageSerializer
from api.models import Message
from rest_framework import permissions

class MessageView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        """Save the post data when creating a new message."""
        serializer.save(author=self.request.user)
