# -*- coding: utf-8 -*-

import logging

from erlyvideo import ErlyvideoEvent

from django.contrib.auth.models import User
from django.core.urlresolvers import get_callable
from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from djerlyvideo.conf.settings import ERLYVIDEO_PUBLISH_AUTH_FUNC, ERLYVIDEO_PLAY_AUTH_FUNC
from djerlyvideo.decorators import test_access
from djerlyvideo.models import Server
from djerlyvideo.signals import server_event, publish_auth as _publish_auth, play_auth as _play_auth


__docformat__ = "restructuredtext"

logger = logging.getLogger('djerlyvideo')


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
    """
    Принимает и обрабатывает информацию о событии от сервера Erlyvideo
    """
    logger.debug("%s" % request.POST)

    json_str = request.POST.self.keys()[0]
    event_info = ErlyvideoEvent.load_from_json(json_str)

    try:
        server = Server.objects.get(host=event_info.host)
    except Server.DoesNotExist:
        logger.warning('Erlyvideo server %s not found.' % event_info.host)
        return HttpResponseForbidden()

    server_event.send(sender=ErlyvideoEvent, server=server, event_info=event_info)
    
    return HttpResponse()


@csrf_exempt
@test_access
def publish_auth(request):
    """
    Авторизация при побликации потока
    """
    server_host = request.META['SERVER_NAME']
    try:
        server = Server.objects.get(host=server_host)
    except Server.DoesNotExist:
        logger.warning('Erlyvideo server %s not found.' % server_host)
        return HttpResponseForbidden()

    func = get_callable(ERLYVIDEO_PUBLISH_AUTH_FUNC)
    if func(server, request.GET['ip'], request.GET['file'], request.GET['user_id'], request.GET['session_id']):
        _publish_auth.send(sender=User, server=None, ip=request.GET['ip'], file=request.GET['file'],
                           user_id=request.GET['user_id'], session_id=request.GET['session_id'])
        return HttpResponse()
    else:
        return HttpResponseForbidden()


@csrf_exempt
@test_access
def play_auth(request):
    """
    Авторизация при проигрывании потока
    """
    server_host = request.META['SERVER_NAME']
    try:
        server = Server.objects.get(host=server_host)
    except Server.DoesNotExist:
        logger.warning('Erlyvideo server %s not found.' % server_host)
        return HttpResponseForbidden()

    func = get_callable(ERLYVIDEO_PLAY_AUTH_FUNC)
    if func(server, request.GET['ip'], request.GET['file'], request.GET['user_id'], request.GET['session_id']):
        _play_auth.send(sender=User, server=None, ip=request.GET['ip'], file=request.GET['file'],
                        user_id=request.GET['user_id'], session_id=request.GET['session_id'])
        return HttpResponse()
    else:
        return HttpResponseForbidden()
