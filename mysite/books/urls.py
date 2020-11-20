from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('latest', views.latest_books, name='latest'),
]