# Generated by Django 5.0.3 on 2024-03-29 00:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0009_alter_commentaire_utilisateur_and_more'),
        ('projecto_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='utilisateur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.utilisateur'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='utilisateur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.utilisateur'),
        ),
        migrations.AlterField(
            model_name='langues',
            name='utilisateur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.utilisateur'),
        ),
        migrations.AlterField(
            model_name='skills',
            name='utilisateur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.utilisateur'),
        ),
        migrations.DeleteModel(
            name='Utilisateur',
        ),
    ]
