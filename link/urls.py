from django.conf.urls.defaults import *


from ddtcms.link.models import Link


info_dict = {
    'queryset': Link.objects.all(),
}

urlpatterns = patterns('',
    (r'^$',                               'django.views.generic.list_detail.object_list', info_dict),
    (r'^(?P<object_id>\d+)/$',            'django.views.generic.list_detail.object_detail', info_dict),
    #(r'^(?P<object_id>\d+)/$',            'django.views.generic.list_detail.object_detail', info_dict),
    url(r'^new/$', 'link.views.newlink',name='newlink'),
)