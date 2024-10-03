from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Doctor, Patient, Appointment, Profile, Medication, Notification, Payment, Feedback

# Registering models to the admin site
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Profile)
admin.site.register(Medication)
admin.site.register(Notification)
admin.site.register(Payment)
admin.site.register(Feedback)
