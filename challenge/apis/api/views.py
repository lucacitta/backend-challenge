from django.http.response import Http404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import ApiModelSerializer
from apis.models import Apis
from apis.tasks import populate

@api_view(['POST', 'GET'])
def populateApis(request):
    if request.method=='POST':
        populate.delay()
        return Response({'message':'Task llamada correctamente'}, status=status.HTTP_201_CREATED)
    raise Http404




@api_view(['POST', 'GET'])
def findKeyword(request):
    if 'keyword' in request.data:
        if request.method=='POST':
            data = Apis.objects.filter(API__startswith=request.data['keyword'])
            if data.exists():
                serializer = ApiModelSerializer(data, many = True)
                return Response({'message':serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({'message':'Ninguna api coincide con el criterio seleccionado'},
                                status=status.HTTP_404_NOT_FOUND)
    raise Http404




class CategoryApiView(APIView):

    def get(self, request):
        raise Http404

    def post(self, request):
        if 'category' in request.data:
            category = Apis.objects.filter(Category = request.data['category'])
            if category.exists():
                serializer = ApiModelSerializer(category, many = True)
            else:
                return Response({'message':'Ninguna categoria coincide con el criterio seleccionado'},
                                status=status.HTTP_404_NOT_FOUND)
            return Response(serializer.data)
        raise Http404




@api_view(['POST','GET'])
def orderedList(request):
    if request.method=='POST':
        apis = Apis.objects.order_by('id')
        serializer = ApiModelSerializer(apis, many=True)
        return Response(serializer.data)
    else:
        raise Http404




@api_view(['POST','GET'])
def itemDetail(request):
    if 'pk' in request.data:    #Nos aseguramos de que haya algun pk
        if request.method=='POST':
            item = Apis.objects.filter(id = request.data['pk'])
            if item.exists():
                serializer = ApiModelSerializer(item, many = True)
            else:
                return Response({'message':'Ningun item coincide con el criterio seleccionado'},
                                status=status.HTTP_404_NOT_FOUND)
            return Response(serializer.data)
    raise Http404
