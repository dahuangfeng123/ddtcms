from django.conf.urls.defaults import *
from ddtcms.photo.models import Photo
from ddtcms.home.views import common_dict
info_dict = {
'queryset': Photo.objects.all(),
'template_name': 'photo/photo_list.html',
'extra_context':common_dict,    
}

urlpatterns = patterns('',
    (r'^$',           'django.views.generic.list_detail.object_list',info_dict),
    (r'^upload/$','ddtcms.photo.views.upload'),
    (r'^photo/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\w{1,2})/$',     'django.views.generic.date_based.archive_day', dict(info_dict,month_format='%m')),
)
