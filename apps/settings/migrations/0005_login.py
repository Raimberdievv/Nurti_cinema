# Generated by Django 4.0.2 on 2022-05-05 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0004_ad_delete_our_statistics_remove_about_us_about_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('surname', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
