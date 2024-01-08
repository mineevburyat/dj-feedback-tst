from django import forms 
from .models import Feedback
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
    phone_number = PhoneNumberField(region="RU")
    
        
        