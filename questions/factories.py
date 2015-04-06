import factory

import datetime

from django.contrib.auth.models import User
from django.contrib.webdesign import lorem_ipsum

from questions.models import Question, QuestionComment


class QuestionFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Question

    # @factory.lazy_attribute_sequence
    # def author(self, n):
    #     author = User.objects.create(email='admin-{}@example.com'.format(n), username='admin-{}'.format(n))
    #     author.set_password('admin-{}'.format(n))
    #     author.save()
    #     return author

    @factory.lazy_attribute
    def question_title(self):
        return lorem_ipsum.words(5, True)

    @factory.lazy_attribute
    def question_text(self):
        return lorem_ipsum.words(25, True)

    @factory.lazy_attribute
    def pub_date(self):
        return datetime.datetime.now()

    # question = models.ForeignKey(Question)
    # author = models.ForeignKey(User)
    # comment_text = models.CharField(max_length=1500)
    # pub_date = models.DateTimeField('date published', auto_now_add=True)


class QuestionCommentFactory(factory.DjangoModelFactory):
    FACTORY_FOR = QuestionComment

    # @factory.lazy_attribute
    # def question(self):
    #     return Question.objects.all().order_by('?')[0]

    @factory.lazy_attribute_sequence
    def author(self, n):
        author = User.objects.create(email='admin-{}@example.com'.format(n), username='admin-{}'.format(n))
        author.set_password('admin-{}'.format(n))
        author.save()
        return author

    @factory.lazy_attribute
    def pub_date(self):
        return datetime.datetime.now()

    @factory.lazy_attribute
    def comment_text(self):
        return lorem_ipsum.words(10, True)
