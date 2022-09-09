from django import template
from freddit.models import Thread, Comment

register = template.Library()

@register.inclusion_tag('freddit/thread_tags.html')
def get_thread_list():
	return {'threads': Thread.objects.all()}