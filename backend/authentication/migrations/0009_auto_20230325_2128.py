# Generated by Django 4.1.7 on 2023-03-26 02:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_user_assigned_user_favorites_alter_user_my_games'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='favorites',
        )
    ]