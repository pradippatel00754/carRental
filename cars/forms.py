from django import forms
from cars.models import Car

class CreateCarForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateCarForm, self).__init__(*args, **kwargs)
        self.fields['carcompany'].widget.attrs['class'] = 'form-control'
        self.fields['carcompany'].widget.attrs['placeholder'] = 'Car Company'
        self.fields['color'].widget.attrs['class'] = 'form-control'
        self.fields['cartype'].widget.attrs['class'] = 'form-control'
        self.fields['cartype'].widget.attrs['placeholder'] = 'Car Type'
        self.fields['car_image'].widget.attrs['class'] = 'form-control'
        self.fields['car_image'].widget.attrs['placeholder'] = 'Car Image'
        self.fields['desc'].widget.attrs['class'] = 'form-control'
        self.fields['desc'].widget.attrs['placeholder'] = 'Description'


    class Meta:
            model = Car
            fields = '__all__'
            exclude = ['user','availability']
            widgets = {
                'car_model': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Car Model'}),
                'year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Year'}),
                'rentalrate': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Rental Rate'}),
            }

class UpdateCarForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateCarForm, self).__init__(*args, **kwargs)
        self.fields['carcompany'].widget.attrs['class'] = 'form-control'
        self.fields['carcompany'].widget.attrs['placeholder'] = 'Car Company'
        self.fields['color'].widget.attrs['class'] = 'form-control'
        self.fields['cartype'].widget.attrs['class'] = 'form-control'
        self.fields['cartype'].widget.attrs['placeholder'] = 'Car Type'
        self.fields['car_image'].widget.attrs['class'] = 'form-control'
        self.fields['car_image'].widget.attrs['placeholder'] = 'Car Image'
        self.fields['desc'].widget.attrs['class'] = 'form-control'
        self.fields['desc'].widget.attrs['placeholder'] = 'Description'


    class Meta:
            model = Car
            fields = '__all__'
            exclude = ['user','availability']
            widgets = {
                'car_model': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Car Model'}),
                'year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Year'}),
                'rentalrate': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Rental Rate'}),
            }