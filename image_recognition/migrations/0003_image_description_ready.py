# Generated by Django 3.0.3 on 2020-06-01 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_recognition', '0002_auto_20200601_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='description_ready',
            field=models.BooleanField(default=False),
        ),
    ]
