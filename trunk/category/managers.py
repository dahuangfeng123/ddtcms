from django.db import models
from django.dispatch import dispatcher
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import force_unicode

class CategoryManager(models.Manager):
    def get_children_for_pk(self, pk):
        return self.filter(root_pk=pk)
    
    #def get_content_type_set(self,app,model):
    #    ctype=ContentType.objects.get(app_label=app, model=model)        
    #    return self.filter('outline__content_type'=ctype)



    def for_model(self, model):
        """
        QuerySet for all Categorys for a particular model (either an instance or
        a class).
        """
        ct = ContentType.objects.get_for_model(model) 
        queries={'outline__content_type':ct}
        qs = self.get_query_set().filter(**queries)
        
        if isinstance(model, models.Model):
            qs = qs.filter(object_pk=force_unicode(model._get_pk_val()))
        return qs
