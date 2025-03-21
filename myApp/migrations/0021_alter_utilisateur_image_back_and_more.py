# Generated by Django 5.0.3 on 2024-03-31 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0020_alter_utilisateur_image_back_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='image_back',
            field=models.ImageField(blank=True, default='media/images/images/grey_pic.jpg', null=True, upload_to='images/images/'),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='photo_profile',
            field=models.ImageField(blank=True, default='media/images/images/defaultImage.jpg', null=True, upload_to='images/images/'),
        ),
    ]
