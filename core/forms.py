from django import forms
from API_BOLETINS.models import Boletins

from API_LOCALIDADES.models import Localidades
from django_select2.forms import Select2MultipleWidget

class BoletinsForm(forms.ModelForm):

    CONSOLIDADOS_PUBLICOS = (
        ('HOMICIDIO','HOMICIDIO'),
        ('LATROCINIO','LATROCINIO'),
        ('LESAO CORPORAL','LESAO CORPORAL'),
        ('LESAO CORPORAL SEGUIDA DE MORTE','LESAO CORPORAL SEGUIDA DE MORTE'),
        ('FURTO','FURTO'),
        ('ROUBO','ROUBO'),
        ('ESTUPRO','ESTUPRO'),
        ('ESTUPRO DE VULNERAVEL','ESTUPRO DE VULNERAVEL'),
        ('TRAFICO DE DROGAS','TRAFICO DE DROGAS'),
    )
    data_inicio = forms.DateField(required=True,
        label='Data início',
        widget=forms.DateInput(
            format='%d-%m-%Y',
            attrs={
                'type': 'date',
            }),
        input_formats=('%Y-%m-%d',),
    )
    data_fim = forms.DateField(required=True,
        label='Data fim',
        widget=forms.DateInput(
            format='%d-%m-%Y',
            attrs={
                'type': 'date',
            }),
        input_formats=('%Y-%m-%d',),
    )
    
    # Analisar a possiblidade de executar somente uma consulta no Localidades e aproveitar todos os valores
    lista_municipios = forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple, 
                                                choices=[(municipio['municipios'], municipio['municipios']) for municipio in Localidades.objects.distinct('municipios').values()])
    lista_consolidados = forms.MultipleChoiceField(required=True, 
                                                choices=CONSOLIDADOS_PUBLICOS, widget=Select2MultipleWidget)
    lista_bairros = forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple, 
                                            choices=[(bairro['bairros'], bairro['bairros']) for bairro in Localidades.objects.distinct('bairros').values()])

    class Meta:
        model = Boletins
        fields = ['lista_municipios', 'lista_bairros', 'lista_consolidados', 'data_inicio', 'data_fim', ]
    