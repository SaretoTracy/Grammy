# Generated by Django 4.0.3 on 2022-04-03 18:42

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', cloudinary.models.CloudinaryField(max_length=255, verbose_name='images/')),
                ('bio', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=100)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='images/')),
                ('caption', models.CharField(max_length=250)),
                ('Comments', models.CharField(max_length=250)),
                ('profile', models.ManyToManyField(to='insta.profile')),
            ],
        ),
    ]
