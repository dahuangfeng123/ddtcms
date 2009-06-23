# -*- coding: utf-8 -*-
"""
>>> from djangotdd.categories.models import Category
>>> a = Category.objects.create(name='PHP')
>>> b = Category.objects.create(name='Python')
>>> c = Category.objects.create(name='PHP6', parent=a)
>>> d = Category.objects.create(name='PHP5', parent=a)
>>> e = Category.objects.create(name='Zend Framework', parent=d)

>>> a.is_root()
True

>>> c.is_root()
False

>>> a.get_children()
[<Category: PHP6>, <Category: PHP5>]

>>> Category.objects.get_children_for_pk(a.pk)
[<Category: PHP6>, <Category: PHP5>, <Category: Zend Framework>]
"""
