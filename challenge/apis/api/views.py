from django.utils.functional import empty
import requests
import json

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import ApiModelSerializer

from apis.models import Apis


@api_view(['POST', 'GET'])
def populateApis(request):
    if request.method=='POST':
        data = get_data()
        serializer = ApiModelSerializer(data = data, many = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'funciono todo bien creo'}, status=status.HTTP_201_CREATED)
        return Response({'serializer.errors':serializer.errors,'message':'algo salio mal en el is valid'})
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

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


@api_view(['POST', 'GET'])
def findKeyword(request):
    if request.method=='POST':
        keyword = request.data['keyword']
        data = Apis.objects.filter(API__startswith=keyword)
        print(data)
        if data.exists():
            serializer = ApiModelSerializer(data, many = True)
            return Response({'message':serializer.data})
        else:
            return Response({'message':'Ninguna api coincide con el criterio seleccionado'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
