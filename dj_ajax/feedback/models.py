from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    phone_number = PhoneNumberField(blank=False)
    
    def __str__(self):
        return f"{self.name} ({self.phone_number})"
    
    