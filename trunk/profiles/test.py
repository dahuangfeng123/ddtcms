F:\Python\mysite>manage.py shell
Python 2.5.2 (r252:60911, Feb 21 2008, 13:11:45) [MSC v.1310 32 bit (Intel)] on
win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> import django
>>> import mysite
>>> dir(mysite)
['__builtins__', '__doc__', '__file__', '__name__', '__path__', 'article', 'blog
', 'captcha', 'faq', 'forum', 'home', 'member', 'news', 'notice', 'photo', 'poll
s', 'settings', 'todo', 'wiki']
>>> import ddtcms.member
>>> import ddtcms.profiles
>>> dir(profiles)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'profiles' is not defined
>>> import ddtcms.profiles as profiles
>>> profiles
<module 'ddtcms.profiles' from 'F:\Python\mysite\..\mysite\profiles\__init__.pyc
'>
>>> dir(profiles)
['__builtins__', '__doc__', '__file__', '__name__', '__path__']
>>> profiles.views
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'module' object has no attribute 'views'
>>> import profiles.views as pw
>>> pw
<module 'profiles.views' from 'F:\Python\mysite\profiles\views.pyc'>
>>> dir(pw)
['Http404', 'HttpResponseRedirect', 'ObjectDoesNotExist', 'RequestContext', 'Use
r', '__builtins__', '__doc__', '__file__', '__name__', 'create_profile', 'edit_p
rofile', 'get_object_or_404', 'login_required', 'object_list', 'profile_detail',
 'profile_list', 'render_to_response', 'reverse', 'utils']
>>> pm=profiles.utils.get_profile_model()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'module' object has no attribute 'utils'
>>> import profiles.utils as utils
>>> pm=utils.get_profile_model()
>>> pm
<class 'ddtcms.member.models.Profile'>
>>> dir(pm)
['DoesNotExist', 'MultipleObjectsReturned', '__class__', '__delattr__', '__dict_
_', '__doc__', '__eq__', '__getattribute__', '__hash__', '__init__', '__metaclas
s__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr_
_', '__setattr__', '__str__', '__unicode__', '__weakref__', '_collect_sub_object
s', '_default_manager', '_get_FIELD_display', '_get_next_or_previous_by_FIELD',
'_get_next_or_previous_in_order', '_get_pk_val', '_meta', '_set_pk_val', 'delete
', 'get_absolute_url', 'get_next_by_birthday', 'get_previous_by_birthday', 'obje
cts', 'pk', 'save', 'save_base', 'user']
>>> qs=pm._default.manager.all()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: type object 'Profile' has no attribute '_default'
>>> qs=pm._default_manager.all()
>>> qs
[]
>>> qs=pm._default_manager.all()
>>> qs
[<Profile: admin>]
>>>