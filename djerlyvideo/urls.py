# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('djerlyvideo.views',
    url(r'^event_handlers$', 'event_handlers', name='djerlyvideo_event_handlers'),
    url(r'^publish_auth$', 'publish_auth', name='djerlyvideo_publish_auth'),
    url(r'^play_auth$', 'play_auth', name='djerlyvideo_play_auth'),
)