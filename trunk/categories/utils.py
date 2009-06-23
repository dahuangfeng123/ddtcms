
from categories.models import Category

def rebuild_tree(node, lft):
    rgt = lft + 1
    for child in node.children.all():
        right = rebuild_tree(child, rgt)
    node.lft, node.rgt = lft, rgt
    node.save()
    return rgt + 1

def display_tree(node=None, **kwargs):
    right = []
    node = node or Category.objects.root()
    for node in node.get_tree(**kwargs):
        if right:
            while right[len(right) - 1].rgt < node.rgt:
                right.pop()
        print u'%s%s' % ('  ' * len(right), node)
        right.append(node)

# for debugging
def display_flat_tree(node=None, **kwargs):
    node = node or Category.objects.root()
    for node in node.get_tree(**kwargs):
        print node.name, node.lft, node.rgt
