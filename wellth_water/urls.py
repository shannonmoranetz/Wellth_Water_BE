from django.urls import path
from .views import ListUsersView
from .views import ListEntriesView


urlpatterns = [
    path('users/', ListUsersView.as_view(), name="users-all"),
    path('entries/', ListEntriesView.as_view(), name="entries-all")
]
