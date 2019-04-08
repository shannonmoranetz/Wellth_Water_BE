from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Users, Entries, Transactions
from .serializers import UsersSerializer, EntriesSerializer, TransactionsSerializer


class ListUsersView(generics.ListAPIView):
    """
    Provides a get all users method handler.
    """
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class ListEntriesView(generics.ListAPIView):
    """
    Provides a get all entries method handler.
    """
    queryset = Entries.objects.all()
    serializer_class = EntriesSerializer

class EntriesView(APIView):
    """
    Provides a post entries method handler.
    """
    def post(self, request, version, user_id, drinktype, amount, format=None):
        entry = Entries.objects.create(user_id=user_id, drinktype=drinktype, amount=amount)
        entries_serializer = EntriesSerializer(entry)
        return Response(entries_serializer.data)

class ListUserEntriesView(APIView):
    """
    Provides a get all entries for specifc user method handler.
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
    Provides a get all Transactions method handler.
    """
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer
