from django.http import HttpResponse

# Create your views here.
def users(request):
    return HttpResponse('Here are our users')