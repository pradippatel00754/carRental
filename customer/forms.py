from django.forms import ModelForm
from .models import ReservationModel, PaymentModel
class ReservationModelForm(ModelForm):
    class Meta:
        model = ReservationModel
        fields = ['r_user','r_car']

class PaymentForm(ModelForm):
    class Meta:
        model = PaymentModel
        fields = ['ptype']