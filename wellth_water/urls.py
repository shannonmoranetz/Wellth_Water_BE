from django.urls import path
from .views import ListUsersView
from .views import ListEntriesView
from .views import ListUserEntriesView


urlpatterns = [
    path('users/', ListUsersView.as_view(), name="users-all"),
    path('entries/', ListEntriesView.as_view(), name="entries-all"),
    path(r'users/entries/(P?<user_id>\d+)', ListUserEntriesView.as_view(), name="user-entries")
]
