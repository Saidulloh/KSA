# Generated by Django 4.1.5 on 2024-03-26 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='document_first_images/', verbose_name='document_first_image')),
                ('second_image', models.ImageField(upload_to='document_second_images/', verbose_name='document_second_image')),
            ],
            options={
                'verbose_name': 'document image',
                'verbose_name_plural': 'Document images',
            },
        ),
    ]
