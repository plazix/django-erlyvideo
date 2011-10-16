# -*- coding: utf-8 -*-

from django.conf import settings


ERLYVIDEO_PUBLISH_AUTH_FUNC = getattr(settings, 'ERLYVIDEO_PUBLISH_AUTH_FUNC', None)

ERLYVIDEO_PLAY_AUTH_FUNC = getattr(settings, 'ERLYVIDEO_PLAY_AUTH_FUNC', None)
