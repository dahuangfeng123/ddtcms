from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.views.generic.simple import direct_to_template
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from ddtcms.blog.sitemaps import BlogSitemap
from ddtcms.blog.models import Blog

from ddtcms.member.views import get_profiles


from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect

def export_selected_objects(modeladmin, request, queryset):
    selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
    ct = ContentType.objects.get_for_model(queryset.model)
    return HttpResponseRedirect("/export/?ct=%s&ids=%s" % (ct.pk, ",".join(selected)))

admin.site.add_action(export_selected_objects)

info_dict = {
    'queryset': Blog.objects.all(),
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
    (r'^(?i)saying/',          include('ddtcms.saying.urls')),
    (r'^(?i)forum/',           include('ddtcms.forum.urls')),
    (r'^(?i)faq/',             include('ddtcms.faq.urls')),
    (r'^(?i)polls/',           include('ddtcms.polls.urls')),
    (r'^(?i)blog/',            include('ddtcms.blog.urls')),
    (r'^(?i)book/',            include('ddtcms.book.urls')),
    (r'^(?i)captcha/',         include('ddtcms.captcha.urls')),
    (r'^(?i)notice/',          include('ddtcms.notice.urls')),
    (r'^(?i)link/',            include('ddtcms.link.urls')),
    (r'^(?i)people/',          include('ddtcms.people.urls')),
    (r'^(?i)todo/',            include('ddtcms.todo.urls')),
    (r'^(?i)guestbook/',       include('ddtcms.guestbook.urls')),
    
    (r'^(?i)member/',          include('ddtcms.member.urls')),
    (r'^(?i)member/$',         direct_to_template, {'extra_context': { 'profiles': get_profiles }, 'template': 'member/front.html' }),
    
    (r'^(?i)photologue/',      include('photologue.urls')),
    (r'^(?i)photologue/$',     direct_to_template, {'template': 'photologue/index.html' }),

    (r'^(?i)attachments/',     include('attachments.urls')),
    (r'^(?i)tags/',            include('tagging.urls')),
    
    
    # serve static medias
    (r'^(?i)media/(?P<path>.*)$',      'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    (r'^(?i)themes/(?P<path>.*)$',     'django.views.static.serve',{'document_root': settings.STATIC_THEMES}),
    (r'^(?i)images/(?P<path>.*)$',     'django.views.static.serve',{'document_root': settings.STATIC_IMAGE}),
    (r'^(?i)css/(?P<path>.*)$',        'django.views.static.serve',{'document_root': settings.STATIC_CSS}),	
    (r'^(?i)js/(?P<path>.*)$',         'django.views.static.serve',{'document_root': settings.STATIC_JS}),    		
    (r'^(?i)upload/(?P<path>.*)$',     'django.views.static.serve',{'document_root': settings.STATIC_UPLOAD}),
    (r'^(?i)editor/(?P<path>.*)$',     'django.views.static.serve',{'document_root': settings.STATIC_EDITOR}),
    (r'^(?i)attachment/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_UPLOAD+"attachment/"}),
    
    	    
    (r'^(?i)sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),    
    (r'^(?i)sitemap-(?P<section>.+).xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    
    # user django comments system    
    (r'^(?i)comments/', include('django.contrib.comments.urls')),
    
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),


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