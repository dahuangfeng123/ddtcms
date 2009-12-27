from django.conf.urls.defaults import *


urlpatterns = patterns('',
    (r'^$',         'ddtcms.home.views.index'),
    (r'^(?i)favicon.ico$',     'ddtcms.home.views.favicon'),  
    #(r'^list/$',    'ddtcms.home.list.index'),
    #(r'^login/$',  'ddtcms.home.login.login'),
    #(r'^logout/$', 'ddtcms.home.login.logout'),
)
