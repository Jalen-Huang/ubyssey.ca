# Generated by Django 3.1.8 on 2021-06-11 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specialfeaturelanding', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='speciallandingpage',
            name='current_section',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
