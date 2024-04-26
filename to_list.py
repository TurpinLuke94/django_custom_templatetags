# Imports the 'template' class from the 'django' module
from django import template

"""
Custom template tags: https://docs.djangoproject.com/en/4.0/howto/custom-template-tags/#code-layout

"""

# Creates a valid tag library in which all the tags are registered
register = template.Library()

# Creates a 'to_list' template tag
@register.simple_tag
def to_list(*args):
    """
    Converts the tag's arguments into a list and returns it. The 'simple_tag' decorator is a helper function which wraps this function in a render function, performs other necessary bits, and registers it with the template system.

    https://docs.djangoproject.com/en/4.0/howto/custom-template-tags/#simple-tags

    """
    return list(args)
