# Generated by Django 4.0.4 on 2022-05-16 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appadmin', '0008_alter_article_pinned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pinned',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]