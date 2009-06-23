
from django.db import models

class CategoryManager(models.Manager):
    """
    A collection of methods that make accessing the category tree easier.
    """
    
    def get_root(self):
        """
        Returns the root node of the tree.
        """
        return self.get(parent__isnull=True)
    
    def get_path(self, node, include_root=False):
        """
        Returns a list of internal nodes from the root node to the given node.
        """
        if not include_root:
            qs = self.exclude(parent__isnull=True)
        qs = qs.filter(lft__lt=node.lft, rgt__gt=node.rgt)
        return list(qs.order_by('lft')) + [node]
    
    def get_tree(self, node, include_root=False):
        """
        Returns a list of nodes that are descendants of the given node.
        """
        # TODO: make this a nested list and not a flat list
        if not include_root:
            qs = self.exclude(parent__isnull=True)
        qs = qs.filter(lft__range=(node.lft, node.rgt))
        return qs.order_by('lft')
    
    def num_descendants(self, node):
        """
        Returns a count of all descendants of the given node.
        """
        return (node.rgt - node.lft - 1) / 2