# Generated by Django 4.0.2 on 2022-05-06 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0007_alter_sign_up_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watch_movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
    ]
