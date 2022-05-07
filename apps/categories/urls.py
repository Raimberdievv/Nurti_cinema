from django.urls import path
from apps.categories.views import category_detail


urlpatterns = [
    path('category_detail', category_detail, name = "category_detail"),
]