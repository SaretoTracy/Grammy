# Generated by Django 4.0.3 on 2022-04-03 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0009_comments_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='photos',
            name='comments',
            field=models.TextField(default='No Comment'),
        ),
    ]