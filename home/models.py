from . import blocks as homeblocks

from article.models import ArticlePage
from section.models import SectionPage , CategorySnippet
from django.db import models

from ads.models import AdSlot
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtailmodelchooser.edit_handlers import ModelChooserPanel

# Create your models here.

class HomePage(Page):
    show_in_menus_default = True
    template = "home/home_page.html"

    ajax_template = "home/ajax_section.html"
    
    parent_page_types = [
        'wagtailcore.Page',
    ]

    subpage_types = [
        'section.SectionPage',
        'authors.AllAuthorsPage',
    ]

    sections_stream = StreamField(
        [
            ("home_page_section_block", homeblocks.HomepageFeaturedSectionBlock())
        ],
        null=True,
        blank=True,
    )

    home_leaderboard_ad_slot = models.ForeignKey(
        AdSlot,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )
    home_mobile_leaderboard_ad_slot = models.ForeignKey(
        AdSlot,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )
    home_sidebar_ad_slot1 = models.ForeignKey(
        AdSlot,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )
    home_sidebar_ad_slot2 = models.ForeignKey(
        AdSlot,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel("sections_stream", heading="Sections"),
        ModelChooserPanel('home_leaderboard_ad_slot'),
        ModelChooserPanel('home_mobile_leaderboard_ad_slot'),
        ModelChooserPanel('home_sidebar_ad_slot1'),
        ModelChooserPanel('home_sidebar_ad_slot2'),
    ]


    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        qs = ArticlePage.objects.live().public().order_by('-last_published_at')
        context['above_cut_articles'] = qs[:6]
        context['breaking_news_article'] = qs.filter(is_breaking=True)

        for section_stream in self.sections_stream:
            section_title = str(section_stream.value['section'])
            section_slug = section_stream.value['section'].slug
            context[section_title] = self.get_section_articles(section_slug=section_slug)

        return context
                  
    #takes a section_slug and returns the feature articles for that section
    def get_section_articles(self, section_slug):
        sectionPage = SectionPage.objects.get(slug = section_slug)
        return sectionPage.get_featured_articles()

    def get_all_section_slug(self):
        
        allsection_slug = []
        allsectionPages = SectionPage.objects.all()

        for section in allsectionPages:
            allsection_slug.append(section.slug)

        return allsection_slug