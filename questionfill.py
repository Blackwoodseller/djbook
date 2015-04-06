#/home/alp/projects/venv/bin/python
from questions.views import Question, QuestionComment
from django.contrib.auth.models import User
from django.utils import timezone
import random

user = User.objects.filter(username = 'Marusya')[0]
for i in xrange(10):
    q = Question(author = user, question_title = 'question' + str(i), question_text = 'Description for question #' + str(i), pub_date = timezone.now())
    q.save()
    for j in xrange(1,random.randint(1,20)):
        c = QuestionComment(question = q, author = user, pub_date = timezone.now(), comment_text = 'Comment #' +str(j) + ' for question #' + str(i) + ' : ' +'qwertyuioopasdfghhjkkl;zxcvbnnm,,'[random.randint(1,30)]*random.randint(4,100))
        c.save()
        print str(i) + '.' + str(j)
    q.save()