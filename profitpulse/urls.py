from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

from users import views


def helloworld(request):
    print('Hello World!')
    return HttpResponse('Hello world')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('helloworld/', helloworld),
    path('login/', views.login_page, name="login"),
    path('users/', include('users.urls')), ##includes the users app
]
