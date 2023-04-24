# Generated by Django 4.2 on 2023-04-24 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pgn', '0010_auto_20230325_2124'),
        ('authentication', '0011_remove_user_favorited_user_pgn_favorites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='assigned',
            field=models.ManyToManyField(blank=True, related_name='user_assigned', to='pgn.pgn'),
        ),
        migrations.AlterField(
            model_name='user',
            name='my_games',
            field=models.ManyToManyField(blank=True, related_name='user_mygames', to='pgn.pgn'),
        ),
    ]
