from django.db import models
from django.db.models import Q

class ProjectManager(models.Manager):
    def for_user(self, user):
        user_projects = Q(user__exact=user)
        return self.filter(user_projects)