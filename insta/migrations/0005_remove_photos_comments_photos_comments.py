# Generated by Django 4.0.3 on 2022-04-03 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0004_alter_photos_image_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photos',
            name='comments',
        ),
        migrations.AddField(
            model_name='photos',
            name='comments',
            field=models.ManyToManyField(to='insta.comments'),
        ),
    ]
