from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor.fields import RichTextField
# Create your models here.


class Category(models.Model):
    nama = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(blank=True, null=True, editable=False)

    class Meta:

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.nama

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nama)
        super(Category, self).save(*args, **kwargs)


class Tag(models.Model):
    nama = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(blank=True, null=True, editable=False)

    class Meta:

        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.nama

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nama)
        super(Tag, self).save(*args, **kwargs)


class Article(models.Model):
    judul = models.CharField(max_length=255, unique=True)
    kategori = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    body = RichTextField(blank=True, null=True)
    cover = models.ImageField(upload_to='artikel/')
    pinned = models.BooleanField(default=False)
    slug = models.SlugField(blank=True, null=True, editable=False)
    posted = models.DateTimeField(auto_now=False, auto_now_add=True)
    edited = models.DateTimeField(auto_now=True, auto_now_add=False)
    status = models.CharField(
        max_length=50,
        choices=(
            ("1", "published"),
            ("2", "draft"),
        ),
        default=1
    )

    class Meta:

        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.judul

    def save(self, *args, **kwargs):
        self.slug = slugify(self.judul)
        super(Article, self).save(*args, **kwargs)


class About(models.Model):
    nama = models.CharField(max_length=255, unique=True)
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True, editable=False)

    class Meta:

        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

    def __str__(self):
        return self.nama

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nama)
        super(About, self).save(*args, **kwargs)


class Advertisement(models.Model):
    nama = models.CharField(max_length=50)
    rectangle = models.ImageField(upload_to='ads/')
    rectangle_link = models.URLField(max_length=200)
    leaderboard = models.ImageField(upload_to='ads/')
    leaderboard_link = models.URLField(max_length=200)
    potrait = models.ImageField(upload_to='ads/')
    potrait_link = models.URLField(max_length=200)
    slug = models.SlugField(blank=True, null=True, editable=False)
    durasi = models.DateField(auto_now=False, auto_now_add=False)
    reg = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:

        verbose_name = 'Advertisement'
        verbose_name_plural = 'Advertisements'

    def __str__(self):
        return self.nama

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nama)
        super(Advertisement, self).save(*args, **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama1 = models.CharField(max_length=50)
    nama2 = models.CharField(max_length=50)
    nohp = models.CharField(max_length=12, blank=True, null=True)
    email = models.EmailField(max_length=254)
    slug = models.SlugField(blank=True, null=True, editable=False)

    class Meta:

        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.nama1

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nama1)
        super(Profile, self).save(*args, **kwargs)
