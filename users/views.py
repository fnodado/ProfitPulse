from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .models import Profile


# Create your views here.
def users(request):
    profiles = Profile.objects.all()
    print(profiles)
    return render(request, 'users/account.html')

def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile': profile}
    return render(request, 'users/account.html', context)

def login_page(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            print('Username does not exits')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            #Create session id
            login(request, user)
            print("login user: ", user)
            profile_user = user.profile
            print("profile_user user: ", profile_user.id)
            return redirect('user-profile', pk=profile_user.id)
        else:
            print("Username OR Password is incorrect")

    return render(request, 'users/login_register.html')
