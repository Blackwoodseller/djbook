from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import login, logout
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djbook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^questions/', include('registration.backends.default.urls')),

    # url(r'^questions/', include('questions.urls', namespace='questions')),
    url(r'', include('registr.urls')),
    url(r'^questions/', include('questions.urls', namespace='questions')),
    url(r'^admin/', include(admin.site.urls)),

    # url(r'^$', TemplateView.as_view(template_name='registration/index.html'), name='index'),
    #
    # url(r'^questions/$', views.QuestionsView.as_view(), name='questions'),
    # url(r'^q<question_id>\d+/$', views.QuestionView.as_view(), name='question'),
    # url(r'^new_question/$', views.NewQuestionView.as_view(), name='new_question'),
    #
    # url(r'^accounts/', include('registration.backends.default.urls')),
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^accounts/login/$',  login),
    # url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/accounts/login/'}),
)
