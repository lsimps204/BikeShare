# Generated by Django 2.2.4 on 2019-10-20 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0006_delete_locationbikecount'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile/profile_images'),
        ),
    ]
