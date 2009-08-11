# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseServerError, HttpResponseForbidden, HttpResponseNotAllowed
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from ddtcms.news.models import News
from ddtcms.news.models import Category
from ddtcms.news.forms import NewsForm
from django.views.generic.list_detail import object_list

from django.views.generic.date_based import object_detail
from attachments.models import Attachment
from django.contrib.contenttypes.models import ContentType

from ddtcms.news.signals import latest_news_created
def by_tag(request,tag):
	qs = News.objects.all().filter(tags__contains=tag,pub_date__isnull=False)
	return object_list(request,qs,template_object_name='item')
	
def by_category(request,category_slug):
	#raise Http404(category_slug)
	
	the_category = get_object_or_404(Category.objects.all(), slug=category_slug)
	
	the_parent=the_category.parent
	
	#qs = News.objects.all().filter(category=the_category,pub_date__isnull=False)
	qs = News.objects.for_categories(category=the_category)
	
	if the_parent:
		child_categories=the_parent.get_children()
	else:
		child_categories=the_category.get_children()
		
	most_viewed_list = News.objects.get_published().order_by('-views')[:10]
	
	recommended_news     = News.objects.get_recommended()[:5]
		
	return object_list(request,qs,template_object_name='item',paginate_by=10,
						extra_context={'category':the_category,
							'child_categories':child_categories,
							"most_viewed_list":most_viewed_list,
							"recommended_news":recommended_news,})
	
def category_list(request,empty_arg):
	return object_list(request,Category.objects.all(),template_object_name='item')
	
#def by_author(request,author_slug):
#   the_author = get_object_or_404(NewsAuthor.on_site, slug=author_slug)
#   qs = NewsItem.on_site.filter(author=the_author,date__isnull=False)
#   return object_list(request,qs,template_object_name='item')
#   
#def author_list(request):
#   return object_list(request,NewsAuthor.on_site.all(),template_object_name='item')

def index(request):
	news_count = News.objects.all().count()
	news_list = News.objects.get_published()[:10]
	most_viewed_list = News.objects.get_published().order_by('-views')[:10]
	categories = Category.objects.all().filter(parent__exact=None)
	return render_to_response('news/news_index.html', locals(),
							  context_instance=RequestContext(request))
		

def view(request,year, month, day,slug):
	try:
		news=News.objects.all().get(slug=slug)
	except News.DoesNotExist:
		raise Http404
	news.views += 1
	news.save()
	
	most_viewed_list = News.objects.get_published().order_by('-views')[:10]
	recommended_news     = News.objects.get_recommended()[:5]
		
	the_category = get_object_or_404(Category.objects.all(), slug=news.category.slug)
	
	the_parent=the_category.parent
	
	if the_parent:
		child_categories=the_parent.get_children()
	else:
		child_categories=the_category.get_children()
		
	return object_detail(request, year, month, day, queryset=News.objects.all(), date_field='pub_date',slug=slug,
						extra_context={
						"most_viewed_list":most_viewed_list,
						"recommended_news":recommended_news,
						"child_categories":child_categories,})


@login_required
def post(request, category, success_url=None,
			 form_class=NewsForm,
			 template_name='news/news_post.html',
			 extra_context=None):	
	
	c = get_object_or_404(Category.objects.all(), slug=category)
	if request.method == 'POST':
		form = form_class(data=request.POST, files=request.FILES)
		if form.is_valid():
		    			
			n = News(
				title     =form.cleaned_data['title'],
				slug      =form.cleaned_data['slug'],
				deliverer =form.cleaned_data['deliverer'],
				category  =form.cleaned_data['category'],
				source    =form.cleaned_data['source'],
				content   =form.cleaned_data['content'],
				summary   =form.cleaned_data['summary'],					   
			)
			
			n.save()

			kwargs = {}
			kwargs['title']   = _("%s Posted A new News: %s") % (self.deliverer.username,self.title)
			kwargs['content'] = _("%s Posted A new News,go and view it now <a href='%s'> %s </a> " ) % (self.deliverer.username,self.get_absolute_url(),self.title)
			kwargs['slug']    = "news%d-%s" % (self.id,datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
			latest_news_created.send(sender=self.__class__,**kwargs)			


			for attachedfilefield in form.files:
				#attachment_file = form.files[attachedfilefield]
				#attach = Attachment()
				#attach.attached_by = request.user
				#attach.file        = attachment_file
				#attach.content_type = ContentType.objects.get_for_model(n)
				#attach.object_id   = n.id
				#attach.title       = attachment_file.name
				#attach.summary     = n.title
				#attach.file.save(attachment_file.name, attachment_file, save=False)
				#attach.save()

				attachment_file = form.files[attachedfilefield]
				attach = Attachment()
				attach.handle_uploaded_attachment(
					n,
					attachment_file,
					attached_by = request.user,
					title       = attachment_file.name,
					summary     = n.title
				)


				if attachedfilefield == u"file":
					if not n.pic:
						n.pic = attach.file_url()
						n.save()

			return HttpResponseRedirect(n.get_absolute_url())
			
			#return HttpResponseRedirect(success_url or reverse('news-index'))
	else:
		form = form_class(initial={'category':c.id, 'deliverer':request.user.id})
		#form = form_class()
	
	if extra_context is None:
		extra_context = {}
	context = RequestContext(request)
	for key, value in extra_context.items():
		context[key] = callable(value) and value() or value
	return render_to_response(template_name,
							  { 'form': form,
							    'category':c,
							  },
							  context_instance=context)