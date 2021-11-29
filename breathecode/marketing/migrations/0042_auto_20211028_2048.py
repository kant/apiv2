# Generated by Django 3.2.7 on 2021-10-28 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0041_merge_20211018_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortlink',
            name='destination_status_text',
            field=models.CharField(blank=True, default=None, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='shortlink',
            name='lastclick_at',
            field=models.DateTimeField(blank=True,
                                       default=None,
                                       help_text='Last time a click was registered for this link',
                                       null=True),
        ),
        migrations.AddField(
            model_name='shortlink',
            name='private',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='downloadable',
            name='destination_status',
            field=models.CharField(choices=[('ACTIVE', 'Active'), ('NOT_FOUND', 'Not found'),
                                            ('ERROR', 'Error')],
                                   default='ACTIVE',
                                   max_length=15),
        ),
        migrations.AlterField(
            model_name='shortlink',
            name='destination_status',
            field=models.CharField(choices=[('ACTIVE', 'Active'), ('NOT_FOUND', 'Not found'),
                                            ('ERROR', 'Error')],
                                   default='ACTIVE',
                                   max_length=15),
        ),
    ]
