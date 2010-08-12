from django.conf.urls.defaults import *
from Accounts.views import login, register

urlpatterns = patterns('',                       
    url(r'^$', login),
    url(r'^login', login),
    url(r'^register', register),
)