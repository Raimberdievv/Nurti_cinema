# Generated by Django 4.0.2 on 2022-05-07 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0007_movieimage_delete_popular_movies_movies_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='release_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]