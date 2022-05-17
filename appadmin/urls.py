from django.urls import path
from appadmin.views import Home, PostCreate, PostList, PostUpdate, Profil, Iklan, Tentang


urlpatterns = [
    path('', Home, name='home'),
    path('about/', Tentang, name='about'),
    path('create/', PostCreate, name='create'),
    path('iklan/', Iklan, name='iklan'),
    path('list/', PostList, name='list'),
    path('profil/', Profil, name='profil'),
    path('update/<slug:slug>/', PostUpdate, name='update'),
]
