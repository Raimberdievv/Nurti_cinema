# Generated by Django 4.0.2 on 2022-05-07 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('film', '0006_popular_movies'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_image', models.ImageField(blank=True, null=True, upload_to='movie_image/')),
            ],
            options={
                'verbose_name': 'Картинка фильма',
                'verbose_name_plural': 'Картинки фильмов',
            },
        ),
        migrations.DeleteModel(
            name='popular_movies',
        ),
        migrations.AddField(
            model_name='movies',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='movie_category', to='categories.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movies',
            name='genre',
            field=models.CharField(choices=[('Боевики', 'Боевики'), ('Комедии', 'Комедии'), ('Фантастика/фэнтези', 'Фантастика/фэнтези'), ('Мультфильмы', 'Мультфильмы'), ('Драма/мелодрама', 'Драма/мелодрама'), ('Ужасы', 'Ужасы'), ('Детектив/Триллеры', 'Детектив/Триллеры'), ('Документальные', 'Документальные')], default='Фантастика/Боевики', max_length=250),
        ),
        migrations.AddField(
            model_name='movies',
            name='movie_trailer',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movies',
            name='rating',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movies',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movies',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='movieimage',
            name='movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movie_image', to='film.movies'),
        ),
    ]