from django.urls import path
from apps.settings.views import about_us,movies,movie_single



urlpatterns = [
    path('about_us/',about_us,name="about_us"),
    path('movies/', movies, name="movies"),
    path('movie_single/', movie_single, name="movie_single"),
]
