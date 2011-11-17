# -*- coding: utf-8 -*-

import logging

from django.contrib.auth.models import User
from django.core.urlresolvers import get_callable
from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from djerlyvideo.conf.settings import ERLYVIDEO_PUBLISH_AUTH_FUNC, ERLYVIDEO_PLAY_AUTH_FUNC
from djerlyvideo.decorators import test_access
from djerlyvideo.models import ErlyvideoEvent
from djerlyvideo.signals import server_event, publish_auth as _publish_auth, play_auth as _play_auth


__docformat__ = "restructuredtext"

logger = logging.getLogger('erlyvideo')


def public_auth_sample(server, ip, file, user_id, session_id):
    """
    Пример функции проверки разрешено ли пользователю публиковать поток

    :param server: сервер ``djerlyvideo.models.Server`` отправивший запрос
    :param ip: IP адресс пользователя публикующего поток
    :param file: имя потока
    :param user_id: ID пользователя переданного в данных сессии
    :param session_id: ID сессии
    :return: True - разрешено, False - запрещено
    """
    return True


def play_auth_sample(server, ip, file, user_id, session_id):
    """
    Пример функции проверки разрешено ли пользователю просматривать поток

    :param server: сервер ``djerlyvideo.models.Server`` отправивший запрос
    :param ip: IP адресс пользователя просматривающего поток
    :param file: имя потока
    :param user_id: ID пользователя переданного в данных сессии
    :param session_id: ID сессии
    :return: True - разрешено, False - запрещено
    """
    return True


@csrf_exempt
@test_access
def event_handlers(request):
    logger.debug("%s" % request.POST)

    json_str = request.POST.self.keys()[0]
    event_info = ErlyvideoEvent.load_from_json(json_str)

    server_event.send(sender=ErlyvideoEvent, server=None, event_info=event_info)
    
    return HttpResponse()


@csrf_exempt
@test_access
def publish_auth(request):
    """
    Авторизация при побликации потока
    """
    func = get_callable(ERLYVIDEO_PUBLISH_AUTH_FUNC) if ERLYVIDEO_PUBLISH_AUTH_FUNC else public_auth_sample
    if func(None, request.GET['ip'], request.GET['file'], request.GET['user_id'], request.GET['session_id']):
        _publish_auth.send(sender=User, server=None, ip=request.GET['ip'], file=request.GET['file'], user_id=request.GET['user_id'],
            session_id=request.GET['session_id'])
        return HttpResponse()
    else:
        return HttpResponseForbidden()


@csrf_exempt
@test_access
def play_auth(request):
    """
    Авторизация при проигрывании потока
    """
    func = get_callable(ERLYVIDEO_PLAY_AUTH_FUNC) if ERLYVIDEO_PLAY_AUTH_FUNC else play_auth_sample
    if func(None, request.GET['ip'], request.GET['file'], request.GET['user_id'], request.GET['session_id']):
        _play_auth.send(sender=User, server=None, ip=request.GET['ip'], file=request.GET['file'], user_id=request.GET['user_id'],
            session_id=request.GET['session_id'])
        return HttpResponse()
    else:
        return HttpResponseForbidden()
