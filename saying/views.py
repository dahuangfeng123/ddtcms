from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseServerError, HttpResponseForbidden, HttpResponseNotAllowed
from django.views.generic.list_detail import object_list
from django.views.generic.date_based import object_detail

def index(request):
	return HttpResponse("")

def post(request):
	return HttpResponse("")

def view(request):
	return HttpResponse("")

def by_tag(request,tag):
	return HttpResponse("")