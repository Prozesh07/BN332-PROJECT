# Doctor/urls.py

from django.urls import path
from .views import DoctorList, DoctorDetail, DoctorWebList

urlpatterns =[
    path('doctors/', DoctorWebList.as_view(), name='doctor-web-list'),
    path('doctors/', DoctorList.as_view(), name='doctor_list'),  # List and create doctors
    path('doctors/<int:pk>/', DoctorDetail.as_view(), name='doctor_detail'),  # Retrieve, update, and delete a doctor
]
