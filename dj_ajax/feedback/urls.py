from django.urls import path
from .views import feedback_form

urlpatterns = [
    path('', feedback_form, name='feedback'),
    # path('contact-form/', ContactFormView.as_view(), name='contact_form'),
]