from __future__ import absolute_import

from django.conf.urls.defaults import patterns, url

from .views import access_action

urlpatterns = patterns('',
    url('(?P<gate>\d+)/$', access_action, name='access_action'),
)
