"""
URL configuration for DoctorBS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from NSW.views import index, doctor_list, book_appointment, aboutus
import NSW.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', NSW.views.index),
    path('', index, name='home'),
    path('doctors/', doctor_list, name='doctor_list'),
    # path('book-appointment/', book_appointment, name='book_appointment'),
    path('aboutus/', aboutus, name='aboutus'),
    path('api/', include('Doctor.urls')),
    path('api/', include('Booking.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/nsw/', include('NSW.urls')), # Enable DRF's built-in auth
]
