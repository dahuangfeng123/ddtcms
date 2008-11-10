from django.conf.urls.defaults import *


urlpatterns = patterns('',
    (r'^$',         'ddtcms.home.views.index'),
    (r'^add/$',     'ddtcms.home.add.index'),
    (r'^list/$',    'ddtcms.home.views.list'),
    #(r'^list/$',    'ddtcms.home.list.index'),
    #(r'^login/$',  'ddtcms.home.login.login'),
    #(r'^logout/$', 'ddtcms.home.login.logout'),
)
