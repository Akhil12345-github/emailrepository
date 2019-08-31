from django.shortcuts import render, redirect
from emailproject import settings
from django.core.mail import send_mail

def index(request):
    subject = 'Hi Yashwanth'
    message = ' Thinnavara '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['yashwanthreddy9876@gmail.com',]
    send_mail(subject, message, email_from, recipient_list, fail_silently=False)
    return render(request, 'emailapp/index.html')
