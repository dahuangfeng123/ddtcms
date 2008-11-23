#coding=utf-8
from django.template import loader, Context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from ddtcms.wiki.models import Wiki
from ddtcms.home.views import common_dict
import datetime


def index(request, pagename=""):
    """显示正常页面，对页面的文字做特殊的链接处理"""
    if pagename:
        #查找是否已经存在页面
#        pages = Wiki.objects.get_list(pagename__exact=pagename)
        pages = Wiki.objects.filter(pagename=pagename)
        if pages:
            # 存在则调用页面模板进行显示
            return process(request,'wiki/page.html',  pages[0])
        else:
            # 不存在则进入编辑画面
            return render_to_response('wiki/edit.html',{'pagename':pagename},context_instance=RequestContext(request))

    else:
#        page = Wiki.objects.get_object(pagename__exact='FrontPage')

        
        return render_to_response('wiki/index.html', common_dict,context_instance=RequestContext(request))
        #page = Wiki.objects.get(pagename='FrontPage')
        #if page:
        #    pass
        #else:
        #    page = Wiki(pagename='FrontPage', content='Welcome to Easy Wiki')
        #    page.save()
        #return process('wiki/page.html', page)


def edit(request, pagename):
    """显示编辑存在页面"""
#    page = Wiki.objects.get_object(pagename__exact=pagename)
    page = Wiki.objects.get(pagename=pagename)
    return render_to_response('wiki/edit.html', {'pagename':pagename, 'content':page.content},context_instance=RequestContext(request))

def save(request, pagename):
    """
    保存页面内容，老页面进行内容替换，新页面生成新记录
    """
    content = request.POST['content']
    pub_date= request.POST['pub_date']
    if pub_date:
        pass
    else:
        pub_date=datetime.datetime.now()

    
#    pages = Wiki.objects.get_list(pagename__exact=pagename)
    pages = Wiki.objects.filter(pagename=pagename)
    
    if pages:
        pages[0].content = content
        pages[0].save()
    else:
        page = Wiki(pagename=pagename, content=content,pub_date=pub_date,)
        page.save()
    return HttpResponseRedirect("/wiki/%s/" % pagename)

import re

r = re.compile(r'\b(([A-Z]+[a-z]+){2,})\b')
def process(request,template, page):
    """处理页面链接，并且将回车符转为<br>"""
    t = loader.get_template(template)
    content = r.sub(r'<a href="/wiki/\1/">\1</a>', page.content)
    content = re.sub(r'[\n\r]+', '<br>', content)
    c = Context({'pagename':page.pagename, 'content':content})
    #return HttpResponse(t.render(c))
    return render_to_response(template, 
                              {'pagename':page.pagename, 'content':content},
                              context_instance=RequestContext(request))