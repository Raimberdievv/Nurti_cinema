from django.shortcuts import render
from apps.film.models import  Movies
from django.shortcuts import render
from apps.film.models import Movies
# Create your views here.


def index(request):
    movies = Movies.objects.all()
    context = {
        'movies' : movies,
    }
    return render(request,'index.html',context)



def movie_detail(request, id):
    movie = Movies.objects.get(id = id)
    context = {
        'movie' : movie,
    }
    return render(request, 'watch_movie.html', context)



