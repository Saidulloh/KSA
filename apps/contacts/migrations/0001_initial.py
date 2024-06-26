# Generated by Django 4.1.5 on 2024-03-26 11:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OurContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('phone_number', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(message='You should write +996[code][number]', regex='^(\\+996)\\d{9}$')], verbose_name='phone_number')),
                ('address', models.CharField(max_length=256, verbose_name='address')),
                ('chart_from', models.DateTimeField(auto_now=True, verbose_name='chart_from')),
                ('chart_till', models.DateTimeField(auto_now=True, verbose_name='chart_till')),
            ],
            options={
                'verbose_name': 'our contact',
                'verbose_name_plural': 'Our contacts',
            },
        ),
    ]
