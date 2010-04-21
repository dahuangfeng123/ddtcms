from django.conf.urls.defaults import *
from ddtcms.notice.models import Notice
info_dict = {
'queryset': Notice.objects.all(),
}


urlpatterns = patterns('django.views.generic',
    (r'^$',                   'date_based.archive_index', dict(info_dict,date_field='pub_date')),
    (r'^(?P<slug>[-\w]+)/$',  'list_detail.object_detail',dict(info_dict,slug_field='slug')),
)
