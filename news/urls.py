from django.conf.urls.defaults import *
from tagging.models import Tag
from ddtcms.news.models import News,Category
import news.views.default as news_views

try:
	PAGINATE = settings.NEWS_PAGINATE_BY
except:
	PAGINATE = 8

news_dict = {
'queryset': News.objects.all(),
'extra_context':{'categories':Category.objects.all()}
}

news_date_dict = dict(news_dict, date_field='pub_date')

tag_dict = {
'queryset': Tag.objects.all(),
}

#urlpatterns = patterns('',
#
#    (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$', 'django.views.generic.date_based.object_detail', dict(news_dict,slug_field='slug')),
#    (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$', 'ddtcms.news.views.view'),
#    (r'^$',                        'django.views.generic.date_based.archive_index', news_dict),
#    (r'^$',                        'ddtcms.news.views.index'),
#    url(r'^tags/(?P<slug>[-\w]+)/$',  'django.views.generic.list_detail.object_detail',dict(tag_dict,slug_field='slug')),
#    
#)

urlpatterns = patterns('django.views.generic.date_based',
	url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<object_id>\d+)/$', 'object_detail', news_date_dict, name="news-item-id"),
	#url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$', 'object_detail', news_date_dict, name="news-item"),
	url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$', 'archive_day', news_date_dict),
	url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', 'archive_month', news_date_dict),
	url(r'^(?P<year>\d{4})/$', 'archive_year',  dict(news_date_dict, make_object_list=True)),

)
urlpatterns += patterns('django.views.generic.list_detail',
	#url(r'^$', 'object_list', dict(news_dict, paginate_by=PAGINATE,template_name='news/news_index.html'), name="news-index"),
)

urlpatterns += patterns('',
	url(r'^$', news_views.index,name="news-index"),
	url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$', news_views.view, name="news-item"),
	url(r'^(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', news_dict, name="news-item-id"),
	url(r'^tags/$','django.views.generic.list_detail.object_list',tag_dict),
	url(r'^post/$', news_views.post,name='news-post'),
	url(r'^tag/(?P<tag>.+)/$',news_views.by_tag,name='news-by-tag'),
	#url(r'^category/(?P<category_slug>.+)/$',news_views.by_category,name='news-by-category'),
	url(r'^categor(y|ies)/$',news_views.category_list,name='news-categories'),
	#url(r'^authors/(?P<author_slug>.+)/$',news_views.by_author,name='news-by-author'),
	#url(r'^authors/$',news_views.author_list,name='news-authors'),
	
	url(r'^(?P<category_slug>[-\w]+)/$',news_views.by_category,name='news-by-category'),
    url(r'^(?P<category>[-\w]+)/post/$', news_views.post, name='news-newitem'),
    url(r'^([-\w/]+/)(?P<category>[-\w]+)/post/$', news_views.post),
	url(r'^([-\w/]+/)(?P<category_slug>[-\w]+)/$', news_views.by_category, name='news-by-subcategory'),
	
	#url(r'^category/(?P<category_slug>.+)/$',news_views.by_category,name='news-by-category'),
	#url(r'^categor(y|ies)/$',news_views.category_list,name='news-categories'),
	#url(r'^authors/(?P<author_slug>.+)/$',news_views.by_author,name='news-by-author'),
	#url(r'^authors/$',news_views.author_list,name='news-authors'),
)