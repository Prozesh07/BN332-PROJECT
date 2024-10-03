from django.http import HttpResponse
from django.urls import path

from . import views
from .views import ProfileList, PatientList, NotificationList, FeedbackList, book_appointment


def test_view(request):
    print("Request reached the test view")
    return HttpResponse("Test")

urlpatterns = [
    path('profiles/', ProfileList.as_view(), name='profile-list'),
    path('patients/', PatientList.as_view(), name='patient-list'),
    path('notifications/', NotificationList.as_view(), name='notification-list'),
    path('feedbacks/', FeedbackList.as_view(), name='feedback-list'),
    # path('book-appointment/', book_appointment, name='book_appointment'),
    path('test-url/', test_view, name='test_url'),
]
