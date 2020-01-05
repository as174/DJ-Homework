from django import template

register = template.Library()

@register.filter
def bgcolor(value):
    if value == '-':
        color = '#FFFFFF'
    else:
        if float(value) < 0:
            color = '#34D800'
        elif 1 <= float(value) <= 2:
            color = '#FD7279'
        elif 2 < float(value) <= 5:
            color = '#FD3F49'
        elif float(value) > 5:
            color = '#A30008'
        else:
            color = '#FFFFFF'
    return color