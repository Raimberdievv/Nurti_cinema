from tabnanny import verbose
from django.apps import AppConfig


class FilmConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.film'
    verbose_name  = "Фильмы"