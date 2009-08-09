from django.conf.urls.defaults import *
from tagging.models import Tag
from ddtcms.people.models import Person
news_dict = {
'queryset': Person.objects.all(),
}



urlpatterns = patterns('',

    (r'^$',   'django.views.generic.list_detail.object_list', news_dict),


)
