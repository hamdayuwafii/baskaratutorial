from django.contrib import admin
from appadmin.models import About, Advertisement, Article, Category, Profile, Tag


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('slug', 'posted', 'edited')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    readonly_fields = ('slug', 'reg')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
