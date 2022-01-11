from __future__ import absolute_import, unicode_literals

import requests
import json

from celery import shared_task

from .api.serializers import ApiModelSerializer

@shared_task
def populate():
    data = get_data()
    serializer = ApiModelSerializer(data = data, many = True)
    if serializer.is_valid():
        serializer.save()

def get_data():
    url = 'https://api.publicapis.org/entries'
    response = requests.get(url)    #El requerimiento decia utilizar post, pero no es metodo permitido por la api
    data = json.loads(response.content)
    data = boolean_fix(data['entries'])
    return data

def boolean_fix(data):
    for datos in data:
        if datos['Cors'] == 'yes':
            datos['Cors'] = True
        elif datos['Cors'] == 'no':
            datos['Cors'] = False
        else:
            datos['Cors'] = None
    return data
