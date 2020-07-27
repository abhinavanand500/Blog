from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [

    # Api to Post or comment
    path('postComment', views.postComment, name = 'postComment'),

    #endpoints
    path('',views.blogHome,name='blogHome'),
    path('<str:slug>',views.blogPost,name='blogPost'),
    

]
