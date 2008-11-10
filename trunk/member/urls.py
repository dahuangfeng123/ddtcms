from django.conf.urls.defaults import *
from ddtcms.home.views import common_dict
from ddtcms.member.models import Profile,Resume

common_dict.update({'app_label':'member',    })
    
    
member_dict = {
'queryset': member.objects.all(),
'extra_context':common_dict,
}
member_dict.update({'date_field': 'pub_date',})

pages_dict = {
'queryset': member.objects.all(),
'extra_context':common_dict,
'paginate_by':1,
}


urlpatterns = patterns('',
    (r'^$',                            'django.views.generic.date_based.archive_index', member_dict),

)
