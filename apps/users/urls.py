from django.urls import path 
from apps.users.views import ad , account_settings
from apps.users.views import sign_up,login,user_profile,update_profile,delete_profile


urlpatterns = [
    path('sign_up/', sign_up, name = "sign_up"),
    path('login/',login, name = "login"),
    path('ad/',ad, name = "ad"),
    path('account_settings/',account_settings, name = "account_settings"),
    path('user/<int:id>/',user_profile, name = "user_profile"),
    path('user/update/<int:id>/',update_profile, name = "update_profile"),
    path('user/delete/<int:id>/',delete_profile, name = "delete_profile"),
]



