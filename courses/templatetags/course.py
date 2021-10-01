from django import template
from ..models import Course

register = template.Library()


@register.filter
def model_name(obj):
    try:
        return obj._meta.model_name
    except AttributeError:
        return None


@register.filter
def enrolled(obj, course):
    try:
        obj.courses_joined.get(id=course.id)
    except Course.DoesNotExist:
        return False
    except:
        return False
    return True
