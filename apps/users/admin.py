from django.contrib import admin
from apps.users.models import Ad , Account_settings ,User



class UserAdmin(admin.ModelAdmin):
    # fields = ('username', 'tel') #Вывести нужное поле
    # exclude = ('username',) #Исключить поле 
    list_display = ('username', 'email', 'tel')
    search_fields = ('username', 'email')
    ordering = ('username',)
    list_per_page = 10



admin.site.register(Ad)
admin.site.register(Account_settings)
admin.site.register(User, UserAdmin)
