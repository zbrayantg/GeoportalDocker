from django import template

register = template.Library()


@register.filter(name='split')
def split(value):
    """
        Returns the number of register
    """
    return value.split("-")[0]
