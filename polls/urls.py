# had to create on your own
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]