from django.urls import path
from apps.film.views import index, movie_detail


urlpatterns = [
    path('', index, name = "index"),
    path('movie/<int:id>', movie_detail, name="movie_detail"),
]
