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
class OwnerUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OwnerUpdateForm, self).__init__(*args, **kwargs)
        self.fields['decs'].widget.attrs['class'] = 'form-control'
        self.fields['decs'].widget.attrs['placeholder'] = 'Description'
        self.fields['prof_image'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'prof_image', 'age', 'mobile', 'location', 'decs')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Mobile Number'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'location': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Locations'}),
        }