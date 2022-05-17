from django.shortcuts import render
from django.core.paginator import Paginator
from appadmin.models import About, Advertisement, Article, Category, Tag


# Create your views here.
def Home(request):
    iklan = Advertisement.objects.get(id=1)
    list_artikel = Article.objects.all().filter(status='1')
    list_kategori = Category.objects.all()
    list_tag = Tag.objects.all()
    list_pin = list_artikel.filter(pinned=1)
    paginator = Paginator(list_artikel, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'heading': 'Homepage', 'list_artikel': list_artikel,'list_kategori': list_kategori, 'list_tag': list_tag, 'list_pin': list_pin, 'iklan': iklan, 'page_obj': page_obj}
    return render(request, "appsite/home.html", context)


def Tentang(request):
    iklan = Advertisement.objects.get(id=1)
    about = About.objects.get(id=1)
    list_kategori = Category.objects.all()
    context = {'heading': 'About', 'list_kategori': list_kategori,'about': about, 'iklan': iklan}
    return render(request, "appsite/about.html", context)


def Kategori(request, slug):
    iklan = Advertisement.objects.get(id=1)
    list_artikel = Article.objects.all().filter(status='1')
    list_kategori = Category.objects.all()
    list_tag = Tag.objects.all()
    list_pin = list_artikel.filter(pinned=1)
    data = list_kategori.get(slug=slug)
    filter_post = list_artikel.filter(kategori=data)
    paginator = Paginator(filter_post, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'heading': 'Kategori', 'list_artikel': list_artikel, 'list_kategori': list_kategori,'list_tag': list_tag, 'list_pin': list_pin, 'filter_post': filter_post, 'iklan': iklan, 'page_obj': page_obj}
    return render(request, "appsite/kategori.html", context)


def Tagpost(request, slug):
    iklan = Advertisement.objects.get(id=1)
    list_artikel = Article.objects.all().filter(status='1')
    list_kategori = Category.objects.all()
    list_tag = Tag.objects.all()
    list_pin = list_artikel.filter(pinned=1)
    data = list_tag.get(slug=slug)
    filter_post = list_artikel.filter(tag=data)
    paginator = Paginator(filter_post, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'heading': 'Tag', 'list_artikel': list_artikel, 'list_kategori': list_kategori,'list_tag': list_tag, 'list_pin': list_pin, 'filter_post': filter_post, 'iklan': iklan, 'page_obj': page_obj}
    return render(request, "appsite/tag.html", context)


def Postingan(request, slug):
    iklan = Advertisement.objects.get(id=1)
    list_artikel = Article.objects.all().filter(status='1')
    list_kategori = Category.objects.all()
    list_tag = Tag.objects.all()
    list_pin = list_artikel.filter(pinned=1)
    artikel = list_artikel.get(slug=slug)
    context = {'heading': 'Tag', 'list_artikel': list_artikel, 'list_kategori': list_kategori,'list_tag': list_tag, 'list_pin': list_pin, 'artikel': artikel, 'iklan': iklan}
    return render(request, "appsite/artikel.html", context)
