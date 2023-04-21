from django.contrib import admin
from cars.models import *
# Register your models here.
admin.site.register(Car)
admin.site.register(CarType)
admin.site.register(CarCompany)
admin.site.register(CarColor)
