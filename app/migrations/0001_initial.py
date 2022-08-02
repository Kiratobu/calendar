# Generated by Django 4.0.6 on 2022-07-28 10:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('head_branch', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('date', models.DateField(verbose_name='Дата события')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('time_from', models.TimeField(verbose_name='Время начала')),
                ('time_to', models.TimeField(verbose_name='Время окончания')),
                ('repeat', models.CharField(blank=True, choices=[('MON', 'Каждый Понедельник'), ('TUE', 'Каждый Вторник'), ('WED', 'Каждую Среду'), ('THU', 'Каждый Четверг'), ('FRI', 'Каждую Пятницу'), ('SAT', 'Каждую Субботу'), ('SUN', 'Каждое Воскресенье'), ('ED', 'Каждый день'), ('EWD', 'Каждый будний день'), ('EW', 'Каждую неделю'), ('EM', 'Каждый месяц'), ('EY', 'Каждый год')], max_length=255, null=True, verbose_name='Повторение')),
                ('is_private', models.BooleanField(default=True, verbose_name='Является личным событием')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification', models.CharField(blank=True, choices=[('Without notification', 'Без уведомлений'), ('five_minutes', 'За 5 минут до события'), ('ten_minutes', 'За 10 минут до события'), ('fifteen_minutes', 'За 15 минут до события'), ('thirty_minutes', 'За 30 минут до события'), ('one_hour', 'За час до события'), ('three_hours', 'За 3 часа до события'), ('one_day', 'За день до события'), ('three_days', 'За 3 дня до события')], default='Without notification', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('organisation_admin', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserParticipant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('accepted', 'Принято'), ('declined', 'Отклонено'), ('deligated', 'Делегировано')], max_length=100, verbose_name='Статус мероприятия')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_creator', to=settings.AUTH_USER_MODEL, verbose_name='Организатор')),
                ('event_participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_participant', to='app.event')),
                ('user_participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_participant', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('capacity', models.PositiveIntegerField(verbose_name='Вместимость')),
                ('is_available', models.BooleanField(verbose_name='Доступно')),
                ('has_projector', models.BooleanField(verbose_name='Имеется проектор')),
                ('has_desk', models.BooleanField(verbose_name='Имеется доска')),
                ('organization_room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='app.organisation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ImageRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('room_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.room')),
            ],
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('color', models.CharField(choices=[('R', 'Красный'), ('G', 'Зелёный'), ('B', 'Синий'), ('Y', 'Жёлтый'), ('O', 'Оранжевый'), ('P', 'Фиолетовый')], max_length=255, verbose_name='Цвет')),
                ('user_event_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_event_type', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_type', to='app.eventtype'),
        ),
        migrations.AddField(
            model_name='event',
            name='notifications',
            field=models.ManyToManyField(related_name='notifications', to='app.notification'),
        ),
        migrations.AddField(
            model_name='event',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.room'),
        ),
        migrations.CreateModel(
            name='BranchPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.branch')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.post')),
            ],
        ),
        migrations.AddField(
            model_name='branch',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='app.organisation'),
        ),
        migrations.AlterUniqueTogether(
            name='branch',
            unique_together={('organisation', 'title')},
        ),
    ]
