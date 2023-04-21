from django.db import models
from user.models import User

# Create your models here.
class CarType(models.Model):
    car_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cartype'

    def __str__(self):
        return self.car_type

class CarColor(models.Model):
    color = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'carcolor'

    def __str__(self):
        return self.color
class CarCompany(models.Model):
    car_com = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'carcompany'

    def __str__(self):
        return self.car_com

class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    car_model = models.CharField(max_length=10)
    carcompany = models.ForeignKey(CarCompany, null=True, on_delete=models.CASCADE)
    year = models.IntegerField()
    color = models.ForeignKey(CarColor, null=True, on_delete=models.CASCADE)
    car_image = models.ImageField(upload_to="cars_images/", null=True, blank=True)
    cartype = models.ForeignKey(CarType, null=True, on_delete=models.CASCADE)
    rentalrate = models.FloatField()
    availability = models.BooleanField(default=True)
    desc = models.TextField(max_length=500,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cars'

    def __str__(self):
        return self.car_model

    def saveCar(self):
        self.save()
