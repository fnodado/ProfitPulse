from lib2to3.fixes.fix_input import context

from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout

from .forms import CustomUserCreationForm
from .models import Profile
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def users(request):
    profile_user = request.user
    # profiles = Profile.objects.all()
    print(profile_user)
    return render(request, 'users/account.html')

def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile': profile}
    return render(request, 'users/account.html', context)

def login_page(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exits')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            #Create session id
            login(request, user)
            print("login user: ", user)
            profile_user = user.profile
            print("profile_user user: ", profile_user.id)
            return redirect('dashboard')
        else:
            messages.error(request, "Username OR Password is incorrect")

    return render(request, 'users/login_register.html')

def logout_user(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('login')

def register_user(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')

    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)
