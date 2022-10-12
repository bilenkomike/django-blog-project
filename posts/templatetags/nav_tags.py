
from django import template

register = template.Library()




from posts.models import Post


@register.inclusion_tag('tags/list.html')
def posts_list():
    return {'posts': Post.objects.order_by('-id')[:10]}
