# Generated by Django 4.0.5 on 2022-07-07 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_user_id_userpost_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='branch',
            options={'ordering': ['title']},
        ),
        migrations.AlterField(
            model_name='branch',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='app.organisation'),
        ),
        migrations.AlterUniqueTogether(
            name='branch',
            unique_together={('organisation', 'title')},
        ),
    ]
