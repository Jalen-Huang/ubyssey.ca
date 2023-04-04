# Generated by Django 3.2.11 on 2023-04-04 01:12

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_homepage_sidebar_stream'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='sidebar_stream',
            field=wagtail.core.fields.StreamField([('sidebar_advertisement_block', wagtail.core.blocks.StructBlock([])), ('sidebar_issues_block', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('issues', wagtail.core.blocks.StreamBlock([('issue', wagtail.core.blocks.StructBlock([('date', wagtail.core.blocks.DateBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('show_image', wagtail.core.blocks.BooleanBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=True))]))]))])), ('sidebar_section_block', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('section', wagtail.core.blocks.PageChooserBlock(page_type=['section.SectionPage']))])), ('sidebar_flex_stream', wagtail.core.blocks.StreamBlock([('title', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('image_link', wagtail.core.blocks.StructBlock([('date', wagtail.core.blocks.DateBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('show_image', wagtail.core.blocks.BooleanBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=True))]))]))], blank=True, null=True),
        ),
    ]
