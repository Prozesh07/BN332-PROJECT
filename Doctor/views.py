from rest_framework import generics
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorList(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

from django.shortcuts import render
from .models import Doctor  # Import the Doctor model
from rest_framework.views import APIView

# Web-based view for rendering doctors in HTML format
class DoctorWebList(APIView):
    def get(self, request):
        doctors = Doctor.objects.all()  # Fetch all doctors from the database
        return render(request, 'doctor_list.html', {'doctors': doctors})  # Render the doctor list in HTML
