import imp
from django.shortcuts import render
from django.http import HttpResponse
from .task import *
from django.core.mail import send_mail
# Create your views here.

def index(request):
    send_mail_task.delay()
    # send_mail("celery working now","Celery is best feature in django","nadafmajid99@gmail.com",["nadafmajid99@gmail.com"],fail_silently=False)
    return HttpResponse("<h1>Hello World </h1>")
