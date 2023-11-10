from rest_framework import serializers 
from .models import Consolidados
 
 
class SerializarConsolidados(serializers.ModelSerializer):
 
    class Meta:
        model = Consolidados
        fields = ('consolidado',
                  )