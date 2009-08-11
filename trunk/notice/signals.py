from django.db.models import signals
from ddtcms.notice.models import Notice
from ddtcms.news.models import News

def my_handler(sender, **kwargs):
    new_notice=Notice()
    new_notice.title="A new News Posted"
    new_notice.content='content'
    new_notice.slug='news%s' % datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    new_notice.save()
signals.post_save.connect(my_handler, sender=News)
