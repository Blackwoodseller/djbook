from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import login, logout, views  #as auth_views
from django.views.generic import TemplateView

from questions import views as q_views

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='questions/index.html'), name='index'),
    url(r'^page(?P<page>\d+)/$', q_views.QuestionsView.as_view(),name='question_list' ),
    url(r'^(?P<question_id>\d+)/page(?P<page>\d+)/$', q_views.QuestionView.as_view(), name='question'),
    url(r'^new_comment/(?P<question_id>\d+)/$', q_views.NewQuestCommentFormView.as_view(), name='new_comment'),
    url(r'^new_question/$', q_views.NewQuestFormView.as_view(), name='new_question'),
    )
