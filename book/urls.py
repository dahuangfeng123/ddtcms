from django.conf.urls.defaults import *


from ddtcms.book.models import Book


info_dict = {
    'queryset': Book.objects.all(),
}

urlpatterns = patterns('',
    (r'^$',                               'django.views.generic.list_detail.object_list', info_dict),
    (r'^(?P<object_id>\d+)/$',            'django.views.generic.list_detail.object_detail', info_dict),
)
