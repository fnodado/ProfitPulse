from . import views
from  django.urls import path

urlpatterns = [
    path('create-trade/', views.create_trade, name="create_trade"),
]