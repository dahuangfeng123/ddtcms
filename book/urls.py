from django.conf.urls.defaults import *


from ddtcms.book.models import Book

from ddtcms.home.views import common_dict
info_dict = {
    'queryset': Book.objects.all(),
    'extra_context':common_dict,    
}

urlpatterns = patterns('',
    (r'^$',                               'django.views.generic.list_detail.object_list', info_dict),
    (r'^(?P<object_id>\d+)/$',            'django.views.generic.list_detail.object_detail', info_dict),
)
