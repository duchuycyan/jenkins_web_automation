import re

from django import template

register = template.Library()


def currency(value):
    new_value = str(value)
    if len(new_value) > 3 and len(new_value) <= 6:
        result = new_value[:-3] + '.' + new_value[-3:]
    elif len(new_value) > 6 and len(new_value) <= 9:
        result = new_value[:-6] + '.' + new_value[-6:-3] + '.' + new_value[-3:]
    else:
        pass
    return result

def ram(value):
    value = float(value)
    if value < 1:
        value = str(round(1024 * value)) + ' MB'
    value = str(value).replace('.0', '')
    return value

register.filter('currency', currency)
register.filter('ram', ram)
