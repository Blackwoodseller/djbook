# -*- coding: utf-8 -*-
from django.core.mail import send_mail

from celery.task import task



@task(ignore_result=True, max_retries=1, default_retry_delay=10)
def new_comment_mail(subject, message, from_addr, recipient_list):
    send_mail(subject, message, from_addr, recipient_list)
