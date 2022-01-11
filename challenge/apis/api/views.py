import requests
import json

from django.http.response import Http404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
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
        raise Http404

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
        data = Apis.objects.filter(API__startswith=request.data['keyword'])
        if data.exists():
            serializer = ApiModelSerializer(data, many = True)
            return Response({'message':serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message':'Ninguna api coincide con el criterio seleccionado'},
                            status=status.HTTP_404_NOT_FOUND)
    else:
        raise Http404




class CategoryApiView(APIView):

    def get(self, request):
        raise Http404

    def post(self, request):
        category = Apis.objects.filter(Category = request.data['category'])
        if category.exists():
            serializer = ApiModelSerializer(category, many = True)
        else:
            return Response({'message':'Ninguna categoria coincide con el criterio seleccionado'},
                            status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)




@api_view(['POST','GET'])
def orderedList(request):
    if request.method=='POST':
        apis = Apis.objects.order_by('id')
        serializer = ApiModelSerializer(apis, many=True)
        return Response(serializer.data)
    else:
        raise Http404