from django.urls import path
from .views import contact_form

urlpatterns = [
    path('contact-form/',contact_form,name="contact-form")
    
]