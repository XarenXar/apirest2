from rest_framework import serializers
from .models import Datos


class DatosSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    company_Id = serializers.CharField()
    zubale_Id = serializers.IntegerField()
    determinante = serializers.IntegerField()
   

    def create(self, validated_data):
        """
        Create and return a new `Serie` instance, given the validated data.
        """
        return Serie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Serie` instance, given the validated data.
        """
        instance.company_Id = validated_data.get('company_Id', instance.company_Id)
        instance.zubale_Id = validated_data.get('zubale_Id', instance.zubale_Id)
        instance.determinante = validated_data.get('determinante', instance.determinante)
        instance.save()
        return instance