from django.test import TestCase


from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Users
from .serializers import UsersSerializer
from .models import Entries
from .serializers import EntriesSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_user(name="", email=""):
        if name != "" and email != "":
            Users.objects.create(name=name, email=email)

    def create_entry(amount="", type=""):
        if amount != "" and type != "":
            Users.objects.create(amount=amount, type=type)
            import code; code.interact(local=dict(globals(), **locals()))


    def setUp(self):
        # add test data
        self.create_user("bob", "bob@gmail.com")
        self.create_user("bobo", "bobo@gmail.com")
        self.create_user("bobby", "bobby@gmail.com")





class GetAllUsersTest(BaseViewTest):

    def test_get_all_users(self):
        response = self.client.get(
            reverse("users-all", kwargs={"version": "v1"})
        )
        expected = Users.objects.all()
        serialized = UsersSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetAllEntriesTest(BaseViewTest):

    def test_get_all_entries(self):

        response = self.client.get(
            reverse("entries-all", kwargs={"version": "v1"})
        )
        expected = Entries.objects.all()
        serialized = EntriesSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
