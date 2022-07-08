from rest_framework import serializers
from core.models import Suscripcion
class SuscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suscripcion
        fields =['nombre','fecha_suscripcion','descuento','precio']