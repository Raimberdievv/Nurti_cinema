from distutils.command.upload import upload
from django.db import models
# from distutils.command.upload import upload
# from tabnanny import verbose
# from django.db import models
from django.contrib.auth.models import AbstractUser
# # Create your models here.



class User(AbstractUser):
    tel = models.CharField(max_length=255, default="0", blank=True, null=True)
    profile_image = models.ImageField(upload_to = "image/", blank=True, null=True)

    def __str__(self):
        return self.username 

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"





class Ad(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(null=True)
    img1 = models.ImageField(max_length=255, null=True, blank=True, upload_to="images/")
    video = models.FileField(upload_to="videos/", null=True, blank=True)
    target_url = models.URLField(max_length=200, null=True)
    # owner = models.ForeignKey(on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        return self.title



class Account_settings(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    profile_logo = models.ImageField(upload_to="images/")
    email = models.EmailField()
    old_password = models.CharField(max_length=255)
    new_password = models.CharField(max_length=255)
    date_of_birth = models.IntegerField()
    gender = models.CharField(max_length=255)
    language = models.CharField(max_length=255)


    def __str__(self):
        return self.name