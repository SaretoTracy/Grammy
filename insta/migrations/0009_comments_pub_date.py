# Generated by Django 4.0.3 on 2022-04-03 22:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0008_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]