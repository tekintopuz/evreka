# Generated by Django 4.0.1 on 2022-01-17 19:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0006_rename_last_latitude_vehicle_latitude_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longtitude', models.FloatField(blank=True, null=True)),
                ('collection_frequency', models.IntegerField(default=0)),
                ('last_collection', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BinOperation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('bin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navigation.bin')),
                ('operation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navigation.operation')),
            ],
        ),
    ]