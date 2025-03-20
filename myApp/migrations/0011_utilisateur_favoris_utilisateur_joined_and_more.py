# Generated by Django 5.0.3 on 2024-03-29 23:22

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0010_utilisateur_bio_utilisateur_image_back_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateur',
            name='favoris',
            field=models.ManyToManyField(to='myApp.publication'),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='joined',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='localisation',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
