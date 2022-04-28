from django.db import models

# Create your models here.

class Setting(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    logo = models.ImageField(upload_to = 'logo/')
    tel = models.CharField(max_length=255)
    email = models.EmailField()
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)


    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"



class Movies(models.Model):
    title = models.CharField(max_length=255) 
    description =  models.TextField()
    picture = models.ImageField(upload_to = 'media/logo/')    
    release_date = models.DateField(auto_now=True)
    age_limit = models.CharField(max_length=250)
    film_genre = models.CharField(max_length=255)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"    