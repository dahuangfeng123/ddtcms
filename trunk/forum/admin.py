from django.contrib import admin
from forum.models import Forum, Thread, Post, Subscription

class ForumAdmin(admin.ModelAdmin):
    list_display = ('title', '_parents_repr','slug','order')
    list_filter = ('groups',)
    ordering = ['parent', 'title']
    prepopulated_fields = {"slug": ("title",)}

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['author','thread']

class ThreadAdmin(admin.ModelAdmin):
    list_display = ('title', 'forum', 'posts','latest_post_time')
    list_filter = ('forum',)
    
class PostAdmin(admin.ModelAdmin):
    list_display = ('thread', 'floor','time')
    list_filter = ('thread',)

admin.site.register(Forum, ForumAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
