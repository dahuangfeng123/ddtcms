from django.contrib import admin
from ddtcms.book.models import Book,Author,Publisher
from ddtcms.book.models import Chapter

admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Chapter)



