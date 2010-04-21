from django.conf.urls.defaults import *


from ddtcms.link.models import Link


info_dict = {
    'queryset': Link.objects.all(),
}

urlpatterns = patterns('',
    (r'^$',                               'django.views.generic.list_detail.object_list', info_dict),
    (r'^(?P<object_id>\d+)/$',            'django.views.generic.list_detail.object_detail', info_dict),
    #(r'^(?P<object_id>\d+)/$',            'django.views.generic.list_detail.object_detail', info_dict),
)

urlpatterns = patterns('ddtcms.link.views',
	url(r'^$',                          'index',       name="link_index"),
	url(r'^add/$',                      'link_create', name="link_create"),
	url(r'^(?P<object_id>\d+)/$',       'link_detail', name="link_detail"),
	url(r'^(?P<object_id>\d+)/edit/$',  'link_change', name="link_change"),
	url(r'^(?P<object_id>\d+)/del/$',   'link_delete', name="link_delete"),
	url(r'^import/$',                   'link_import', name='link_import'),
    url(r'^export/$',                   'link_export', name='link_export'),
)
