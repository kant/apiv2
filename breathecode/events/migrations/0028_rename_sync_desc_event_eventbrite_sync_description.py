# Generated by Django 3.2.9 on 2021-11-29 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0027_rename_sync_status_event_eventbrite_sync_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='sync_desc',
            new_name='eventbrite_sync_description',
        ),
    ]
