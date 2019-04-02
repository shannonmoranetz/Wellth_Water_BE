from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Users
from .serializers import UsersSerializer
from .models import Entries
from .serializers import EntriesSerializer


class ListUsersView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class ListEntriesView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Entries.objects.all()
    serializer_class = EntriesSerializer
