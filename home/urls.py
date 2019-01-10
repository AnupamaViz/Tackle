from django.contrib import admin
from django.conf.urls import url
from home import views

urlpatterns = [
    url(r'^homepage/', views.homePage, name='homepage'),
    url(r'^antibullyinglaws/', views.anBuLa, name='abl'),
    url(r'^womenrights/', views.women, name='wr'),
    url(r'^humanrights/', views.everyone, name='hr'),
    url(r'^childrights/', views.child, name='cr'),
    url(r'^signup/', views.signUp, name='sign'),
    url(r'^login/', views.logIn, name='login'),
    url(r'^post/',views.post, name='post'),
    url(r'^logged/', views.loggedIn, name='logged'),
    url(r'^loggedhome/', views.loggedHome, name='loghome'),
]
