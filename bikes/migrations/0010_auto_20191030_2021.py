# Generated by Django 2.2.4 on 2019-10-30 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0009_auto_20191024_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bikerepairs',
            name='date_malfunctioned',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
