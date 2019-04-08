from django.urls import path
from .views import ListUsersView, ListEntriesView, ListUserEntriesView, ListTransactionsView, EntriesView

urlpatterns = [
    path('users/', ListUsersView.as_view(), name="users-all"),
    path('entries/', ListEntriesView.as_view(), name="entries-all"),
    path('entries/<int:user_id>/<slug:drinktype>/<int:amount>/', EntriesView.as_view(), name="entries-create"),
    path(r'users/<int:user_id>/entries/', ListUserEntriesView.as_view(), name="user-entries"),
    path('transactions/', ListTransactionsView.as_view(), name="transactions-all"),
]
