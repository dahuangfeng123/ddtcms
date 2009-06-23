from django.conf.urls.defaults import *
from ddtcms.faq.models import Faq
faq_dict = {
'queryset': Faq.objects.all(),
}


urlpatterns = patterns('',
    (r'^$',                   'django.views.generic.date_based.archive_index', dict(faq_dict,date_field='pub_date')),
    (r'^(?P<slug>[-\w]+)/$',  'django.views.generic.list_detail.object_detail',dict(faq_dict,slug_field='slug')),
)
