from django.urls import path
from apps.settings.views import about_us,movies,movie_single,login,sign_up,watch_movie,contact



urlpatterns = [
    path('about_us/',about_us,name="about_us"),
    path('movies/', movies, name="movies"),
    path('login/',login,name="login"),
    path('sign_up/',sign_up,name="sign_up"),
    path('watch_movie/',watch_movie,name="watch_movie"),
    path('contact/',contact,name="contact"),
    path('movie_single/',movie_single,name="movie_single"),
]
