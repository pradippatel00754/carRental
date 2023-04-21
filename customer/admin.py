from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(ReservationModel)
admin.site.register(PaymentTypeModel)
admin.site.register(PaymentModel)
