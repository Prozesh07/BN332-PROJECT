# Booking/views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from Doctor.models import Doctor  # Assuming Doctor model exists in Doctor app
from .forms import AppointmentForm
from NSW.models import Patient


def book_appointment(request):
    doctor_id = request.GET.get('doctor_id')

    # Check if doctor_id is passed correctly
    if doctor_id:
    # Retrieve the single doctor instance using the doctor_id
        doctors = get_object_or_404(Doctor, pk=doctor_id)  # This will raise 404 if no doctor matches
    else:
        # no doctor selected, the form will allow the user to choose
        doctor = None
        doctors = Doctor.objects.all()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)

        if doctor:
            appointment.doctor = doctors  # Assign the specific doctor
        else:
            appointment.doctor = form.cleaned_data['doctor']
            appointment.save()

            send_verification_email(request, appointment)
            return redirect('home')  # Redirect to a success page after booking
            # return redirect('payment_page')
    else:
        form = AppointmentForm(initial={'doctor': doctors})
    return render(request, 'book_appointment.html', {'form': form, 'doctor': doctors})

from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from .tokens import appointment_verification_token  # Token generator
from .models import Appointment


def send_verification_email(request, appointment):
    # Get the current site (useful if you want to include the domain in the email)
    current_site = get_current_site(request)

    # The subject of the email
    mail_subject = 'Activate your appointment'

    # Generate a unique token and user ID
    uid = urlsafe_base64_encode(force_bytes(appointment.pk))
    token = appointment_verification_token.make_token(appointment)

    # Generate the verification link
    verification_link = reverse('verify_appointment', kwargs={'uidb64': uid, 'token': token})
    full_link = f"http://{current_site.domain}{verification_link}"

    # Construct the email message
    message = f"Hi {appointment.patient_name},\n\nPlease click the link below to confirm your appointment:\n{full_link}"

    # Use Django's send_mail function to send the email
    send_mail(
        mail_subject,
        message,
        'your_email@gmail.com',  # Your email as the sender
        [appointment.patient_email],  # Recipient's email
        fail_silently=False,
    )
from django.utils.http import urlsafe_base64_decode
from django.shortcuts import render, redirect
from .tokens import appointment_verification_token
from .models import Appointment

def verify_appointment(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        appointment = Appointment.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Appointment.DoesNotExist):
        appointment = None

    if appointment is not None and appointment_verification_token.check_token(appointment, token):
        appointment.status = 'confirmed'  # Update appointment status to confirmed
        appointment.save()
        return redirect('appointment_confirmed')  # Redirect to a success page
    else:
        return render(request, 'appointment_invalid.html')  # Render an invalid link page

from django.shortcuts import render

def appointment_confirmed(request):
    return render(request, 'appointment_confirmed.html')

from rest_framework import generics
from .models import Appointment
from .serializers import AppointmentSerializer

class AppointmentListCreateView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
