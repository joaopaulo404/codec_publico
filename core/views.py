from bs4 import BeautifulSoup
from django.shortcuts import render, redirect
from API_LOCALIDADES.models import Localidades
from API_BOLETINS.models import Boletins
import pandas as pd
import numpy as np
import datetime
from django.http import HttpResponse, HttpResponseRedirect
from io import BytesIO
from django.contrib import messages
from core.listas import CONSOLIDADOS_PUBLICOS, LISTA_MUNICIPIOS
from .forms import BoletinsForm
from .filtros import dataframe_pagina, buscar_boletins_pelo_form
from datetime import datetime
# Create your views here.

dataframe = pd.DataFrame()

# form_recorte_global = BoletinsForm()

def home(request):
    # if request.user.is_authenticated:
    #     return redirect('/usuarios')
    if request.method == 'GET':
        form = BoletinsForm()
        context = {
            'form': form,
            'data': Boletins.objects.filter(ano_fato=datetime.now().strftime("%Y")).order_by('data_fato').last().data_fato,
            'consolidados_disponiveis':CONSOLIDADOS_PUBLICOS,
            'lista_municipios': LISTA_MUNICIPIOS
        }
        return render(request, 'core/home.html', context)
    if request.method == 'POST':
        form = BoletinsForm(request.POST)
        if form.is_valid():
            try:
                # global form_recorte_global 
                form_recorte_global = form
                print(form_recorte_global['data_inicio'])
                request.session['form_recorte_global'] = str(form)
                dataframe = dataframe_pagina(form)
                df = dataframe[['CONSOLIDADO(S)', 'MUNICÍPIO(S)', 'BAIRRO(S)',
                                'RISP', 'DATA DO FATO']].head(13)
                context = {
                    'form': form,
                    'df': df,
                    'data': Boletins.objects.filter(ano_fato=datetime.now().strftime("%Y")).order_by('data_fato').last().data_fato,
                    'consolidados_disponiveis':CONSOLIDADOS_PUBLICOS,
                    'lista_municipios': LISTA_MUNICIPIOS
                }
            except ValueError:
                form = BoletinsForm(request.POST)
                context = {
                    'erro': "Não encontramos nenhum dado referente aos filtros selecionados nesse período de tempo. Por favor, busque novamente.",
                    'data': Boletins.objects.filter(ano_fato=datetime.now().strftime("%Y")).order_by('data_fato').last().data_fato,
                    'form': form,
                    'consolidados_disponiveis':CONSOLIDADOS_PUBLICOS,
                    'lista_municipios': LISTA_MUNICIPIOS
                }

        else:
            form = BoletinsForm(request.POST)
            context = {
                'form': form,
                'erro': 'Certifique-se que todas as caixas foram selecionadas corretamente',
                'data': Boletins.objects.filter(ano_fato=datetime.now().strftime("%Y")).order_by('data_fato').last().data_fato,
                'consolidados_disponiveis':CONSOLIDADOS_PUBLICOS,
                'lista_municipios': LISTA_MUNICIPIOS
            }
        return render(request, 'core/home.html', context=context)

def download_recorte(request):
    form_recorte_global = request.session.get('form_recorte_global', None)
    soup = BeautifulSoup(form_recorte_global, 'html.parser')

    # Criar um dicionário para armazenar os campos do formulário
    formulario_dict = {}

    # Extrair os campos de checkbox do formulário e atualizar o dicionário
    campos_checkbox = soup.find_all('input', {'type': 'checkbox'})
    for campo in campos_checkbox:
        if campo.has_attr('checked'):
            nome_campo = campo.get('name')
            valor_campo = campo.get('value')
            if nome_campo not in formulario_dict:
                formulario_dict[nome_campo] = []
            formulario_dict[nome_campo].append(valor_campo)

    # Extrair os campos de seleção do formulário e atualizar o dicionário
    campos_selecao = soup.find_all('select')
    for campo in campos_selecao:
        nome_campo = campo.get('name')
        valores_selecionados = [option.get('value') for option in campo.find_all('option', selected=True)]
        formulario_dict[nome_campo] = valores_selecionados

    # Extrair os campos de data do formulário e atualizar o dicionário
    campos_data = soup.find_all('input', {'type': 'date'})
    for campo in campos_data:
        nome_campo = campo.get('name')
        valor_campo = campo.get('value')
        formulario_dict[nome_campo] = valor_campo
    dataframe = buscar_boletins_pelo_form(formulario_dict)
    if dataframe is not None:
        try:
            with BytesIO() as b:
                writer = pd.ExcelWriter(b, engine='xlsxwriter')
                tamanho_maximo_de_linhas = 500000
                lista_de_dataframes = [dataframe.loc[i:i+tamanho_maximo_de_linhas-1,:] for i in range(0, len(dataframe),tamanho_maximo_de_linhas)]
                numero_folha = 1
                for df in lista_de_dataframes:
                    print('Número da folha ', numero_folha)
                    df.to_excel(
                        writer, sheet_name=f'Sheet{numero_folha}', index=False
                    )     
                    numero_folha += 1
                writer.close()
                hoje = datetime.now().strftime("%d/%m/%y")
                filename = f'{hoje}.xlsx'
                response = HttpResponse(
                    b.getvalue(),
                    content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                )
                response['Content-Disposition'] = 'attachment; filename=%s' % filename
                return response
        except ValueError:
            context = {
                'erro': "A tabela gerada possui um tamanho não suportado pelo Excel. Portanto, solicitamos que divida o intervalo de tempo da consulta em duas partes",
                'form': form_recorte_global,
                'consolidados_disponiveis':CONSOLIDADOS_PUBLICOS,
                'lista_municipios': LISTA_MUNICIPIOS
            }
            return render(request, 'core/home.html', context=context)
    else:
        context = {
            'form': form_recorte_global,
            'consolidados_disponiveis':CONSOLIDADOS_PUBLICOS,
            'lista_municipios': LISTA_MUNICIPIOS,
            'erro': 'Nenhum dataframe foi reconhecido'
        }
    return render(request, 'core/home.html', context=context)

def analise(request):
    global dataframe
    dataframe_analise = dataframe.groupby(
        ["ANO DO FATO", "CONSOLIDADO(S)", "RISP", "MUNICÍPIO(S)", "MÊS DO FATO"]).agg({"CONSOLIDADO(S)": np.size})
    if dataframe is not None:

        with BytesIO() as b:
            writer = pd.ExcelWriter(b, engine='xlsxwriter')
            dataframe_analise.to_excel(
                writer, sheet_name='Sheet1', index=False)
            writer.close()
            hoje = datetime.now().strftime("%d/%m/%y")
            filename = f'Analise {hoje}.xlsx'
            response = HttpResponse(
                b.getvalue(),
                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )
            response['Content-Disposition'] = 'attachment; filename=%s' % filename
            return response
    else:
        return render(request, 'core/home.html')