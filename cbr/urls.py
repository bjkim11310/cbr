from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('community', views.home, name='community'),
    path('about', views.about, name='about'),
    path('ap', views.ap, name='ap'),
    path('sat', views.sat, name='sat'),
    path('<str:testName>', views.goTest, name='goTest'),
]