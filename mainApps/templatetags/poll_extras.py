from django import template
import datetime

register = template.Library()

@register.filter(name='Cutthecrap')
def Cutthecrap(value, value2):
    return value.split('@')[value2]