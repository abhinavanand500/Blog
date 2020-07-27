from django.urls import path, include
from home import views

urlpatterns = [
    path('',views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('search',views.search,name='search'),
    path('handleSignup',views.handleSignup,name='handleSignup'),
    path('handleLogin',views.handleLogin,name='handleLogin'),
    path('handleLogout',views.handleLogout,name='handleLogout'),
    path('adminside', views.adminside),

]
