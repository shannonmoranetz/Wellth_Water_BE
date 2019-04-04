from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Users
from .serializers import UsersSerializer
from .models import Entries
from .serializers import EntriesSerializer
from .serializers import UserEntriesSerializer


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


class ListUserEntriesView(APIView):
    """
    Provides a get method handler.
    """
    def get(self, request, version, user_id, format=None):
        user = Users.objects.get(id=user_id)
        entries = Entries.objects.filter(user_id=user_id)
        serializer = UserEntriesSerializer(user, many=False)
        return Response(serializer.data)

        # Consider Rendering into JSON from rest_framework.renderers import JSONRenderer
        # json = JSONRenderer().render(serializer.data)
        # json
