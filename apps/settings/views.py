from django.shortcuts import render
# from apps.settings.models import  Setting,Login,Sign_up
from apps.film.models import  Movies 
from django.shortcuts import render
from apps.settings.models import  Setting



# Create your views here.
def index(request):
    home = Setting.objects.latest('id')
    movies = Movies.objects.all().order_by('id')[:8]
    context = {
        'home' : home,
        'movies' : movies,
    }
    return render(request,'index.html',context)


def about_us(request):
    home = Setting.objects.latest('id')
    context = {
        'home' : home,
    }
    return render(request, 'about.html',context) 
    
def movies(request):
    home = Setting.objects.latest('id')
    context = {
        'home' : home,
    }
    return render(request, 'movies.html',context) 



def movie_single(request):
    home = Setting.objects.latest('id')
    context = {
        'home' : home,
    }
    return render(request, 'movie_single.html',context)   


def login(request):
    home = Setting.objects.latest('id')
    context = {
        'home' : home,
    }
    return render(request, 'login.html',context)



def sign_up(request):
    home = Setting.objects.latest('id')
    context = {
        'home' : home,
    }
    return render(request, 'sign_up.html',context) 
    


def watch_movie(request):
    home = Setting.objects.latest('id')
    movies = Movies.objects.all().order_by('id')[:8]
    context = {
        'home' : home,
        'movies' : movies,
    }
    return render(request, 'watch_movie.html',context) 

  

def contact(request):
    home = Setting.objects.latest('id')
    context = {
        'home' : home,
    }
    return render(request, 'contacts.html',context)