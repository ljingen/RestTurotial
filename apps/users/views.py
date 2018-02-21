from django.contrib.auth import get_user_model
from rest_framework import generics,permissions
from .serializers import UserProfileSerializer
# Create your views here.
User = get_user_model()


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = "username"
