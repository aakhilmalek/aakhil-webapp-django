from django.shortcuts import render
from .models import ContactForm
from django.contrib import messages as msg

# Create your views here.



def contact_form(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        messages = request.POST['message']
        contact = request.POST['contact']
        ContactForm.objects.create(name=name,email=email,contact=contact,messages=messages)
        msg.success(request, 'Thank you ,Your form has been submitted successfully')
        return render(request, 'designer/index.html')
    else:
        return render(request, 'designer/index.html')

    return render(request, 'designer/index.html')
