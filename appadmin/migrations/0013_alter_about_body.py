# Generated by Django 4.0.4 on 2022-05-16 15:02

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appadmin', '0012_alter_article_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
