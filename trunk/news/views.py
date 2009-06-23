# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from ddtcms.home.views import common_dict

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
        
    return render_to_response('index.html',common_dict)


def post(request):
		return render_to_response('blog/blog_post.html',RequestContext(request, {'extra_context':common_dict,}))