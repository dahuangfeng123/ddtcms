from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.views.generic.simple import direct_to_template
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from ddtcms.blog.sitemaps import BlogSitemap
from ddtcms.blog.models import Entry

from userprofile.views import get_profiles


info_dict = {
    'queryset': Entry.objects.all(),
    'date_field': 'pub_date',
}

sitemaps = {
    'flatpages': FlatPageSitemap,
    'blog': BlogSitemap,
}






from ddtcms import settings

urlpatterns = patterns('',
    # Example:
    # (r'^ddtcms/', include('ddtcms.foo.urls')),
    (r'^',                     include('ddtcms.home.urls')),
    (r'^(?i)news/',            include('ddtcms.news.urls')),
    (r'^(?i)article/',         include('ddtcms.article.urls')),
    (r'^(?i)forum/',           include('ddtcms.forum.urls')),
    (r'^(?i)faq/',             include('ddtcms.faq.urls')),
    (r'^(?i)polls/',           include('ddtcms.polls.urls')),
    (r'^(?i)blog/',            include('ddtcms.blog.urls')),
    (r'^(?i)captcha/',         include('ddtcms.captcha.urls')),
    (r'^(?i)todo/',            include('ddtcms.todo.urls')),
    (r'^(?i)notice/',          include('ddtcms.notice.urls')),
    (r'^(?i)link/',            include('ddtcms.link.urls')),
    (r'^(?i)category/',        include('ddtcms.category.urls')),
    
    #(r'^(?i)member/',          include('ddtcms.profiles.urls')),
    #(r'^(?i)member/',          include('ddtcms.member.urls')),
    (r'^(?i)photologue/',      include('photologue.urls')),
    
    
    #(r'^blog/',    include('diario.urls.entries')),   
    
    (r'^accounts/', include('userprofile.urls')),
    #(r'^accounts/$', 'django.contrib.auth.views.login'),    
    (r'^accounts/$', direct_to_template, {'extra_context': { 'profiles': get_profiles }, 'template': 'member/front.html' }),
        
    #(r'^accounts/profile/$', 'django.views.generic.simple.direct_to_template',{'template':'registration/profile.html'}),
    
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


# Serves media content. WARNING!! Only for development uses.
# On production use lighthttpd for media content.
if settings.DEBUG:

    # Delete the first trailing slash, if any.
    if settings.MEDIA_URL.startswith('/'):
        media_url = settings.MEDIA_URL[1:]
    else:
        media_url = settings.MEDIA_URL

    # Add the last trailing slash, if have not.
    if not media_url.endswith('/'):
        media_url = media_url + '/'

    urlpatterns += patterns('',
        (r'^' + media_url + '(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}
        ),
    )