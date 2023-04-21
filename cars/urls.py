from django.urls import path, include
from .views import *

urlpatterns = [
    path('createcar/', CreateCarView.as_view(), name="carcreate"),
    path('deletecar/<int:pk>', DeleteCarView.as_view(), name="deletecar"),
    path('updatecar/<int:pk>', UpdateCarView.as_view(), name="updatecar"),
    path('detailscar/<int:pk>', DetailCarView.as_view(), name="detailscar"),
]