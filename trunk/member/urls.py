from django.conf.urls.defaults import *
from ddtcms.home.views import common_dict
from ddtcms.member.models import Profile,Resume

common_dict.update({'app_label':'member',    })
    
    
member_dict = {
'queryset': Profile.objects.all(),
'extra_context':common_dict,
'template_name':'member/index.html',
}


pages_dict = {
'queryset': Profile.objects.all(),
'extra_context':common_dict,
'paginate_by':1,
}


urlpatterns = patterns('',
    (r'^$',                            'django.views.generic.list_detail.object_list', member_dict),


)
