from rest_framework import serializers
from .models import Registros

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registros
        fields = ("d_codigo","d_asenta","d_tipo_asenta","D_mnpio","d_estado","d_ciudad","d_CP","c_estado","c_oficina","c_CP","c_tipo_asenta","c_mnpio","id_asenta_cpcons","d_zona","c_cve_ciudad")