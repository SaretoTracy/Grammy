# Generated by Django 4.0.3 on 2022-04-03 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photos',
            name='profile',
        ),
    ]
