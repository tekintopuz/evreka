# Generated by Django 4.0.1 on 2022-01-17 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0007_bin_operation_binoperation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='binoperation',
            name='bin',
        ),
        migrations.RemoveField(
            model_name='binoperation',
            name='operation',
        ),
        migrations.DeleteModel(
            name='Bin',
        ),
        migrations.DeleteModel(
            name='BinOperation',
        ),
        migrations.DeleteModel(
            name='Operation',
        ),
    ]