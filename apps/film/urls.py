from django.urls import path
from apps.film.views import movie_detail


urlpatterns = [
    path('movie/<int:id>',movie_detail,name="movie_detail"),
]
