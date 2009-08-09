from django import template

register = template.Library()

def attachments(context, obj):
    return {
        'object': obj, 
        #'request': context['request'],
        'user': context['user'],
    }

register.inclusion_tag('attachments/attachments.html', takes_context=True)(attachments)

def forum_post_attachments(context, obj):
    return {
        'object': obj, 
        #'request': context['request'],
        'user': context['user'],
    }

register.inclusion_tag('attachments/forum_post_attachments.html', takes_context=True)(forum_post_attachments)

def news_attachments(context, obj):
    return {
        'object': obj, 
        #'request': context['request'],
        'user': context['user'],
    }

register.inclusion_tag('attachments/news_attachments.html', takes_context=True)(news_attachments)