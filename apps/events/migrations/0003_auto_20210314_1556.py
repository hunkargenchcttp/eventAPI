# Generated by Django 3.1.7 on 2021-03-14 12:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_remove_event_sessions'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='endDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='event',
            name='sessions',
            field=models.ManyToManyField(to='events.session'),
        ),
        migrations.AddField(
            model_name='event',
            name='startDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='event',
            name='timezone',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='session',
            name='endDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='session',
            name='speaker',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='session',
            name='startDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
