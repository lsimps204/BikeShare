# Generated by Django 2.2.4 on 2019-10-15 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0005_auto_20191014_2338'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LocationBikeCount',
        ),
    ]
