from django import template

register = template.Library()

WEEKDAYS = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday',
}

@register.filter
def weekday_name(value):
    return WEEKDAYS[value]
