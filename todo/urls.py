from django.conf.urls.defaults import *
from ddtcms.home.views import common_dict
from ddtcms.todo.models import Project

common_dict.update({'app_label':'blog',    })

    
    
    
    
todo_dict = {
'queryset': Project.objects.all().filter(type__exact=0),
'extra_context':common_dict,
}
todo_dict.update({'date_field': 'pub_date',})

pages_dict = {
'queryset': Project.objects.all(),
'extra_context':common_dict,
'paginate_by':1,
}


urlpatterns = patterns('',
    #url(r'^$','todo.views.index',name='todo'),
    #(r'^$',                   'django.views.generic.date_based.archive_index', todo_dict),
    url(r'^$',             'todo.views.index',name='todo-index'),
    url(r'^manage/$',             'todo.views.manage',name='todo-manage'),
    (r'^(?P<object_id>\d+)/$',      'django.views.generic.list_detail.object_detail', dict(queryset=Project.objects.all())),
    (r'^(?P<slug>[-\w]+)/$',   'django.views.generic.list_detail.object_detail', dict(queryset=Project.objects.all(),slug_field='slug')),
    (r'^task/add/',            'todo.views.task_add'),
    (r'^task/done/',           'todo.views.task_done'),
    (r'^task/undone/',         'todo.views.task_undone'),
    (r'^task/delete/',         'todo.views.task_del'),
    (r'^project/add/',         'todo.views.project_add'),
    (r'^project/delete/',      'todo.views.project_del'),
    (r'^project/change_type/', 'todo.views.project_chg_type'),
    
)