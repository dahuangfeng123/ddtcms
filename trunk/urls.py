from django.conf.urls.defaults import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from ddtcms.blog.sitemaps import BlogSitemap
from ddtcms.blog.models import Entry

info_dict = {
    'queryset': Entry.objects.all(),
    'date_field': 'pub_date',
}

sitemaps = {
    'flatpages': FlatPageSitemap,
    'blog': BlogSitemap,
}






from ddtcms  import settings

urlpatterns = patterns('',
    # Example:
    # (r'^mysite/', include('ddtcms.foo.urls')),
    (r'^',                include('ddtcms.home.urls')),
    (r'^(?i)news/',       include('ddtcms.news.urls')),
    (r'^(?i)article/',    include('ddtcms.article.urls')),
    (r'^(?i)photo/',      include('ddtcms.photo.urls')),
    (r'^(?i)forum/',      include('ddtcms.forum.urls')),
    (r'^(?i)faq/',        include('ddtcms.faq.urls')),
    (r'^(?i)wiki/',       include('ddtcms.wiki.urls')),
    (r'^(?i)polls/',      include('ddtcms.polls.urls')),
    (r'^(?i)blog/',       include('ddtcms.blog.urls')),
    (r'^(?i)captcha/',    include('ddtcms.captcha.urls')),
    (r'^(?i)todo/',       include('ddtcms.todo.urls')),
    (r'^(?i)notice/',     include('ddtcms.notice.urls')),
    (r'^(?i)profiles/',   include('ddtcms.profiles.urls')),
    (r'^(?i)book/',   include('ddtcms.book.urls')),
    
    #(r'^blog/',    include('diario.urls.entries')),   
    
    (r'^accounts/', include('registration.urls')),
    (r'^accounts/$', 'django.contrib.auth.views.login'),
    (r'^accounts/profile/$', 'django.views.generic.simple.direct_to_template',{'template':'registration/profile.html'}),
    
    # serve static medias
    (r'^media/(?P<path>.*)$',   'django.views.static.serve',{'document_root': settings.STATIC_PATH}),
    (r'^styles/(?P<path>.*)$',  'django.views.static.serve',{'document_root': settings.STATIC_STYLE}),
    (r'^scripts/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_SCRIPT}),
    (r'^images/(?P<path>.*)$',  'django.views.static.serve',{'document_root': settings.STATIC_IMAGE}),
    (r'^upload/(?P<path>.*)$',   'django.views.static.serve',{'document_root': settings.STATIC_FILE_UPLOAD_DIR}),
        
    (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),    
    #(r'^sitemap.xml$', 'django.contrib.sitemaps.views.index', {'sitemaps': sitemaps}),
    (r'^sitemap-(?P<section>.+).xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    
    # user django comments system    
    (r'^comments/', include('django.contrib.comments.urls')),

    # Uncomment this for admin0.96:
    #(r'^admin/', include('django.contrib.admin.urls')),
    
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/docs/', include('django.contrib.admindocs.urls')),
    
    # Uncomment the next line to enable the admin1.0beta:
    (r'^admin/(.*)', admin.site.root),


)