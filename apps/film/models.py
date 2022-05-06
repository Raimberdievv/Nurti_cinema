from django.db import models

# Create your models here.

class Movies(models.Model):
    title = models.CharField(max_length=255) 
    description =  models.TextField()
    picture = models.ImageField(upload_to = 'media/')    
    release_date = models.DateField(auto_now=True)
    age_limit = models.CharField(max_length=250)
    film_genre = models.CharField(max_length=255)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"    



class popular_movies(models.Model):
    title = models.CharField(max_length=255)
    

