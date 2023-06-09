# Generated by Django 4.1.7 on 2023-03-12 07:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_band_active_band_biography_band_genre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='abt',
            name='description',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='title',
            name='description',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='title',
            name='sold',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='title',
            name='type',
            field=models.CharField(choices=[('RE', 'Records'), ('CL', 'Clothing'), ('PO', 'Posters'), ('MI', 'Miscellaneous')], default='PO', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='title',
            name='year_released',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2023)]),
        ),
        migrations.AlterField(
            model_name='band',
            name='year_formed',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2023)]),
        ),
    ]
