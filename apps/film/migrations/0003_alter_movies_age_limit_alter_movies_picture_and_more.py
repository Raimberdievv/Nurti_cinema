# Generated by Django 4.0.2 on 2022-04-30 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0002_movies_alter_setting_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='age_limit',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='movies',
            name='picture',
            field=models.ImageField(upload_to='media/logo/'),
        ),
        migrations.AlterField(
            model_name='movies',
            name='release_date',
            field=models.DateField(auto_now=True),
        ),
    ]
