#coding=utf-8
from django.utils.translation import ugettext as _
from todo.models import Project,Task,TASK_PRIORITY,PROJECT_TYPE
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import get_object_or_404,get_list_or_404,render_to_response
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
import datetime
@staff_member_required
def manage(request):
    '''todo homepage'''
    is_auth = request.user.is_authenticated()
    #not completed projects
    if is_auth:
        projects = Project.objects.extra(where=['tasks = 0 or tasks <> completed '])
        #projects = Project.objects.filter(tasks__exact = completed)
    else:#public projects only
        projects = Project.objects.extra(where=['tasks = 0 or tasks <> completed  and type=%s'], params=[PROJECT_TYPE['public']])
    #completed projects
    if is_auth:
        com_proj = Project.objects.extra(where=['tasks > 0 and tasks = completed '])
    else:
        com_proj = Project.objects.extra(where=['tasks > 0 and tasks = completed  and type=%s'], params=[PROJECT_TYPE['public']])

    return render_to_response('todo/index.html',
                                  {'projects':projects,'completed_projects':com_proj,'is_authenticated':is_auth}
                                    ,context_instance=RequestContext(request))
    #return HttpResponse('this a test task page')

@login_required
def index(request):
    '''todo homepage'''
    user = request.user
    is_auth = request.user.is_authenticated()
    #not completed projects
    if is_auth:
        projects = Project.objects.filter(user__exact = user)
    else:#public projects only
        projects = Project.objects.extra(where=['tasks = 0 or tasks <> completed  and type=%s'], params=[PROJECT_TYPE['public']])
    #completed projects
    if is_auth:
        com_proj = Project.objects.extra(where=['tasks > 0 and tasks = completed '])
    else:
        com_proj = Project.objects.extra(where=['tasks > 0 and tasks = completed  and type=%s'], params=[PROJECT_TYPE['public']])

    return render_to_response('todo/index.html',
                                  {'projects':projects,'completed_projects':com_proj,'is_authenticated':is_auth}
                                    ,context_instance=RequestContext(request))
    #return HttpResponse('this a test task page')

@staff_member_required
def task_add(request):
    '''add task to project'''
    pid = int(request.POST.get('pid',0))
    task = Task()
    task.name = request.POST.get('task_name')
    task.project = get_object_or_404(Project,id__exact = pid)
    priority = request.POST.get('priority')
    if priority:
        task.priority = priority
    else:
        task.priority = TASK_PRIORITY['medium']
    task.completed = 0
    task.save()
    #add project task count
    task.project.tasks += 1
    task.project.save()
    #return HttpResponseRedirect('/todo/')
    return HttpResponse('success')

@staff_member_required
def project_add(request):
    '''add todo project'''
    project = Project()
    project.user = request.user
    project.name = request.POST.get('project_name')
    project.type = request.POST.get('project_type',0)
    project.desc = u''
    project.slug = u''
    project.tasks = 0
    project.completed = 0
    project.save()
    return HttpResponse('success')

@staff_member_required
def project_del(request):
    '''delete project'''
    project_id = int(request.POST.get('project_id',0))
    project = get_object_or_404(Project,id__exact=id)
    project.delete()
    return HttpResponse('success')

@staff_member_required
def project_chg_type(request):
    '''change project type'''
    project_id = int(request.POST.get('project_id',0))
    project = get_object_or_404(Project,id__exact=project_id)
    #if project.type == PROJECT_TYPE['public']:
    #    project.type = PROJECT_TYPE['private']
    #else:
    #    project.type = PROJECT_TYPE['public']  
    project.type = not project.type
    project.save()
    return HttpResponse('success')

@staff_member_required
def task_done(request):
    '''done a task'''
    task_id = int(request.POST.get('task_id',0))
    task = get_object_or_404(Task,id__exact=task_id)
    task.completed = 1
    task.save()
    #add project completed task count
    task.project.completed += 1
    task.project.save()
    return HttpResponse('success')

@staff_member_required
def task_undone(request):
    '''undone a task'''
    task_id = int(request.POST.get('task_id',0))
    task = get_object_or_404(Task,id__exact=task_id)
    task.completed = 0
    task.save()
    #reduce project completed task count
    task.project.completed -= 1
    task.project.save()
    return HttpResponse('success')

@staff_member_required
def task_del(request):
    '''delete a task'''
    task_id = int(request.POST.get('task_id',0))
    task = get_object_or_404(Task,id__exact=task_id)
    task.project.tasks -= 1
    #is a completed task
    if task.completed == 1:
        task.project.completed -= 1
    task.project.save()
    task.delete()
    return HttpResponse('success')
