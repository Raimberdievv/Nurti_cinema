from django.urls import path 
from apps.users.views import ad , account_settings
# from apps.users.views import sign_up,login


# urlpatterns = [
#     path('sign_up/', sign_up, name = "sign_up"),
#     path('login/',login, name = "login"),
# ]


urlpatterns = [
    path('ad/',ad, name = "ad"),
    path('account_settings/',account_settings, name = "account_settings"),
]