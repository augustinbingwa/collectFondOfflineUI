from django import template
register = template.Library()
from apps.home.models import *
from django.utils import timezone
from apps.home.enums import *

@register.filter()
def get_client_by_code(code):
    client_value = ''
    if code:
        client = Client.objects.filter(code_client=code).first()
        client_value = f'{client.nom} {client.prenom} {client.code_client}'
    return client_value

@register.filter()
def get_id_client_by_code(code):
    client_value = ''
    if code:
        client = Client.objects.filter(code_client=code).first()
        client_value = client.id
    return client_value

@register.filter()
def get_client_by_code_date_cr(code):
    client_value = ''
    status = 'Nouveau'
    time = timezone.now()
    if code:
        client = Client.objects.filter(code_client=code).first()
        if client:
            if client.date_creation.year == time.year - 1:
                status = 'Ancien'
            elif client.date_creation.year <= time.year - 2:
                status = 'Très ancien'
        client_value = f'{status} | Creation: {client.date_creation}'
    return client_value


@register.filter()
def get_type_cotisation(value):
    return choix_type_cotisation[value] or ''

@register.filter()
def get_periode_cotisation(value):
    return choix_periode_cotisation[value] or ''

# function to return value if value not none
@register.filter()
def get_value(value):
    return value or ''