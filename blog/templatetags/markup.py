from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

from blog.models import markup as markup_func

from markdown import markdown
from typogrify.filters import typogrify


register = template.Library()


@register.filter
@stringfilter
def markup(value):
    return mark_safe(markup_func(value))
