from django.shortcuts import render
from apps.settings.models import Setting
# from apps.users.models import User_account_settings
# from django.shortcuts import render, redirect
# from apps.users.forms import UserRegistrationForm, LoginForm
# from apps.settings.models import Setting
# from django.contrib.auth import authenticate, login
# from django.http import HttpResponse
# from apps.settings.models import Setting



# # Create your views here.
# def sign_up(request):
#     if request.method == 'POST':
#         user_form = UserRegistrationForm(request.POST)
#         if user_form.is_valid():
#             # Create a new user object but avoid saving it yet
#             new_user = user_form.save(commit=False)
#             # Set the chosen password
#             new_user.set_password(user_form.cleaned_data['password'])
#             # Save the User object
#             new_user.save()
#             return redirect('index')
#     else:
#         user_form = UserRegistrationForm()
#     return render(request, 'sign_up.html', {'user_form': user_form})

# def login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(username=cd['username'], password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return redirect('index')
#                 else:
#                     return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse('Invalid login')
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form})



def ad(request):
    home = Setting.objects.latest('id')
    context = {
        'home' : home,
    }
    return render(request, 'ad.html',context) 



def account_settings(request):
    home = Setting.objects.latest('id')
    context = {
        'home' : home,
    }
    return render(request, 'account_settings.html',context)     