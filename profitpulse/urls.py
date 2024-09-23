from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

def helloworld(request):
    print('Hello World!')
    return HttpResponse('Hello world')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', helloworld),
    path('users/', include('users.urls')), ##includes the users app
]
