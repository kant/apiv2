# Generated by Django 3.1.4 on 2020-12-09 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursework', '0005_auto_20200814_0307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='syllabus',
            name='json',
            field=models.JSONField(),
        ),
    ]