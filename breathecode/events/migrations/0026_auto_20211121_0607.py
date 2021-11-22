# Generated by Django 3.2.9 on 2021-11-21 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0025_eventcheckin_attended_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='managed_by',
            field=models.CharField(choices=[('BREATHECODE', 'Breathecode'), ('EVENTBRITE', 'Eventbrite')],
                                   default='EVENTBRITE',
                                   max_length=11),
        ),
        migrations.AddField(
            model_name='event',
            name='sync',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='sync_status',
            field=models.CharField(
                choices=[('PENDING', 'Pending'), ('PERSISTED', 'Persisted'), ('ERROR', 'Error'),
                         ('WARNING', 'Warning'), ('SYNCHED', 'Synched')],
                default='PENDING',
                help_text='One of: PENDING, PERSISTED or ERROR depending on how the eventbrite sync status',
                max_length=9),
        ),
        migrations.AlterField(
            model_name='organization',
            name='sync_status',
            field=models.CharField(
                choices=[('PENDING', 'Pending'), ('PERSISTED', 'Persisted'),
                         ('ERROR', 'Error'), ('WARNING', 'Warning'), ('SYNCHED', 'Synched')],
                default='PENDING',
                help_text='One of: PENDING, PERSISTED or ERROR depending on how the eventbrite sync status',
                max_length=9),
        ),
    ]
