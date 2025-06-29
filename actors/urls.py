from actors.views import ActorsCreateListView, ActorsRetrieveUpdateDestroyView
from django.urls import path


urlpatterns = [
    path('actors/', ActorsCreateListView.as_view(), name='actors-create-list-view'),
    path('actors/<int:pk>/', ActorsRetrieveUpdateDestroyView.as_view(), name='actors-Retrieve-update-destroy-view'),
]
