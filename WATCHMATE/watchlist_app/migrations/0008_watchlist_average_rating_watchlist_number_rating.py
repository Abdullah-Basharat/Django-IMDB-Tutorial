# Generated by Django 5.1.6 on 2025-03-12 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0007_remove_watchlist_average_rating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='average_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='number_rating',
            field=models.IntegerField(default=0),
        ),
    ]
