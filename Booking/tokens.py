# tokens.py

from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six

class AppointmentVerificationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return six.text_type(user.pk) + six.text_type(timestamp)

appointment_verification_token = AppointmentVerificationTokenGenerator()
