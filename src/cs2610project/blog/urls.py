from django.urls import path

from . import views

app_name='blog'
urlpatterns = [
    path('bio', views.bio, name='bio'),
    path('tips', views.tips, name='tips'),
    path('', views.index, name='index'),
    path('bloghome',views.BlogHome, name ='bloghome'),
    path('<int:b_id>/postComment', views.postComment, name = 'postComment'),
    path('blogarchive',views.BlogArchive, name ='archive'),
    path('<int:b_id>',views.BlogEntry, name ='entry'),
    path('nuke', views.nuke, name = 'nuke'),
    path('init', views.init,name = 'init' ),
]

