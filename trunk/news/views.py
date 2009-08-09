# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from ddtcms.news.models import News
from ddtcms.news.models import Category
from ddtcms.news.forms import NewsCreateForm
from django.views.generic.list_detail import object_list

from django.views.generic.date_based import object_detail


def by_tag(request,tag):
	qs = News.objects.all().filter(tags__contains=tag,pub_date__isnull=False)
	return object_list(request,qs,template_object_name='item')
	
def by_category(request,category_slug):
	the_category = get_object_or_404(Category.objects.all(), slug=category_slug)
	qs = News.objects.all().filter(category=the_category,pub_date__isnull=False)
	return object_list(request,qs,template_object_name='item',extra_context={'category':the_category})
	
def category_list(request,empty_arg):
	return object_list(request,Category.objects.all(),template_object_name='item')
	
#def by_author(request,author_slug):
#	the_author = get_object_or_404(NewsAuthor.on_site, slug=author_slug)
#	qs = NewsItem.on_site.filter(author=the_author,date__isnull=False)
#	return object_list(request,qs,template_object_name='item')
#	
#def author_list(request):
#	return object_list(request,NewsAuthor.on_site.all(),template_object_name='item')

def index(request):
    news_list = News.objects.all()[:5]
    categories = Category.objects.all()[:6]
    return render_to_response('news/news_index.html', locals(),
                              context_instance=RequestContext(request))
        

def view(request,year, month, day,slug):
	news=News.objects.all().get(slug=slug)
	news.views += 1
	news.save()
    
	return object_detail(request, year, month, day, queryset=News.objects.all(), date_field='pub_date',slug=slug)



def post(request, success_url=None,
             form_class=NewsCreateForm,
             template_name='news/news_post.html',
             extra_context=None):
    
    if request.method == 'POST':
        form = form_class(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_news = form.save()
            
            return HttpResponseRedirect(success_url or reverse('news-index'))
    else:
        form = form_class()
    
    if extra_context is None:
        extra_context = {}
    context = RequestContext(request)
    for key, value in extra_context.items():
        context[key] = callable(value) and value() or value
    return render_to_response(template_name,
                              { 'form': form },
                              context_instance=context)