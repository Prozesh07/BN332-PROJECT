from django.db import models

SPECIALTY_CHOICES = [
    ('general', 'General Practitioner'),
    ('cardiologist', 'Cardiologist'),
    ('pediatrician', 'Pediatrician'),
    ('dermatologist', 'Dermatologist'),
]




class Doctor(models.Model):
    name = models.CharField(max_length=255, default='Unnamed Doctor')  # Required field
    specialty = models.CharField(max_length=255, choices=SPECIALTY_CHOICES, default='general')  # Required field
    phone = models.CharField(max_length=15)  # Required field
    available_from = models.TimeField()  # Expected to be time (e.g., 09:00:00)
    available_to = models.TimeField()  # Expected to be time (e.g., 17:00:00)

    def __str__(self):
        return f"Dr. {self.name} - {self.get_specialty_display()}"
