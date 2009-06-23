from ddtcms import settings
from ddtcms.blog.models import Entry
from ddtcms.category.models import Category
from django.contrib.contenttypes.models import ContentType
e1=ContentType.objects.get(app_label='blog', model='entry')
c1=Category.objects.get_content_type(e1)
print c1
