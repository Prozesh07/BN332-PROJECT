from django import forms
from .models import Appointment
from Doctor.models import Doctor
from NSW.models import Patient


class AppointmentForm(forms.ModelForm):
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(), empty_label="Select a Doctor",
                                    widget=forms.Select(attrs={'class': 'form-control'})
                                    )
    patient_name = forms.CharField(max_length=100, required=True)
    patient_contact_number = forms.CharField(max_length=15, required=True)
    patient_email = forms.EmailField(required=True)

    class Meta:
        model = Appointment
        fields = ['doctor', 'appointment_date', 'symptoms', 'patient_name', 'patient_contact_number', 'patient_email']  # Fields to show in the form
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
            'symptoms': forms.Textarea(attrs={'rows': 3}),
        }


