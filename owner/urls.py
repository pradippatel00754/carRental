from django.urls import path, include
from .views import *
urlpatterns = [
    path('cars/',include('cars.urls')),
    path('ownerdashboard/', OwnerDashboard.as_view(), name='ownerdashboard'),
    path('ownerprofile/', OwnerProfile.as_view(), name='ownerprofile'),
    path('profileupdate/<int:pk>', OwnerUpdate.as_view(), name='ownerupdate'),
    path('bookedlist/', BookedListView.as_view(), name="bookedlist"),
    path('upstatus/', BookingStatusUpdate.as_view(), name="upstatus"),
    path('ofeedback/', FeedbackView.as_view(), name="ofeedback"),
]