from django.conf.urls.defaults import *
from ddtcms.home.views import common_dict
common_dict.update({'app_label':'article',})

from ddtcms.article.models import Article
news_dict = {
'queryset': Article.objects.all(),
'date_field': 'pub_date',
'extra_context':common_dict,
}


from ddtcms.blog.models import Tag
tag_dict = {
'queryset': Tag.objects.all(),
}

urlpatterns = patterns('',
    
    (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$', 'django.views.generic.date_based.object_detail', dict(news_dict,slug_field='slug')),
    (r'^$',                        'django.views.generic.date_based.archive_index', news_dict),
    (r'^tags/(?P<slug>[-\w]+)/$',  'django.views.generic.list_detail.object_detail',dict(tag_dict,slug_field='slug')),
    (r'^tags/$',                   'django.views.generic.list_detail.object_list',tag_dict),
)
