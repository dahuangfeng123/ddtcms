from django.conf.urls.defaults import *
from django.conf import settings



#urlpatterns = patterns('django.contrib.category.views',

#)

urlpatterns = patterns('',
    url(r'^cr/(\d+)/(\w+)/$', 'django.views.defaults.shortcut', name='category-url-redirect'),
)

