from django.urls import path
from .views import feedback

urlpatterns = [
    path('', feedback, name='feedback'),
    # path('contact-form/', ContactFormView.as_view(), name='contact_form'),
]