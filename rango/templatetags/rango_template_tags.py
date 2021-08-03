from django import template
from rango.models import City

register = template.Library()

@register.inclusion_tag('rango/cities.html')
def get_category_list(current_category=None):
    return {'categories': City.objects.all(),
            'current_category': current_category}