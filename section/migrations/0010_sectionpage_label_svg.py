# Generated by Django 3.2.11 on 2023-05-24 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0012_uploadeddocument'),
        ('section', '0009_alter_sectionpage_colour'),
    ]

    operations = [
        migrations.AddField(
            model_name='sectionpage',
            name='label_svg',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.document'),
        ),
    ]
