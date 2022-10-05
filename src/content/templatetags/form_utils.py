from django import template
from django.forms import CheckboxInput, FileInput

register = template.Library()


@register.filter
def is_checkbox(field):
    return isinstance(field.field.widget, CheckboxInput)


@register.filter
def is_file_input(field):
    return isinstance(field.field.widget, FileInput)
