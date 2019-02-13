from django.urls import path

from . import views

urlpatterns = [
    path('bio', views.bio, name='bio'),
    path('tips', views.tips, name='tips'),
    path('', views.index, name='index'),
               
]
