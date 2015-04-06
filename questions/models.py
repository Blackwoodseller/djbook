# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import signals
from django.core.urlresolvers import reverse

from hashlib import md5
from tasks import  new_comment_mail

from djbook.settings import DEFAULT_FROM_EMAIL


class Question(models.Model):
    author = models.ForeignKey(User)
    question_title = models.CharField(max_length=200)
    question_text = models.CharField(max_length=1500)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __unicode__(self):
        return self.question_title + ' by ' + str(self.author)  +  ' ' +self.pub_date.strftime('%d.%m.%Y at %H:%M')

    def get_descr(self):
       return ('{} by {} {} ({}{})').format((self.question_title).encode('utf-8'), self.author.username,
                                               self.pub_date.strftime('%d.%m.%Y at %H:%M'), (self.question_text[:100]).encode('utf-8'),
                               '...' if len((self.question_text).encode('utf-8')) > 100 else '')

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - timezone.timedelta(days=1)) and self.pub_date <= timezone.now()
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def get_absolute_url(self):
        return reverse('questions:question', kwargs={'question_id': self.pk, 'page': 1})

    def avatar24(self):
        return 'http://www.gravatar.com/avatar/' + md5(self.author.email).hexdigest() + '?d=mm&s=' + str(24)

    def pretty_pub_date(self):
        return self.pub_date.strftime('%d.%m.%Y at %H:%M')


class QuestionComment(models.Model):
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)
    comment_text = models.CharField(max_length=1500)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __unicode__(self):
        return self.comment_text[:100] + ' ' + self.pub_date.strftime('%d.%m.%Y at %H:%M')

    def avatar24(self):
        return 'http://www.gravatar.com/avatar/' + md5(self.author.email).hexdigest() + '?d=retro&s=' + str(24)

    def pretty_pub_date(self):
        return self.pub_date.strftime('%d.%m.%Y at %H:%M')


def notify_comment(sender, instance, created, **kwargs):
    '''send mail for new comment'''
    if created: # and instance.status == 1:
       subject = '%s commented your question %s' % (instance.author.username, instance.question.question_title[:50])
       message = 'User %s in your question ( %s ) add this comment: %s' % ( instance.author.username, instance.question.question_title, instance.comment_text)
       from_addr = DEFAULT_FROM_EMAIL
       recipient_list = (instance.question.author.email,)
       new_comment_mail(subject, message, from_addr, recipient_list)

signals.post_save.connect(notify_comment, sender=QuestionComment)

