from django.conf.urls.defaults import *
from tagging.models import Tag
from ddtcms.saying.models import Saying
saying_dict = {
'queryset': Saying.objects.all(),
'date_field': 'pub_date',
}

tag_dict = {
'queryset': Tag.objects.all(),
}

urlpatterns = patterns('django.views.generic',

    (r'^$',   'date_based.archive_index', saying_dict),
	url(r'^(?P<object_id>\d+)/$', 'list_detail.object_detail', saying_dict, name="saying-item-id"),
	url(r'^tags/$',               'list_detail.object_list',   tag_dict),
)

urlpatterns += patterns('saying.views',
    #(r'^$',   'date_based.archive_index', saying_dict),
	#url(r'^$', 'index', name="saying-index"),
	url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$', 
	                             'view',   name="saying-item"),
	url(r'^tags/(?P<tag>.+)/$',  'by_tag', name='saying-by-tag'),
	url(r'^post/$',              'post',   name='saying-post'),
)