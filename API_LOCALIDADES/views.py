from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from rest_framework.decorators import api_view

from .models import Localidades
from .serializers import SerializarLocalidades
# Views para escrever na API


    # GET = retorna a lista de boletins de ocorrencia
@api_view(['GET'])
def getCidades(request):
    if request.method == 'GET':
        localidades = list(Localidades.objects.distinct('municipios').values())
        localidades_serializadas = SerializarLocalidades(localidades, many=True)
        return JsonResponse(localidades_serializadas.data, safe=False)
    
@api_view(['GET'])
def getBairros(request):
    if request.method == 'GET':
        bairros = list(Localidades.objects.all().values())
        bairros_serializadas = SerializarLocalidades(bairros, many=True)
        return JsonResponse(bairros_serializadas.data, safe=False)

