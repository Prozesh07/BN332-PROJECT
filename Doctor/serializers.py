from rest_framework import serializers
from .models import Doctor


class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialty', 'email', 'phone', 'available_from', 'available_to']

    def validate(self, data):
        if data['available_from'] >= data['available_to']:
            raise serializers.ValidationError("available_from must be earlier than available_to.")
        return data