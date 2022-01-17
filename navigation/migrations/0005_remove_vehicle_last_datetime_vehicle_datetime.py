# Generated by Django 4.0.1 on 2022-01-17 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0004_alter_navigationrecord_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='last_datetime',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]