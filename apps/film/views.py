from django.shortcuts import render
from apps.film.models import Setting , Movies
# Create your views here.


def index(request):
    home = Setting.objects.latest('id')
    movies = Movies.objects.all()
    context = {
        'home' : home,
        'movies' : movies,
    }
    return render(request,'index.html',context)