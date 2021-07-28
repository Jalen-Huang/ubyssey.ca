# Generated by Django 3.2.5 on 2021-07-27 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_articleseriessnippet_seriesorderable'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='articlepage',
            index=models.Index(fields=['last_modified_at'], name='article_art_last_mo_a81817_idx'),
        ),
    ]
