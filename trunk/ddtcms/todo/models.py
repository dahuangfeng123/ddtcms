#coding=utf-8
from django.utils.translation import ugettext as _
from django.db import models

# Create your models here.
#Project types
PROJECT_TYPE = {
'public':0,
'private':1
}
TASK_PRIORITY = {
'low':0,
'medium':1,
'high':2
}

class Project(models.Model):
    '''todo project entity'''
    name        = models.CharField(_('Project Name'),max_length=255)
    pub_date    = models.DateTimeField(_('Created Date'),auto_now_add=True)
    update_date = models.DateTimeField(_('LastUpdated Date'),auto_now=True)
    type        = models.IntegerField(_('Project type'),default=0)
    desc        = models.CharField(_('Project Description'),max_length=1024)
    tasks       = models.IntegerField(_('Project task count'),default=0)
    completed   = models.IntegerField(_('Completed task count'),default=0)
    slug        = models.CharField(_('Project slug'),max_length=255)
    
    def __unicode__(self):
        return self.name    
        
    def get_absolute_url(self):
        if self.slug:
            return "/todo/%s/" % (self.slug)
        else:
            return "/todo/%s/" % (self.id)
            
                 
    class Meta:        
        verbose_name=_('Todo Project')
        verbose_name_plural = _('Todo Projects')
    

         
    
class Task(models.Model):
    '''todo task'''
    name        = models.CharField(_('Task Name'),max_length=255)
    project     = models.ForeignKey(Project, related_name='task_set',verbose_name=_('Task Project'))
    created     = models.DateTimeField(_('Created Date'),auto_now_add=True)
    lastupdated = models.DateTimeField(_('LastUpdated Date'),auto_now=True)
    priority    = models.IntegerField(_('Task Priority'),default=0)
    completed   = models.BooleanField(_('Is task completed'),default=False)
    # SAVE|TODO save function override
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ['completed','-priority']
        verbose_name = _('Todo Task')
        verbose_name_plural = _('Todo Tasks')
        
