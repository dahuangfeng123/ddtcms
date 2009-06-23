from django.conf.urls.defaults import *


from ddtcms.polls.models import Poll

from ddtcms.home.views import common_dict
info_dict = {
    'queryset': Poll.objects.all(),
    'extra_context':common_dict,    
}

urlpatterns = patterns('',
    (r'^$',                               'django.views.generic.list_detail.object_list', info_dict),
    (r'^(?P<object_id>\d+)/$',            'django.views.generic.list_detail.object_detail', info_dict),
    url(r'^(?P<object_id>\d+)/results/$', 'django.views.generic.list_detail.object_detail', dict(info_dict, template_name='polls/results.html'), 'poll_results'),
    (r'^(?P<poll_id>\d+)/vote/$', 'ddtcms.polls.views.vote'),
)
