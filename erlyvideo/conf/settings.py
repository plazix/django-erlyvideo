# -*- coding: utf-8 -*-

from django.conf import settings


ERLYVIDEO_PUBLISH_AUTH_FUNC = getattr(settings, 'ERLYVIDEO_PUBLISH_AUTH_FUNC', None)

ERLYVIDEO_PLAY_AUTH_FUNC = getattr(settings, 'ERLYVIDEO_PLAY_AUTH_FUNC', None)

# с каких ip разрешен доступ к аутентификации и вызову обработчика события
ERLYVIDEO_ACCESS_IPS = getattr(settings, 'ERLYVIDEO_ACCESS_IPS', None)