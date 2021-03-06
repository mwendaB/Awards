# Generated by Django 3.2.7 on 2021-12-14 07:33

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, default='Hey there Im using awards', max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=cloudinary.models.CloudinaryField(default='static/profilepic/default.jpg', max_length=255, verbose_name='image'),
        ),
    ]
