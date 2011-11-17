# -*- coding: utf-8 -*-

from django.conf import settings


ERLYVIDEO_PUBLISH_AUTH_FUNC = getattr(settings, 'ERLYVIDEO_PUBLISH_AUTH_FUNC', 'erlyvideo.views.public_auth_sample')

ERLYVIDEO_PLAY_AUTH_FUNC = getattr(settings, 'ERLYVIDEO_PLAY_AUTH_FUNC', 'erlyvideo.views.play_auth_sample')

# с каких ip разрешен доступ к аутентификации и вызову обработчика события
ERLYVIDEO_ACCESS_IPS = getattr(settings, 'ERLYVIDEO_ACCESS_IPS', None)

ERLYVIDEO_SECRET_KEY = getattr(settings, 'ERLYVIDEO_SECRET_KEY', settings.SECRET_KEY)

# none, random, max_clients
ERLYVIDEO_LOAD_BALANCING_MODE = getattr(settings, 'ERLYVIDEO_LOAD_BALANCING_MODE', 'none')

#ERLYVIDEO_FILTER_SERVER_BY_GROUP = getattr(settings, 'ERLYVIDEO_FILTER_SERVER_BY_GROUP', False)
