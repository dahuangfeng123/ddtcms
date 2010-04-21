# -*- coding: utf-8 -*-
#python.
import os

#django.
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.comments.models import Comment

from django.views.static import serve
from django.conf import settings

#3dpart.

#ddtcms.
from blog.models       import Blog
from link.models       import Link
from member.forms      import RegistrationForm
from news.models       import News,Category
from notice.models     import Notice
from polls.models      import Poll
from photologue.models import Photo
from tagging.models    import Tag





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
    links           = Link.objects.all()[:15]
    #pic_news_list   = News.objects.all().filter(pic__isnull=False)[:5]
    pic_news_list   = News.objects.all().exclude(pic="")[:5]
    try:
        top_headline    = News.objects.get_headlines().latest('id')
    except News.DoesNotExist:
        top_headline = None
    
    headline_news_list   = News.objects.get_headlines()[1:5]
    notice_list     = Notice.objects.all()[:3]
    try:
    	poll  = Poll.objects.all().latest('id')
    except Poll.DoesNotExist:
        poll  = None
    latest_photos      = Photo.objects.all()[:10]
    latest_login_users = User.objects.all().order_by('-last_login')[:6]
    
    #latest_news     = News.objects.all().filter(headline__exact=False)[:10]
    latest_news      = News.objects.get_published()[:6]
    recommended_news = News.objects.get_recommended()[:5]
    flashslide_news  = News.objects.get_flashslide()[:5]
    most_viewed_list = News.objects.get_published().order_by('-views')[:10]
    
    latest_comments  = Comment.objects.all()[:5]    
    categories       = Category.objects.all().filter(parent__exact=None)
    
    if request.user.is_authenticated():
        username = request.session.get('username', None)
        content=' 认证的用户'
    else:
        content='  匿名用户'
        
    #form = RegistrationForm()
    test=['新闻','论坛','ccc','ddd','eee','fff']
       
    return render_to_response('home/index.html',
                            {"links":links,
                            "pic_news_list":pic_news_list,
                            "notice_list":notice_list,
                            "top_headline":top_headline,
                            "headline_news_list":headline_news_list,
                            "latest_photos":latest_photos,
                            "latest_news":latest_news,
                            "recommended_news":recommended_news,
                            "latest_comments":latest_comments,
                            "flashslide_news":flashslide_news,
                            "most_viewed_list":most_viewed_list,
                            "latest_login_users":latest_login_users,
                            "categories":categories,
                            "poll":poll,
                            "test":test,
                            },context_instance=RequestContext(request))
        
#    return render_to_response('index.html',{'sitename':'网站正在建设中。。。'})

def favicon(request):
  path='favicon.ico'
  document_root=settings.STATIC_IMAGE
  fullpath = os.path.join(document_root, path)
  #debug()
  return serve(request,path=path,document_root=settings.STATIC_IMAGE)
    
    
