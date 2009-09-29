# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

from ddtcms.home.views import common_dict
from ddtcms.blog.models import Blog
from ddtcms.blog.forms import CreateBlogForm

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
        
    return render_to_response('blog/index.html',{},context_instance=RequestContext(request))


def post(request, success_url=None,
             form_class=CreateBlogForm,
             template_name='blog/blog_post.html',
             extra_context=None):
    
    if request.method == 'POST':
        form = form_class(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_user = form.save(profile_callback=profile_callback)
            # success_url needs to be dynamically generated here; setting a
            # a default value using reverse() will cause circular-import
            # problems with the default URLConf for this application, which
            # imports this file.
            return HttpResponseRedirect(success_url or reverse('registration_complete'))
    else:
        form = form_class()
    
    if extra_context is None:
        extra_context = {}
    context = RequestContext(request)
    for key, value in extra_context.items():
        context[key] = callable(value) and value() or value
    return render_to_response(template_name,
                              { 'form': form,
                                'extra_context':common_dict,},
                              context_instance=context)
                              
                         
