#from __future__ import absolute_import
#from celery.decorators import periodic_task
#from celery.decorators import task
#from django.core.mail import send_mail
#from celery.task.schedules import crontab
from pressp.celery import app
from django.core.mail import send_mail


@app.task
def user_send_activation_email(user):
     send_mail('You Have Uploaded a talk', 'Confirmation mail', 'settings.EMAIL_HOST_USER',[user.email], fail_silently=False)

@app.task
def user_upload_activation_email(user):
    send_mail('You Have Edited your talk', 'Confirmation mail You Have Edited your talk ', 'settings.EMAIL_HOST_USER',[user.email], fail_silently=True)  

