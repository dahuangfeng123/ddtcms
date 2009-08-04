# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext

from ddtcms.blog.models import Entry
from ddtcms.notice.models import Notice

common_dict={
    "sitename":"我的网站测试中。。。",
    "sitedomain":"127.0.0.1",
    'app_label':'',
    'notice_list':Notice.objects.all()[:2],
}
    


def index(request):
#    return HttpResponse("Hello, Django.")
#    if not request.user.is_authenticated():
#        return HttpResponseRedirect('/login/?next=%s' % request.path)

    content='fffffffff'
    username='amouysuser'
    if request.user.is_authenticated():
        username = request.session.get('username', None)
        content=' 认证的用户'
    else:
        content='  匿名用户'
        
    return render_to_response('index.html',
        {},
        context_instance=RequestContext(request))
        
#    return render_to_response('index.html',{'sitename':'网站正在建设中。。。'})

def list(request):
  latest_post_list = Entry.objects.all()
  return render_to_response('index.html',{'latest_post_list': latest_post_list})

def register(request):
  return render_to_response('register.html','') 

def login(request):
  return render_to_response('login.html','') 

def logout(request):
  return HttpResponse("""you've logout from vill""")