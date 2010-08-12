from django.conf.urls.defaults import *
from News.views import archive

urlpatterns = patterns('',
    url(r'^$', archive),
)