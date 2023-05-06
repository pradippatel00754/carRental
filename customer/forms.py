from django import forms
from .models import ReservationModel, PaymentModel
from user.models import User
class ReservationModelForm(forms.ModelForm):
    class Meta:
        model = ReservationModel
        fields = ['r_user','r_car']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = PaymentModel
        fields = ['ptype']

class CustomerUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CustomerUpdateForm, self).__init__(*args, **kwargs)
        self.fields['lice_image'].widget.attrs['class'] = 'form-control'
        self.fields['prof_image'].widget.attrs['class'] = 'form-control'
        self.fields['decs'].widget.attrs['class'] = 'form-control'
        self.fields['decs'].widget.attrs['placeholder'] = 'Description'
        self.fields['prof_image'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'prof_image', 'age', 'mobile', 'lice_image', 'licence', 'location', 'decs')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Mobile Number'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'licence': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Licence'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Locations'}),
        }