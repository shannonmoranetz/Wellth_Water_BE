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
from .models import Transactions
from .serializers import TransactionsSerializer


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

class EntriesView(APIView):
    """
    Provides a get method handler.
    """
    def post(self, request, version, user_id, drinktype, amount, format=None):
        # user = Users.objects.get(user_id=user_id)
        entry = Entries.objects.create(user_id=user_id, drinktype=drinktype, amount=amount)
        entries_serializer = EntriesSerializer(entry)
        return Response(entries_serializer.data)

class ListUserEntriesView(APIView):
    """
    Provides a get method handler.
    """
    def get(self, request, version, user_id, format=None):
        user = Users.objects.get(id=user_id)
        entries = Entries.objects.filter(user_id=user_id)
        entries_serializer = EntriesSerializer(entries, many=True)
        users_serializer = UsersSerializer(user)
        ret = users_serializer.data
        ret['entries'] = entries_serializer.data
        return Response(ret)

class ListTransactionsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer
