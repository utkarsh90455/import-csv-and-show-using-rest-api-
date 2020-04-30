from rest_framework import serializers
from .models import csvData

class csvDataSerializers(serializers.ModelSerializer):
    class Meta:
        model=csvData
        fields='__all__'



