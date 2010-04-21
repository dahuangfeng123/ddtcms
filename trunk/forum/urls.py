"""
URLConf for Django-Forum.

django-forum assumes that the forum application is living under
/forum/.

Usage in your base urls.py:
    (r'^forum/', include('forum.urls')),

"""

from django.conf.urls.defaults import *
from forum.models import Forum
from forum.feeds import RssForumFeed, AtomForumFeed
from forum.sitemap import ForumSitemap, ThreadSitemap, PostSitemap

feed_dict = {
    'rss' : RssForumFeed,
    'atom': AtomForumFeed
}

sitemap_dict = {
    'forums': ForumSitemap,
    'threads': ThreadSitemap,
    'posts': PostSitemap,
}

urlpatterns = patterns('',
    
    url(r'^(?P<url>(rss|atom).*)/$',    'django.contrib.syndication.views.feed', {'feed_dict': feed_dict}),
    (r'^sitemap.xml$',                  'django.contrib.sitemaps.views.index', {'sitemaps': sitemap_dict}),
    (r'^sitemap-(?P<section>.+)\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemap_dict}),

)

urlpatterns += patterns('forum.views',
    url(r'^$',                            'forums_list', name='forum_index'),
    url(r'^search/(?P<q>[ \w]+)/$',            'search', name='forum_search_thread'),
    
    url(r'^thread/(?P<thread>[0-9]+)/$',       'thread', name='forum_view_thread'),
    url(r'^thread/(?P<thread>[0-9]+)/reply/$', 'reply',  name='forum_reply_thread'),
    url(r'^thread/(?P<thread>[0-9]+)/edit/$',  'edit',   name='forum_edit_thread'),

    url(r'^subscriptions/$',         'updatesubs', name='forum_subscriptions'),

    url(r'^(?P<slug>[-\w]+)/$',      'forum',     name='forum_thread_list'),
    url(r'^(?P<forum>[-\w]+)/new/$', 'newthread', name='forum_new_thread'),

    url(r'^([-\w/]+/)(?P<forum>[-\w]+)/new/$', 'newthread'),
    url(r'^([-\w/]+/)(?P<slug>[-\w]+)/$',      'forum', name='forum_subforum_thread_list'),
    #url(r'^archives/$',                       'forums_archives', name='forum_archives'),
)
