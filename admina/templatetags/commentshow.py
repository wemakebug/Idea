from django import template

register = template.Library()


@register.filter(name='firstcomment')
def firstcomment(value):
    return value[0]

@register.filter(name='firstcommenttime')
def firstcommenttime(value):
    return value[0].Date

@register.filter(name='firstcommentcontent')
def firstcommentcontent(value):
    return value[0].Content

@register.filter(name='leftcomment')
def leftcomment(value):
    return value[1:]

@register.filter(name='firstcommentId')
def firstcommentId(value):
    return value.Id
