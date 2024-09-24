from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path, include

from users import views


def helloworld(request):
    print('Hello World!')
    return HttpResponse('Hello world')

def dashboard(request):
    return render(request, 'dashboard.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name="dashboard"),
    path('helloworld/', helloworld, name="helloworld"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register_user"),
    path('users/', include('users.urls')), ##includes the users app
]
