from rest_framework import serializers
from .models import Profile, Patient, Notification, Feedback

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['user','email', 'contact_number']
        # To make fields optional
        extra_kwargs = {
            'user': {'required': True},
            'email': {'required': True},
            'contact_number': {'required': True},  # Remove 'required' if you want this to be optional
        }

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['appointment', 'amount', 'date', 'status']
