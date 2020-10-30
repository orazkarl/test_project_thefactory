from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .models import Message
from .serializers import MessageCreateSerializer

class MessageCreateView(CreateAPIView):
    serializer_class = MessageCreateSerializer


