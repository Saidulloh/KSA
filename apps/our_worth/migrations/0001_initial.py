# Generated by Django 4.1.5 on 2024-03-26 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OurWorth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='title')),
                ('icon', models.ImageField(upload_to='our_worth_icons', verbose_name='icon')),
                ('description', models.TextField(verbose_name='description')),
            ],
            options={
                'verbose_name': 'our worth',
                'verbose_name_plural': 'Our worths',
            },
        ),
    ]