from django.contrib import admin
# from apps.users.models import User

# # Register your models here.
# admin.site.register(User)
from apps.users.models import Ad , User_account_settings



admin.site.register(Ad)
admin.site.register(User_account_settings)

