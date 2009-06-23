from django.contrib.sitemaps import Sitemap
from ddtcms.blog.models import Entry

class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Entry.objects.all()

    def lastmod(self, obj):
        return obj.pub_date
