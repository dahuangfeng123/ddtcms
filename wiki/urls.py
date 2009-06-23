from django.conf.urls.defaults import *

from ddtcms.wiki.models import Wiki
from ddtcms.home.views import common_dict
common_dict.update({'app_label':'wiki',})
wiki_dict = {
'queryset': Wiki.objects.all(),
'date_field': 'pub_date',
'extra_context':common_dict,
}

urlpatterns = patterns('',
    #(r'^$', 'ddtcms.wiki.views.index'),
    (r'^$',                        'django.views.generic.date_based.archive_index', wiki_dict),
    (r'^(?P<pagename>\w+)/$',      'ddtcms.wiki.views.index'),
    (r'^(?P<pagename>\w+)/edit/$', 'ddtcms.wiki.views.edit'),
    (r'^(?P<pagename>\w+)/save/$', 'ddtcms.wiki.views.save'),
)
