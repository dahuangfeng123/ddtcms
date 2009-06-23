"""
>>> from categories.models import Category
>>> from categories.utils import display_tree

>>> root = Category.objects.root()

>>> display_tree()

>>> news = Category(name='News', slug='news')
>>> news.save()
>>> display_tree()
News
>>> news.breadcrumbs()
u'News'
>>> news.get_absolute_url()
u'news/'

>>> technology = Category(name='Technology', slug='technology')
>>> news.children.add(technology)
>>> display_tree()
News
  Technology
>>> technology.breadcrumbs()
u'News :: Technology'
>>> technology.get_absolute_url()
u'news/technology/'

Add two leaf nodes with default ordering.

>>> apple = Category(name='Apple', slug='apple')
>>> technology.children.add(apple)
>>> microsoft = Category(name='Microsoft', slug='microsoft')
>>> technology.children.add(microsoft)
>>> display_tree()
News
  Technology
    Apple
    Microsoft

Change the ordering.

>>> apple.sort_order = 2
>>> apple.save()
>>> microsoft.sort_order = 1
>>> microsoft.save()
>>> display_tree()
News
  Technology
    Microsoft
    Apple

>>> sports = Category(name='Sports', slug='sports')
>>> news.children.add(sports)
>>> display_tree()
News
  Technology
    Microsoft
    Apple
  Sports

"""