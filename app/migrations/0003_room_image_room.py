# Generated by Django 4.0.6 on 2022-08-01 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_event_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='image_room',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
    ]
