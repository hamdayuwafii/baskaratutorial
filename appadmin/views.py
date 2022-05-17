from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from appadmin.models import Article, Category, Profile, Tag, Advertisement, About
from appadmin.forms import ArticleForm, ProfileForm, AdvertisementForm, AboutForm


# Create your views here.
@login_required(login_url="login")
def Home(request):
    pengguna = request.user
    akun = Profile.objects.get(user=pengguna)
    list_artikel = Article.objects.all()
    list_kategori = Category.objects.all()
    list_tag = Tag.objects.all()
    published = list_artikel.filter(status='1')
    draft = list_artikel.filter(status='2')
    paginator = Paginator(list_artikel, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'heading': 'Dashboard', 'akun': akun, 'list_artikel': list_artikel, 'list_kategori': list_kategori,
               'list_tag': list_tag, 'published': published, 'draft': draft, 'page_obj': page_obj}
    return render(request, "appadmin/home.html", context)


@login_required(login_url="login")
def Tentang(request):
    data = About.objects.get(id=1)
    form = AboutForm(instance=data)
    if request.POST:
        form = AboutForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect("appadmin:home")
    context = {'form': form}
    return render(request, "appadmin/tentang.html", context)


@login_required(login_url="login")
def Iklan(request):
    list_iklan = Advertisement.objects.get(id=1)
    form = AdvertisementForm(instance=list_iklan)
    if request.POST:
        form = ArticleForm(request.POST, request.FILES, instance=list_iklan)
        if form.is_valid():
            form.save()
            return redirect("appadmin:iklan")
    context = {'list_iklan': list_iklan, 'form': form}
    return render(request, "appadmin/iklan.html", context)


@login_required(login_url="login")
def Profil(request):
    pengguna = request.user
    akun = Profile.objects.get(user=pengguna)
    form = ProfileForm(instance=akun)
    if request.POST:
        form = ProfileForm(request.POST, instance=akun)
        if form.is_valid():
            form.save()
            return redirect("appadmin:home")
    context = {'heading': 'Pengaturan Akun', 'akun': akun, 'form': form}
    return render(request, "appadmin/pengaturan.html", context)


@login_required(login_url="login")
def PostList(request):
    list_artikel = Article.objects.all()
    paginator = Paginator(list_artikel, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'heading': 'Daftar Artikel',
               'list_artikel': list_artikel, 'page_obj': page_obj}
    return render(request, "appadmin/postlist.html", context)


@login_required(login_url="login")
def PostCreate(request):
    form = ArticleForm()
    if request.POST:
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("appadmin:list")
    context = {'heading': 'Buat Artikel', 'form': form}
    return render(request, "appadmin/postform.html", context)


@login_required(login_url="login")
def PostUpdate(request, slug):
    data = Article.objects.get(slug=slug)
    form = ArticleForm(instance=data)
    if request.POST:
        form = ArticleForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect("appadmin:list")
    context = {'heading': 'Update Artikel', 'form': form}
    return render(request, "appadmin/postform.html", context)
