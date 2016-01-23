from django.conf.urls import patterns, include, url
from django.contrib import admin
from pulsarvpn.views.step_views import steps
from pulsarvpn.views.button_handler import runKeyGenProcess, runStep3Process, runStep4Process



urlpatterns = patterns(
    '',
    (r'^accounts/', include('allauth.urls')),
    
    url(r'^$', steps, name='steps'),
    url(r'^run-key-gen-process/$', runKeyGenProcess),
    url(r'^run-step3-process/$',runStep3Process, name='runStep3Process'),
    url(r'^run-step4-process/$',runStep4Process, name='runStep4Process'),
)    