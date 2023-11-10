import pandas as pd
from .forms import Boletins


def buscar_boletins_pelo_form(form):
    # print(form['lista_bairros'])
    consolidados = form['lista_consolidados']
    municipios = form['lista_municipios']
    bairros = form['lista_bairros']
    data_inicio = form['data_inicio']
    data_fim = form['data_fim']
    boletins = Boletins.objects.filter(
        data_fato__range=[data_inicio, data_fim]).filter(
        bairros__in=bairros).filter(
        municipios__in=municipios).filter(
        consolidado__in=consolidados).values('consolidado', 'especificacao_crime', 
                'meio_emp_deac', 'municipios', 'bairros', 'ano_fato', 'mes_fato', 'risp', 'aisp',
                'data_fato', 'dia_semana', 'hora_fato', 'fx_4_hor', 'fx_12_hr',
                'latitude', 'longitude', 'distrito', 'reg_integracao', 'local_ocorrencia',
                'vit_sexo', 'vit_idade', 'vit_fx_etaria', 'vit_tipo', 'vit_cor_pele', 'vit_grau_inst',
                'vit_estado_civil', 'aut_sexo', 'aut_idade', 'aut_cor_pele', 'grau_de_relacionamento', )

    dataframe = pd.DataFrame(boletins)
    dataframe.columns = ['CONSOLIDADO(S)', 'ESPECIFICAÇÃO CRIME', 'MEIO EMPREGADO DEAC', 'MUNICÍPIO(S)', 'BAIRRO(S)', 'ANO DO FATO', 'MÊS DO FATO',
                         'RISP', 'AISP', 'DATA DO FATO', 'DIA DA SEMANA', 'HORA DO FATO', 'FAIXA 4 HORAS', 'FAIXA 12 HORAS', 'LATITUDE',
                         'LONGITUDE', 'DISTRITO', 'REGIÃO DE INTEGRAÇÃO', 'LOCAL DA OCORRÊNCIA', 'SEXO VÍTIMA', 'IDADE VÍTIMA',
                         'FAIXA ETÁRIA VÍTIMA', 'TIPO DE VÍTIMA', 'COR VÍTIMA', 'GRAU DE INSTRUÇÃO VÍTIMA', 'ESTADO CIVÍL VÍTIMA', 'SEXO AUTOR', 'IDADE AUTOR',
                         'COR AUTOR', 'GRAU DE RELACIONAMENTO', ]
    return dataframe


def dataframe_pagina(form):
    consolidados = form['lista_consolidados'].value()
    municipios = form['lista_municipios'].value()
    bairros = form['lista_bairros'].value()
    data_inicio = form['data_inicio'].value()
    data_fim = form['data_fim'].value()
    boletins = Boletins.objects.filter(
        data_fato__range=[data_inicio, data_fim]).filter(municipios__in=municipios).filter(consolidado__in=consolidados).filter(bairros__in=bairros).values('consolidado', 'municipios', 'bairros', 'risp','data_fato')

    dataframe = pd.DataFrame(boletins)
    dataframe.columns = ['CONSOLIDADO(S)', 'MUNICÍPIO(S)', 'BAIRRO(S)',
                         'RISP', 'DATA DO FATO']

    return dataframe
