from django.shortcuts import render
from django.core.mail import send_mail
import asyncio


def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']


        # Send Email
        send_mail(
            message_name, # subject
            message , # message
            message_email , # from email
            ['awalker@gmail.com'], # to email
            fail_silently=False, 
        )


        return render(request, 'contact.html', {'message_name': message_name})
    else:
        pass
        return render(request, 'contact.html', {})


# "message-name"
# "message-email"
# "message"

# 'message_email': message_email, 'message': message