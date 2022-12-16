from .serializer import Serializer
from .models import Messages
from rest_framework.response import Response
from rest_framework import viewsets
from .serializer import Serializer
# Create your views here.

class MessagesViewSet(viewsets.ModelViewSet):
    serializer_class = Serializer
    queryset = Messages.objects.all()



