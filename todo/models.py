#coding=utf-8
from django.utils.translation import ugettext as _
from django.db import models
import fpformat
from django.contrib.auth.models import User
from todo.managers import ProjectManager

# Create your models here.
#Project types
PROJECT_TYPE = (
(0,_('public')),
(1,_('private')),
)
TASK_PRIORITY = (
(0,_('low')),
(1,_('medium')),
(2,_('high')),
)

class Project(models.Model):
    '''todo project entity'''
    user        = models.ForeignKey(User, related_name='user_todos',blank=True)
    name        = models.CharField(_('Project Name'),max_length=255)
    pub_date    = models.DateTimeField(_('Created Date'),auto_now_add=True)
    update_date = models.DateTimeField(_('LastUpdated Date'),auto_now=True)
    type        = models.IntegerField(_('Project type'),choices=PROJECT_TYPE,default=0)
    desc        = models.CharField(_('Project Description'),max_length=1024,null=True,blank=True)
    tasks       = models.IntegerField(_('Project task count'),blank=True,default=0)
    completed   = models.IntegerField(_('Completed task count'),blank=True,default=0)
    slug        = models.CharField(_('Project slug'),max_length=255,null=True,blank=True)
    
    def __unicode__(self):
        return self.name    
        
    def get_absolute_url(self):
        if self.slug:
            return "/todo/%s/" % (self.slug)
        else:
            return "/todo/%s/" % (self.id)
            
                 
    class Meta:
        ordering        = ('-update_date','-pub_date',)
        verbose_name = _('Todo Project')
        verbose_name_plural = _('Todo Projects')
        
    def rop(self):
        '''rate of progress use percent'''
        r=0.00
        if(self.tasks!=0):
            r=fpformat.fix(float(self.completed)/self.tasks*100, 2)
        return "%s" % fpformat.fix(r, 2) +"%"
    
    def save(self,*args,**kwargs):
        if not self.desc:
            self.desc = self.name
        super(Project,self).save(*args,**kwargs)




class Task(models.Model):
    '''todo task'''
    name        = models.CharField(_('Task Name'),max_length=255)
    project     = models.ForeignKey(Project, related_name='task_set',verbose_name=_('Task Project'))
    created     = models.DateTimeField(_('Created Date'),auto_now_add=True)
    lastupdated = models.DateTimeField(_('LastUpdated Date'),auto_now=True)
    priority    = models.IntegerField(_('Task Priority'),choices=TASK_PRIORITY,default=0)
    completed   = models.BooleanField(_('Is task completed'),default=False)
    # SAVE|TODO save function override
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ['completed','-priority']
        verbose_name = _('Todo Task')
        verbose_name_plural = _('Todo Tasks')
        
