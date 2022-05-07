from django.db import models
from apps.categories.models import Category

# Create your models here.

class Movies(models.Model):
    title = models.CharField(max_length=255) 
    description =  models.TextField()
    picture = models.ImageField(upload_to = 'media/',blank = True, null = True)    
    GENRE_CHOICES = (
        ('Боевики', 'Боевики'),
        ('Комедии', 'Комедии'),
        ('Фантастика/фэнтези', 'Фантастика/фэнтези'),
        ('Мультфильмы', 'Мультфильмы'),
        ('Драма/мелодрама', 'Драма/мелодрама'),
        ('Ужасы', 'Ужасы'),
        ('Детектив/Триллеры', 'Детектив/Триллеры'),
        ('Документальные', 'Документальные'),
    )
    genre = models.CharField(choices=GENRE_CHOICES, default='Фантастика/Боевики', max_length=250)
    rating = models.IntegerField()
    slug = models.SlugField()
    release_date = models.DateField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='movie_category')
    movie_trailer = models.CharField(max_length=255)
    age_limit = models.CharField(max_length=250)
    film_genre = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"    



class MovieImage(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name="movie_image", null=True)
    movie_image = models.ImageField(upload_to = "movie_image/", null = True, blank = True)
    
    class Meta:
        verbose_name = "Картинка фильма"
        verbose_name_plural = "Картинки фильмов"


# class MovieComment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_movie")
#     movie = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name="movie_comment" )
#     message = models.TextField()
#     created = models.DateField(auto_now=True)        
