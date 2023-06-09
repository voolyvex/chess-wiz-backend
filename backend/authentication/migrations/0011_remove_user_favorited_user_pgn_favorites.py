# Generated by Django 4.1.7 on 2023-03-28 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pgn', '0010_auto_20230325_2124'),
        ('authentication', '0010_pgnfavorites_user_favorited'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='favorited',
        ),
        migrations.AddField(
            model_name='user',
            name='pgn_favorites',
            field=models.ManyToManyField(related_name='favorite_users', through='authentication.PgnFavorites', to='pgn.pgn'),
        ),
    ]
