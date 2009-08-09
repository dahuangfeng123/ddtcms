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

urlpatterns = patterns('',

    (r'^$',   'django.views.generic.date_based.archive_index', saying_dict),


)

urlpatterns = patterns('',
  #(r'^$',   'django.views.generic.date_based.archive_index', saying_dict),
	url(r'^$', 'saying.views.index', name="saying-index"),
	url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$', "saying.views.view", name="saying-item"),
	url(r'^(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', saying_dict, name="saying-item-id"),
	url(r'^tags/$','django.views.generic.list_detail.object_list',tag_dict),
	url(r'^tags/(?P<tag>.+)/$','saying.views.by_tag',name='saying-by-tag'),
	url(r'^post/$', 'saying.views.post',name='saying-post'),
)