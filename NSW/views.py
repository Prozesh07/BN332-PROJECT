from django.shortcuts import render, get_object_or_404


def index(request):
    return render(request,'base.html')
    return render(request, 'home.html')

def doctor_list(request):
    return render(request, 'doctor_list.html')

def book_appointment(request):
    return render(request, 'book_appointment.html')

def aboutus(request):
    return render(request, 'aboutus.html')

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Profile, Patient, Notification, Feedback, Appointment
from .serializers import ProfileSerializer, PatientSerializer, NotificationSerializer, FeedbackSerializer

# Profile API
class ProfileList(APIView):
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Patient API
class PatientList(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

# Notification API
class NotificationList(APIView):
    def get(self, request):
        notifications = Notification.objects.all()
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Feedback API
class FeedbackList(APIView):
    def get(self, request):
        feedbacks = Feedback.objects.all()
        serializer = FeedbackSerializer(feedbacks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




