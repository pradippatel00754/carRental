from django.urls import path, include
from .views import *
urlpatterns = [
    path('', CustomerDashboard.as_view(), name="customerdashboard"),
    path('customerprofile/', CustomerProfile.as_view(), name="customerprofile"),
    path('customerupdate/<int:pk>/', CustomerUpdate.as_view(), name="customerupdate"),
    path('feedback/', FeedbackView.as_view(), name="feedback"),
    path('book2/', BookView.as_view(), name="book2"),
    path('payment/', PaymentView.as_view(), name="payment"),
    path('bookedcarlist/', CustomerBookedCarListView.as_view(), name="bookedcarlist"),
]