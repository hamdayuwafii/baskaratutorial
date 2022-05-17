# Generated by Django 4.0.4 on 2022-05-15 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appadmin', '0002_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('rectangle', models.ImageField(upload_to='ads/')),
                ('rectangle_link', models.URLField()),
                ('leaderboard', models.ImageField(upload_to='ads/')),
                ('leaderboard_link', models.URLField()),
                ('potrait', models.ImageField(upload_to='ads/')),
                ('potrait_link', models.URLField()),
                ('slug', models.SlugField(blank=True, editable=False, null=True)),
                ('durasi', models.DateTimeField()),
                ('reg', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Advertisement',
                'verbose_name_plural': 'Advertisements',
            },
        ),
    ]
