from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

from blog.models import markup


register = template.Library()


@register.filter
@stringfilter
def markup(value):
    result = markup(value)
    return mark_safe(result)
