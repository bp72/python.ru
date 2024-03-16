from django import template
from django.conf import settings
from django.db.models.fields.files import FieldFile

register = template.Library()

@register.simple_tag
def get_host_from_url(url):
    try:
        response = url.split("/")
        return response[2]
    except IndexError:
        return response[0]
