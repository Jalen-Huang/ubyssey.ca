from django.conf import settings
from django.urls import include, re_path
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve as serve_static

from dispatch.urls import admin_urls, api_urls, podcasts_urls

from ubyssey.views.feed import FrontpageFeed, SectionFeed
from ubyssey.views.main import UbysseyTheme, HomePageView, ArticleView
from ubyssey.views.guide import guide2016, guide2020

from ubyssey.views.advertise import AdvertiseTheme
from ubyssey.views.magazine import magazine

from ubyssey.zones import *
from ubyssey.widgets import *
from ubyssey.templates import *

from ubyssey.events.api.urls import urlpatterns as event_api_urls
from ubyssey.events.urls import urlpatterns as events_urls

from django.views.generic import TemplateView

theme = UbysseyTheme()
advertise = AdvertiseTheme()

urlpatterns = []

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    re_path(r'^admin', include(admin_urls)),
    re_path(r'^api/', include(api_urls)),
    re_path(r'^podcasts/', include(podcasts_urls)),

    re_path(r'^$', HomePageView.as_view(), name='home'),
    re_path(r'^search/$', theme.search, name='search'),
    re_path(r'^archive/$', theme.archive, name='archive'),
    re_path(r'^rss/$', FrontpageFeed(), name='frontpage-feed'),

    re_path(r'^(?P<slug>[-\w]+)/rss/$', SectionFeed(), name='section-feed'),
    re_path(r'^authors/(?P<slug>[-\w]+)/$', theme.author, name='author'),
    re_path(r'^topic/(\d*)/$', theme.topic, name='topic'),

    # Guide to UBC
    re_path(r'^guide/2016/$', guide2016.landing, name='guide-landing-2016'),
    re_path(r'^guide/2016/(?P<slug>[-\w]+)/$', guide2016.article, name='guide-article-2016'),

    re_path(r'^guide/(?P<year>[0-9]{4})/$', guide2020.landing, name='guide-landing'),
    re_path(r'^guide/(?P<year>[0-9]{4})/(?P<subsection>[-\w]+)/$', guide2020.landing_sub, name='guide-landing-sub'),
    re_path(r'^guide/(?P<year>[0-9]{4})/(?P<subsection>[-\w]+)/(?P<slug>[-\w]+)/$', guide2020.article, name='guide-article'),

    # Magazine
    re_path(r'^magazine/(?P<year>[0-9]{4})/$', magazine.magazine, name='magazine-landing'),
    re_path(r'^magazine/(?P<slug>[-\w]+)/$', magazine.article, name='magazine-article'),

    # Advertising
    re_path(r'^advertise/$', advertise.new, name='advertise-new'),

    # Elections
    re_path(r'^elections/$', theme.elections, name='elections'),

    # Centennial
    re_path(r'^100/$', theme.centennial, name='centennial-landing'),

    # Beta-features
    # re_path(r'^beta/notifications/$', theme.notification, name='notification-beta'),

    # Podcasts
    re_path(r'^podcast/(?P<slug>[-\w]+)', theme.podcast, name='podcasts'),

    # Events
    re_path(r'^events/', include(events_urls)),
    re_path(r'^api/events/', include(event_api_urls)),

    # Videos
    re_path(r'^videos/', theme.video, name='videos'),

    re_path(r'^(?P<section>[-\w]+)/(?P<slug>[-\w]+)/$', ArticleView.as_view(), name='article'),
    re_path(r'^(?P<slug>[-\w]+)/$', theme.section, name='page'),
    re_path(r'^api/articles/(?P<pk>[0-9]+)/rendered/$', theme.article_ajax, name='article-ajax'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
