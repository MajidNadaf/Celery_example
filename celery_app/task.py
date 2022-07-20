import imp

from celery import shared_task 
from time import sleep
from django.core.mail import send_mail

@shared_task
def data_return(a,b):
    print(a+b)
    return None


@shared_task
def send_mail_task():
    send_mail("celery working now","Celery is best feature in django","nadafmajid99@gmail.com",["nadafmajid99@gmail.com"],fail_silently=False)
    return None
