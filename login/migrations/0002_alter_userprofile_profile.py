# Generated by Django 4.2 on 2023-04-20 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile',
            field=models.ImageField(blank=True, upload_to='upload'),
        ),
    ]