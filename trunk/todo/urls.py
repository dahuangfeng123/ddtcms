from django.conf.urls.defaults import *
from ddtcms.home.views import common_dict
from ddtcms.todo.models import Todo

common_dict.update({'app_label':'blog',    })

    
    
    
    
todo_dict = {
'queryset': Todo.objects.all(),
'extra_context':common_dict,
}
todo_dict.update({'date_field': 'pub_date',})

pages_dict = {
'queryset': Todo.objects.all(),
'extra_context':common_dict,
'paginate_by':1,
}


urlpatterns = patterns('',
    (r'^$',                            'django.views.generic.date_based.archive_index', todo_dict),

)
