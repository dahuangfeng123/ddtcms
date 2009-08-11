# -*- coding: utf-8 -*-
from datetime import datetime
from django.shortcuts import get_object_or_404, render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseServerError, HttpResponseForbidden, HttpResponseNotAllowed
from django.template import RequestContext, Context, loader
from django import forms
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.defaultfilters import striptags, wordwrap
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.views.generic.list_detail import object_list

import urllib

from link.models import Link
from link.forms import CreateLinkForm
from django.contrib.auth.decorators import login_required

#@login_required
def newlink(request):
	"""
	Rudimentary post function - this should probably use 
	newforms, although not sure how that goes when we're updating 
	two models.

	Only allows a user to post if they're logged in.
	"""
	if not request.user.is_authenticated():
		#return HttpResponseServerError()
		return HttpResponseForbidden()

	if request.method == 'POST':
		form = CreateLinkForm(request.POST)
		if form.is_valid():
			linktitle =form.cleaned_data['title']            
			url       =form.cleaned_data['url']    
			desc      =form.cleaned_data['description']
			s = Link(title=linktitle,url=url,notes=desc)
			s.save()
			
			#return HttpResponseRedirect(s.get_absolute_url())
			return HttpResponseRedirect("/link/")
	else:
		
		#t=urllib.unquote(request.GET.get('t', 'title not set')).decode('utf8')
		#t=urllib.unquote(request.GET.get('t', 'title not set'))
		t=request.GET.get('t', 'title not set')
		u=request.GET.get('u', 'url not set')
		c=request.GET.get('c', 'title not set')

		form = CreateLinkForm(initial={ 'title': t,
										'url': u,
										'description': c
									})

	msg=request.method
	return render_to_response('link/newlink.html',
		RequestContext(request, {
			'form': form,
			'msg':msg,
		}))
