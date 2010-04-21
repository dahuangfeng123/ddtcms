from django.conf.urls.defaults import *
from tagging.models import Tag
from ddtcms.people.models import Person
info_dict = {
'queryset': Person.objects.all(),
}



urlpatterns = patterns('',

    (r'^$',   'django.views.generic.list_detail.object_list', info_dict),
    url(r'^(?P<object_id>\d+)/$',       'django.views.generic.list_detail.object_detail',dict(info_dict), name="person_detail"),


)

#urlpatterns = patterns('ddtcms.XXXXX.views',
#	url(r'^$',                          'index',        name="XXXXX_index"),
#	url(r'^add/$',                      'XXXXX_create', name="XXXXX_create"),
#	url(r'^(?P<object_id>\d+)/$',       'XXXXX_detail', name="XXXXX_detail"),
#	url(r'^(?P<object_id>\d+)/edit/$',  'XXXXX_change', name="XXXXX_change"),
#	url(r'^(?P<object_id>\d+)/del/$',   'XXXXX_delete', name="XXXXX_delete"),
#)
