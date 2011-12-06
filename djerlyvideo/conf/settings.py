# -*- coding: utf-8 -*-

from django.conf import settings


# метод для авторизации пользователя при публикации потока
ERLYVIDEO_PUBLISH_AUTH_FUNC = getattr(settings, 'ERLYVIDEO_PUBLISH_AUTH_FUNC', 'erlyvideo.views.public_auth_sample')

# метод для авторизации пользователя при проигрывании потока
ERLYVIDEO_PLAY_AUTH_FUNC = getattr(settings, 'ERLYVIDEO_PLAY_AUTH_FUNC', 'erlyvideo.views.play_auth_sample')

# секретный ключ для подписи сессии Erlyvideo
ERLYVIDEO_SECRET_KEY = getattr(settings, 'ERLYVIDEO_SECRET_KEY', settings.SECRET_KEY)

# нужно ли автоматически сохранять сессии трансляции
ERLYVIDEO_AUTO_SAVE_SESSIONS = getattr(settings, 'ERLYVIDEO_AUTO_SAVE_SESSIONS', False)

# none, random, max_clients
#ERLYVIDEO_LOAD_BALANCING_MODE = getattr(settings, 'ERLYVIDEO_LOAD_BALANCING_MODE', 'none')

#ERLYVIDEO_FILTER_SERVER_BY_GROUP = getattr(settings, 'ERLYVIDEO_FILTER_SERVER_BY_GROUP', False)
