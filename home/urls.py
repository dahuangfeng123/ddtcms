from django.conf.urls.defaults import *


urlpatterns = patterns('ddtcms.home.views',
    (r'^$',                    'index'),
    (r'^(?i)favicon.ico$',     'favicon'),  
)
