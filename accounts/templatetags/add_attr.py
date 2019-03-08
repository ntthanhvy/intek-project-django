from django.template import Library

register = Library()


@register.filter(name='add_attr')
def add_attr(field, css):
    atts = {}
    definision = css.split(',')

    for d in definision:
        if ':' not in d:
            atts['class'] = d
        else:
            key, val = d.split(':')
            atts[key] = val

    return field.as_widget(attrs=atts)