# Generated by Django 3.2.11 on 2022-05-19 22:43

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtailmodelchooser.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20220518_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='sidebar_stream',
            field=wagtail.fields.StreamField([('sidebar_advertisement_block', wagtail.blocks.StructBlock([('ad_slot', wagtailmodelchooser.blocks.ModelChooserBlock(target_model='ads.adslot'))])), ('sidebar_issuu_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=255, required=True))])), ('sidebar_section_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=255, required=True)), ('section', wagtail.blocks.PageChooserBlock(page_type=['section.SectionPage']))]))], blank=True, null=True),
        ),
    ]
