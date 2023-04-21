from django.urls import path, include
from .views import *

urlpatterns = [
    path('ownerregister/', OwnerRegisterView.as_view(), name='ownerregister'),
    path('customerregister/', CustomerRegisterView.as_view(), name='customerregister'),
    path('choice/', ChoiseForSignUp.as_view(), name="choice"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page="login"), name='logout'),
    path('owner/', include('owner.urls')),
]