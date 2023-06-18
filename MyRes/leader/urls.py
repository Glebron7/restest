from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Team'),
    path('about-us', views.about, name='About'),
]
