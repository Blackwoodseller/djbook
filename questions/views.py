# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect, request
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic

from questions.mixins import LoginRequiredMixin #, AjaxableResponseMixin
from questions.models import Question, QuestionComment
from questions.forms import NewQuestionForm, NewCommentForm


class QuestionsView(LoginRequiredMixin, generic.ListView):
    """ Class for Question list  with desc pub_date order """
    model = Question
    template_name = 'questions/questions.html'
    context_object_name = 'latest_question_list'
    paginate_by = 10

    def get_queryset(self):
         # return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date') #[:10]
         return Question.objects.order_by('-pub_date')


class QuestionView( LoginRequiredMixin, generic.ListView):  # AjaxableResponseMixin,
    """ Class for Question with comments/answers in pagination and comment form """
    model = QuestionComment
    form_class = NewCommentForm
    template_name = 'questions/question.html'
    context_object_name = 'comments_list'
    paginate_by = 10

    # def post(self, request, *args, **kwargs):
    #     comment = QuestionComment(author=self.request.user,
    #                               question=Question.objects.get(pk=kwargs['question_id']),
    #                               comment_text=self.request.POST['comment_text'])
    #     comment.save()
    #     return HttpResponseRedirect(reverse_lazy('questions:question', args=[self.kwargs['question_id'], 1]))

    def get_queryset(self):
        return QuestionComment.objects.filter(question__pk = int(self.kwargs['question_id'])).order_by('-pub_date')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(QuestionView, self).get_context_data(**kwargs)
        context['question'] = Question.objects.get(pk = int(self.kwargs['question_id']))
        context['form'] = NewCommentForm
        return context


class NewQuestFormView(LoginRequiredMixin, generic.CreateView):
    form_class = NewQuestionForm
    template_name = 'questions/new_question.html'
    success_url = reverse_lazy('questions:question_list', args=[1]) #'/questions/page1/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NewQuestCommentFormView(LoginRequiredMixin, generic.CreateView):
    form_class = NewCommentForm
    template_name = 'questions/question.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.question = Question.objects.get(pk=self.kwargs['question_id'])
        self.object.save()
        return HttpResponseRedirect(reverse_lazy('questions:question', args=[self.kwargs['question_id'], 1]))



