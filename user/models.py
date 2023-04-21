from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    is_owner = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    prof_image = models.ImageField(upload_to="profile_images/", default='default-pic.jpg', null=True, blank=True)
    age = models.IntegerField(null=True)
    licence = models.CharField(max_length=100, null=True)
    lice_image = models.ImageField(upload_to="licence_image/", default='default-pic.jpg', null=True, blank=True)
    mobile = models.IntegerField(null=True)
    location = models.CharField(max_length=100, null=True)
    decs = models.TextField(max_length=300, null=True)

    class Meta:
        db_table = 'user'

class FeedbackModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    feedback = models.TextField(max_length=500)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "feedback"