from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('attachments.views',
    url(r'^newattachment/(?P<content_type>\d+)/(?P<object_id>\d+)/$', 'new_attachment',        name='attachment_new'),
    url(r'^deleteattachment/(?P<attachment_slug>[-\w]+)$',            'delete_attachment',     name='attachment_delete'),
    url(r'^ajaxdeleteattachment/',                                    'attachment_ajaxdelete', name='ajaxdelete_attachment'),
)