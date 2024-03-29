# Generated by Django 5.0.3 on 2024-03-09 18:25

import api.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_platform', models.CharField(max_length=100)),
                ('published_platform_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('creation_timestamp', models.DateTimeField(auto_now_add=True)),
                ('update_timestamp', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-update_timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_code', models.CharField(db_index=True, default=api.models.generate_property_code, max_length=8, unique=True)),
                ('guests_max_number', models.PositiveIntegerField()),
                ('bathrooms_quantity', models.PositiveIntegerField()),
                ('accepts_animals', models.BooleanField(default=False)),
                ('cleaning_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('activation_date', models.DateField()),
                ('creation_timestamp', models.DateTimeField(auto_now_add=True)),
                ('update_timestamp', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Properties',
                'ordering': ['-update_timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_code', models.CharField(db_index=True, default=api.models.generate_booking_code, max_length=8, unique=True)),
                ('checkin_date', models.DateField()),
                ('checkout_date', models.DateField()),
                ('total_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('comments', models.TextField()),
                ('guests_quantity', models.PositiveIntegerField()),
                ('creation_timestamp', models.DateTimeField(auto_now_add=True)),
                ('update_timestamp', models.DateTimeField(auto_now=True)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='api.listing')),
            ],
            options={
                'ordering': ['-update_timestamp'],
            },
        ),
        migrations.AddField(
            model_name='listing',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listings', to='api.property'),
        ),
    ]
