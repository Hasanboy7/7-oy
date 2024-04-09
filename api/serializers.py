from rest_framework import serializers
from .models import CrudModel

class CrudSerializer(serializers.ModelSerializer):
    class Meta:
        model=CrudModel
        fields='__all__'
            