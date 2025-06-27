from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateListView, GenreRetrieveDestroyView
from actors.views import ActorsCreateListView, ActorsRetrieveUpdateDestroyView
from movies.views import MovieCreateListView, MovieRetrieveUpdateDestroyView



urlpatterns = [
    path('admin/', admin.site.urls),

    path('genres/', GenreCreateListView.as_view(), name='genre-create-list-view'),
    path('genres/<int:pk>/', GenreRetrieveDestroyView.as_view(), name='genre-retrieve-update-destroy-view'),

    path('actors/', ActorsCreateListView.as_view(), name='actors-create-list-view'),
    path('actors/<int:pk>/', ActorsRetrieveUpdateDestroyView.as_view(), name='actor-retrieve-update-destroy-view'),

    path('movies/', MovieCreateListView.as_view(), name='movie-create-list-view'),
    path('movies/<int:pk>', MovieRetrieveUpdateDestroyView.as_view(), name='movie-retrieve-update-destroy-view'),
]
