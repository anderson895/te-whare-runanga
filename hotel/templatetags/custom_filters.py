from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Allow dictionary lookups in Django templates"""
    return dictionary.get(key)
