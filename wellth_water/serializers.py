from rest_framework import serializers
from .models import Users
from .models import Entries
from .models import Transactions


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ("id", "name", "email")

class EntriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entries
        fields = ("user_id", "drinktype", "amount", "created_at")

class UserEntriesSerializer(serializers.Serializer):
     entries = EntriesSerializer(many=True)

class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ("id", "amount")
