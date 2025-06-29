from django.urls import path
from genres.views import GenreCreateListView, GenreRetrieveUpdateDestroyView

urlpatterns = [
    path('genres/', GenreCreateListView.as_view(), name='genre-create-list-view'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genre-retrieve-update-destroy-view'),
]