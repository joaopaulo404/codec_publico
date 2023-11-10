from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from rest_framework.decorators import api_view

from .models import Consolidados
from API_BOLETINS.models import Boletins
from .serializers import SerializarConsolidados
# Create your views here.
from django.contrib.auth.decorators import login_required
import datetime



consolidados = ['HOMICIDIO','LATROCINIO','LESAO CORPORAL SEGUIDA DE MORTE']

@api_view(['GET'])
def getConsolidados(request):
    if request.method == 'GET' or request.method == 'POST':
        consolidados = list(Consolidados.objects.all().values())
        consolidados_serializados = SerializarConsolidados(consolidados, many=True)
        return JsonResponse(consolidados_serializados.data, safe=False)


@api_view(['GET'])
def getCVLI(request, mes_fato):
    if request.method == 'GET' or request.method == 'POST':
        ano_atual = datetime.datetime.now().year 
        dia_atual = datetime.datetime.now().day
        intervalo_de_anos = [ano for ano in range(2010, ano_atual+1)]
        data = {'ano':[], 'quantidade':[]}
        for ano in intervalo_de_anos:
            data['ano'].append(ano)
            #dia_inicial = f'{ano}-{mes_fato}-01'
            #dia_final = f'{ano}-{mes_fato}-{dia_atual}'
            quantidade_cvli = Boletins.objects.filter(consolidado__in=consolidados).filter(ano_fato=ano).filter(data_fato__month=mes_fato).count()
            data['quantidade'].append(quantidade_cvli)
        return JsonResponse(data, safe=True)

