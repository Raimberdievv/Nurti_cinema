# Generated by Django 4.0.2 on 2022-04-30 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0004_alter_movies_picture'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Setting',
        ),
    ]
