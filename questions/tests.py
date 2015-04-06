import datetime
from django.utils import timezone

from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.core import mail


from questions.models import Question, QuestionComment
from questions.factories import QuestionFactory, QuestionCommentFactory




# def create_question(author, question_title, question_text, pub_date=timezone.now()):
#     """
#     Creates a question with the given `question`
#     """
#     return Question.objects.create(author=author, question_title=question_title, question_text=question_text,
#                                    pub_date=pub_date)

class QuestionTest(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_superuser(email='admin@example.com', password='', username='admin')
        self.user1.set_password('admin')
        self.user1.save()
        # self.user2 = User.objects.create_superuser(email='qwerty@example.com', password='', username='qwerty')
        # self.user2.set_password('qwerty')
        # self.user2.save()
        # self.questions1 = QuestionFactory.create_batch(2, author=self.user1 )
        # self.questions2 = QuestionFactory.create_batch(3, author=self.user1 )

        self.question1 = Question.objects.create(author=self.user1, question_title='description',
                                                 question_text='How many more time ?')
        self.question1.pub_date = timezone.make_aware(datetime.datetime(2009, 12, 29, 10, 0, 0), timezone.get_default_timezone())
        self.question1.save()
        print 'pub_date' + str(self.question1.pub_date)

        # self.question1 = self.questions1[0] #QuestionFactory(author=self.user1)
        #self.question2 =  self.questions2[0]   #QuestionFactory(author=self.user2)
        self.question2 = Question(author=self.user1, question_title='qtitle', question_text='qtext')
        self.question2.save()

        self.comments1 = QuestionCommentFactory.create_batch(3, question=self.question1)
        self.comments2 = QuestionCommentFactory.create_batch(5, question=self.question2)
        #
        # self.comments1[0].author = self.user1
        # self.comments1[0].comment_text = 'commentarium'
        # self.comments1[0].pub_date = self.question1.pub_date

        self.comment1 = QuestionComment(author=self.user1, question=self.question1, comment_text='commentarium',
                                        pub_date=self.question1.pub_date)
        self.comment2 = QuestionComment(author=self.user1, question=self.question1, comment_text='another comment')

    def test_index(self):
        url = reverse('questions:index')
        resp = self.client.get(url, follow=True)
        self.assertEqual(resp.status_code, 200)

    def test_question_list(self):
        url = reverse('questions:question_list', kwargs={'page': 1})
        resp = self.client.get(url, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, _('Login'))

        self.client.login(username=self.user1.username, password='admin')
        resp = self.client.get(url, follow=True)
        self.assertEqual(resp.status_code, 200)
    #
    #     for order in self.orders1:
    #         self.assertContains(resp, order.get_absolute_url(), 2)
    #         self.assertNotContains(resp, self.orders3.get_absolute_url())
    #         for order in self.orders2:
    #             self.assertNotContains(resp, order.get_absolute_url())

    def test_question(self):
        url = reverse('questions:question', kwargs={'question_id': self.question1.pk, 'page': 1, })
        resp = self.client.get(url, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, _('Login'))

        self.client.login(username=self.user1.username, password='admin')
        resp = self.client.get(url, follow=True)
        self.assertEqual(resp.status_code, 200)


        # self.assertEqual(QuestionComment.objects.filter(question=self.question1).count(), 3)
        # self.assertEqual(QuestionComment.objects.filter(question=self.question2).count(), 5)

    # def test_new_comment(self):
    #     print 'id: ' + str(self.question1.id)
    #     # url = reverse('questions:new_comment', kwargs={'question_id': str(self.question1.id) })
    #     url = reverse('questions:new_comment', args=[self.question1.id])
    #     resp = self.client.get(url, follow=True)
    #     self.assertEqual(resp.status_code, 200)
    #     self.assertContains(resp, _('Login'))
    #
    #     self.client.login(username=self.user1.username, password='admin')
    #     resp = self.client.get(url, follow=True)
    #     self.assertEqual(resp.status_code, 200)

    def test_new_question(self):
        url = reverse('questions:new_question')
        resp = self.client.get(url, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, _('Login'))

        self.client.login(username=self.user1.username, password='admin')
        resp = self.client.get(url, follow=True)
        self.assertEqual(resp.status_code, 200)

    def test_question_unicode(self):
        # self.assertEqual(self.question1,self.comment_text[:100] + ' ' + self.pub_date.strftime('%d.%m.%Y at %H:%M') )
        self.assertEqual(self.question1.__unicode__(), 'description by admin 29.12.2009 at 10:00')


    def test_question_get_descr(self):
        self.assertEqual(self.question1.get_descr(),'description by admin 29.12.2009 at 10:00 (How many more time ?)')
        self.question1.question_text = 'How many more time ?'*5 + '!'
        self.assertEqual(self.question1.get_descr(),'description by admin 29.12.2009 at 10:00 (' +\
                                                    'How many more time ?How many more time ?How many more time ?' +\
                                                    'How many more time ?How many more time ?...)')
    def test_question_was_published_recently(self):
        self.assertFalse(self.question1.was_published_recently())
        self.assertTrue(self.question2.was_published_recently())

    def test_question_get_absolute_url(self):
        self.assertEqual(self.question1.get_absolute_url(), '/questions/' + str(self.question1.pk) + '/page1/')

    def test_question_get_avatar24(self):
        self.assertEqual(self.question1.avatar24(),
                         'http://www.gravatar.com/avatar/e64c7d89f26bd1972efa854d13d7dd61?d=mm&s=24')

    def test_question_pretty_pub_date(self):
        self.assertEqual(self.question1.pretty_pub_date(), '29.12.2009 at 10:00')

    def test_question_comment_unicode(self):
        self.assertEqual(self.comment1.__unicode__(), 'commentarium 29.12.2009 at 10:00')

    def test_question_comment_get_avatar24(self):
        self.assertEqual(self.comment1.avatar24(),
                         'http://www.gravatar.com/avatar/e64c7d89f26bd1972efa854d13d7dd61?d=retro&s=24')

    def test_question_comment_pretty_pub_date(self):
        self.assertEqual(self.comment1.pretty_pub_date(), '29.12.2009 at 10:00')

    def test_add_comment_signal(self):
        self.comment_r = QuestionComment(author=self.user1, question=self.question1, comment_text='commentarium',
                                        pub_date=self.question1.pub_date)
        self.comment_r.save()
        self.assertGreater(len(mail.outbox), 1)