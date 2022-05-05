from distutils.command.upload import upload
from django.db import models


# Create your models here.

class Setting(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    logo = models.ImageField(upload_to = 'logo')
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


class About_us(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    our_statistics = models.IntegerField()
     


class Team(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    team_image = models.ImageField(upload_to = 'media')     



class Ad(models.Model):
    title = models.CharField(max_length=255)          



class Login(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()



class Sign_up(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    tel = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to = "media")
    email = models.EmailField()

  
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"