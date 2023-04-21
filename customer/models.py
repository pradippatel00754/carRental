import datetime
from django.db import models
from cars.models import Car
from user.models import User

# Create your models here.
class PaymentTypeModel(models.Model):
    name_t = models.CharField(max_length=100)

    class Meta:
        db_table = "p_type"

    def __str__(self):
        return self.name_t

class ReservationModel(models.Model):
    CHOICE = (
        ("PENDING", "PENDING"),
        ("DELIVERED", "DELIVERED"),
        ("CANCEL", "CANCEL"),
        ("RETURN","RETURN"),
    )
    r_user = models.ForeignKey(User, on_delete=models.CASCADE)
    r_car = models.ForeignKey(Car, on_delete=models.CASCADE)
    price = models.FloatField(null=True)
    booked = models.DateTimeField(default=datetime.datetime.today)
    status = models.CharField(choices=CHOICE, null=True, max_length=100, default="PENDING")
    return_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'rev_car'

    def placeOrder(self):
        self.save()

class PaymentModel(models.Model):
    puser = models.ForeignKey(User, on_delete=models.CASCADE)
    pbook = models.ForeignKey(ReservationModel, on_delete=models.CASCADE)
    ptype = models.CharField(max_length=100)
    pdone = models.BooleanField(default=False)
    price = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "payment1"


    def paymentSave(self):
        self.save()

