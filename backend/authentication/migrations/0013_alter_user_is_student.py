# Generated by Django 4.2 on 2023-04-24 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0012_alter_user_assigned_alter_user_my_games'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_student',
            field=models.BooleanField(blank=True, default=False, verbose_name='student status'),
        ),
    ]
