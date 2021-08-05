from django import template
from rango.models import City, UserLikedCity

register = template.Library()


@register.inclusion_tag('rango/cities.html')
def get_category_list(current_category=None):
    return {'categories': City.objects.all(),
            'current_category': current_category}


@register.inclusion_tag('rango/mycities.html')
def get_mycity_list(current_city=None, user=None):
    return {'mycities': UserLikedCity.objects.all(),
            'user': user,
            'current_city': current_city}
