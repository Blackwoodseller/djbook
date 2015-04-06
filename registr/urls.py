from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import login, logout, views  #as auth_views
from django.views.generic import TemplateView

from questions import views as q_views

urlpatterns = patterns('',

    url(r'^$', TemplateView.as_view(template_name='questions/index.html'), name='index'),
    # url(r'^admin/', include(admin.site.urls)),

    #override the default urls
    url(r'^password/change/$',
                views.password_change,
                name='password_change'),
    url(r'^password/change/done/$',
                views.password_change_done,
                name='password_change_done'),
    url(r'^password/reset/$',
                views.password_reset,
                name='password_reset'),
    url(r'^password/reset/done/$',
                views.password_reset_done,
                name='password_reset_done'),
    url(r'^password/reset/complete/$',
                views.password_reset_complete,
                name='password_reset_complete'),
    url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
                views.password_reset_confirm,
                name='password_reset_confirm'),

    url(r'', include('registration.backends.default.urls')),
    url(r'^accounts/login/$',  login),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'), #, {'next_page': '/accounts/login/'}),
    url(r'', include('social_auth.urls')),
    )
