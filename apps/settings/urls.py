from django.urls import path
from apps.settings.views import about_us,movies,movie_single,login,sign_up



urlpatterns = [
    path('about_us/',about_us,name="about_us"),
    path('movies/', movies, name="movies"),
    path('movie_single/', movie_single, name="movie_single"),
    path('login/',login,name="login"),
    path('sign_up/',sign_up,name="sign_up"),
]
