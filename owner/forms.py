from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from user.models import User
from customer.models import ReservationModel

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'prof_image', 'age', 'mobile', 'location', 'decs']

class UpdateBookingStatusForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UpdateBookingStatusForm, self).__init__(*args, **kwargs)
        self.fields['status'].widget.attrs['class'] = 'form-control'
    class Meta:
        model = ReservationModel
        fields = ['status']