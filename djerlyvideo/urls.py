# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('.views',
    url(r'^event_handlers$', 'event_handlers', name='erlyvideo_event_handlers'),
    url(r'^publish_auth$', 'publish_auth', name='erlyvideo_publish_auth'),
    url(r'^play_auth$', 'play_auth', name='erlyvideo_play_auth'),
)