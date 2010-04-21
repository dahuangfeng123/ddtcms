from django.conf.urls.defaults import *
from ddtcms.home.views import common_dict
from ddtcms.blog.models import Blog
from ddtcms.blog.models import Category

common_dict.update({'app_label':'blog',
    'latest_Blog_list':Blog.objects.all()[:5],
    'category_list'  : Category.objects.all(),
        
    })

    
    
    
    
blog_dict = {
'queryset': Blog.objects.all(),
'extra_context':common_dict,
}



category_dict = {
'queryset': Category.objects.all(),
'extra_context':common_dict,
}





pages_dict = {
'queryset': Blog.objects.all(),
'paginate_by':3,
}

archive_dict={}
archive_dict.update(blog_dict)
archive_dict.update({'date_field': 'pub_date',})
    





from django.core.paginator import Paginator, InvalidPage

#
# paginator = Paginator(Blog.objects.all().order_by('-pub_date'), 3)
#  latest_post_list = paginator.page(1).object_list
#  catalog_list = Category.objects.all()  
#  page_list = [i for i in paginator.page_range ]
#  return render_to_response('blog_index.html',{
#    'latest_post_list': latest_post_list,
#    'catalog_list': catalog_list,
#    'blog_roll': blog_roll,
#    'page_list': page_list,
#    })


urlpatterns = patterns('django.views.generic',
    (r'^page/(?P<page>\w+)/$',          'list_detail.object_list', pages_dict),

    (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$', 'date_based.object_detail', dict(archive_dict,slug_field='slug')),
    (r'^category/$',                    'list_detail.object_list',category_dict),
    (r'^category/(?P<slug>[-\w]+)/$',   'list_detail.object_detail',dict(category_dict,slug_field='slug')),
    (r'^archive/$',                     'date_based.archive_index', archive_dict),
    (r'^archive/(?P<year>\d{4})/$',     'date_based.archive_year', archive_dict),
    (r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/$',                      'date_based.archive_month', dict(archive_dict,month_format='%m')),
    (r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\w{1,2})/$',     'date_based.archive_day', dict(archive_dict,month_format='%m')),
)

urlpatterns += patterns('ddtcms.blog.views',
    (r'^$',                            'index'),
    (r'^post/$',                       'post'),
)
