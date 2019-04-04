from rest_framework import serializers
from .models import Users
from .models import Entries


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ("name", "email")

class EntriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entries
        fields = ("type", "amount")

class UserEntriesSerializer(serializers.Serializer):
     def to_representation(self, instance):
         ret = {}
         ret['id'] = instance.id
         entries = Entries.objects.filter(user_id=instance.id)
         ret['entries'] = EntriesSerializer(entries).data
         import pdb; pdb.set_trace()
         return ret
