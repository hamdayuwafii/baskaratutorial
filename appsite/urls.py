from django.urls import path
from appsite.views import Home, Kategori, Postingan, Tagpost, Tentang


urlpatterns = [
    path('', Home, name='home'),
    path('about/', Tentang, name='about'),
    path('artikel/<slug:slug>/', Postingan, name='postingan'),
    path('kategori/<slug:slug>/', Kategori, name='kategori'),
    path('tag/<slug:slug>/', Tagpost, name='tag'),
]
