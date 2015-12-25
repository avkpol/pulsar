from django.conf.urls import patterns, include, url
from django.contrib import admin
from pulsarvpn.views.step_views import step1, step3, welcome
from pulsarvpn.views.button_handler import runKeyGenProcess




urlpatterns = patterns(
    '',
    (r'^accounts/', include('allauth.urls')),
    url(r'^welcomepage/$', welcome, name='welcome'),
    url(r'^step1/$', step1, name='step1'),
    # url(r'^step2/$', generate_keys, name='step2'),
    # url(r'^profile/$', user_profile, name='profile'),
    url(r'^run-key-gen-process/$', runKeyGenProcess),
    url(r'^step3/$', step3, name='step3'),
)    