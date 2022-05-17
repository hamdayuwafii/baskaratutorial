from django import forms
from django.forms import widgets
from appadmin.models import Article, Profile, Advertisement, About


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = (
            "judul",
            "kategori",
            "tag",
            "body",
            "cover",
            "pinned",
            "status"
        )
        labels = {
            "judul": "Judul",
            "kategori": "Kategori",
            "tag": "Tag",
            "body": "Body",
            "cover": "Cover",
            "pinned": "Pinned",
            "status": "Status",
        }
        widgets = {
            "judul": widgets.TextInput({"class": "form-control form-control-sm", "placeholder": "Judul Artikel"}),
            "kategori": widgets.Select({"class": "form-select form-select-sm"}),
            "tag": widgets.SelectMultiple({"class": "form-select form-select-sm"}),
            "body": widgets.Textarea({"class": "form-control"}),
            "cover": widgets.FileInput({"class": "form-control form-control-sm", "type": "file"}),
            "pinned": widgets.CheckboxInput({"class": "form-check-input"}),
            "status": widgets.Select({"class": "form-select form-select-sm"}),
        }


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ("nama1", "nama2", "nohp", "email")
        labels = {
            "nama1": "Nama Depan",
            "nama2": "Nama Belakang",
            "nohp": "Nomor Handphone",
            "email": "Email",
        }
        widgets = {
            "nama1": widgets.TextInput({"class": "form-control"}),
            "nama2": widgets.TextInput({"class": "form-control"}),
            "nohp": widgets.TextInput({"class": "form-control"}),
            "email": widgets.EmailInput({"class": "form-control", "type": "email"}),
        }


class AdvertisementForm(forms.ModelForm):

    class Meta:
        model = Advertisement
        fields = (
            "rectangle",
            "rectangle_link",
            "leaderboard",
            "leaderboard_link",
            "potrait",
            "potrait_link",
            "durasi"
        )
        labels = {
            "rectangle": "Rectangle",
            "rectangle_link": "Link",
            "leaderboard": "Leaderboard",
            "leaderboard_link": "Link",
            "potrait": "Potrait",
            "potrait_link": "Link",
            "durasi": "Durasi",
        }
        widgets = {
            "rectangle": widgets.FileInput({"class": "form-control", "type": "file"}),
            "rectangle_link": widgets.URLInput({"class": "form-control"}),
            "leaderboard": widgets.FileInput({"class": "form-control", "type": "file"}),
            "leaderboard_link": widgets.URLInput({"class": "form-control"}),
            "potrait": widgets.FileInput({"class": "form-control", "type": "file"}),
            "potrait_link": widgets.URLInput({"class": "form-control"}),
            "durasi": widgets.DateInput({"class": "form-control", "type": "date"}),
        }


class AboutForm(forms.ModelForm):

    class Meta:
        model = About
        fields = ("body",)
        widgets = {"body": widgets.Textarea({"class": "form-control"})}
