from django import template

register = template.Library()

@register.simple_tag
def dictKeyLookup(the_dict, key):
    # Try to fetch from the dict, and if it's not found return an empty string.
   return the_dict.get(key, '')

@register.filter
def get_key(some_dict, key):
   return some_dict.get(key, '')