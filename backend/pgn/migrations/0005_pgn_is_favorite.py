# Generated by Django 4.1.7 on 2023-03-24 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pgn', '0004_remove_pgn_is_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='pgn',
            name='is_favorite',
            field=models.BooleanField(default=False, verbose_name='is favorite'),
            preserve_default=False,
        ),
    ]
