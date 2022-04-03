# Generated by Django 4.0.3 on 2022-04-03 18:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0002_remove_photos_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='photos',
            name='Comments',
        ),
        migrations.AddField(
            model_name='photos',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='photos',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='photos',
            name='profile',
            field=models.ManyToManyField(to='insta.profile'),
        ),
        migrations.AddField(
            model_name='photos',
            name='comments',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='insta.comments'),
            preserve_default=False,
        ),
    ]
