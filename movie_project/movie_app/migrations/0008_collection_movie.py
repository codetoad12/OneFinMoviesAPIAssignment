# Generated by Django 4.0.5 on 2023-01-17 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0007_alter_movie_user_alter_movie_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='movie',
            field=models.ManyToManyField(to='movie_app.movie'),
        ),
    ]
