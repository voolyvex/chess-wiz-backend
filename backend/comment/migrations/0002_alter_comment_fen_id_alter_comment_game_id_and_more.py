# Generated by Django 4.1.7 on 2023-02-28 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pgn', '0001_initial'),
        ('fen', '0001_initial'),
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='fen_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fen.fen'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='game_id',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='pgn_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pgn.pgn'),
        ),
    ]