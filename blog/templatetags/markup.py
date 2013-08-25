from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

from markdown import markdown
from typogrify.filters import typogrify


register = template.Library()


@register.filter
@stringfilter
def markup(value):
    result = typogrify(markdown(text,
                                lazy_ol=False,
                                output_format='html5',
                                extensions=['abbr',
                                            'codehilite',
                                            'fenced_code',
                                            'sane_lists',
                                            'smart_strong']))
    return mark_safe(result)
