from rest_framework import serializers 
from .models import Localidades
 
 
class SerializarLocalidades(serializers.ModelSerializer):
 
    class Meta:
        model = Localidades
        fields = ('risp',
                  'municipios',
                  'bairros',
                  )