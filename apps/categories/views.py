from django.shortcuts import render
from apps.categories.models import Category
from apps.film.models import Movies
from apps.settings.models import Setting
# Create your views here.

# def category_detail(request, slug):
#     category = Category.objects.get(slug = slug)
#     categories = Category.objects.all().order_by('?')[:5]
#     home = Setting.objects.latest('-id')
#     movies = Movies.objects.all().order_by('-id')
#     context = {
#         'category' : category,
#         'movies' : movies,
#         'home' : home,
#         'categories' : categories,
#     }
#     return render(request, 'movie-single.html', context)


  