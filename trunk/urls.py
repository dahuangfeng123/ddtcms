from django.conf.urls.defaults import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from mysite.blog.sitemaps import BlogSitemap
from mysite.blog.models import Entry

info_dict = {
    'queryset': Entry.objects.all(),
    'date_field': 'pub_date',
}

sitemaps = {
    'flatpages': FlatPageSitemap,
    'blog': BlogSitemap,
}






from mysite import settings

urlpatterns = patterns('',
    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),
    (r'^',                include('mysite.home.urls')),
    (r'^(?i)news/',       include('mysite.news.urls')),
    (r'^(?i)article/',    include('mysite.article.urls')),
    (r'^(?i)photo/',      include('mysite.photo.urls')),
    (r'^(?i)forum/',      include('mysite.forum.urls')),
    (r'^(?i)faq/',        include('mysite.faq.urls')),
    (r'^(?i)wiki/',       include('mysite.wiki.urls')),
    (r'^(?i)polls/',      include('mysite.polls.urls')),
    (r'^(?i)blog/',       include('mysite.blog.urls')),
    (r'^(?i)captcha/',    include('mysite.captcha.urls')),
    (r'^(?i)todo/',       include('mysite.todo.urls')),
    (r'^(?i)notice/',     include('mysite.notice.urls')),
    (r'^(?i)profiles/',   include('mysite.profiles.urls')),
    
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