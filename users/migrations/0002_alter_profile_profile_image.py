# Generated by Django 5.0.6 on 2024-09-24 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='static/images/profiles/user-default.png', null=True, upload_to='static/images/profiles/'),
        ),
    ]
