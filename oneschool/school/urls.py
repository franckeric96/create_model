from django.urls import path
from . import views

urlpatterns = [
    path('single', views.single, name='single')
]
