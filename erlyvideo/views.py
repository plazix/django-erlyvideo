# -*- coding: utf-8 -*-

import logging

from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from erlyvideo.conf.settings import ERLYVIDEO_PUBLISH_AUTH_FUNC, ERLYVIDEO_PLAY_AUTH_FUNC
from erlyvideo.decorators import test_access
from erlyvideo.models import ErlyVideoEvent
from erlyvideo.signals import server_event, publish_auth, play_auth


logger = logging.getLogger('erlyvideo')


def public_auth_sample(ip, file, user_id, session_id):
    return True


def play_auth_sample(ip, file, user_id, session_id):
    return True


@csrf_exempt
@test_access
def event_handlers(request):
    logger.debug("%s" % request.POST)

    json_str = request.POST.self.keys()[0]
    event_info = ErlyVideoEvent.load_from_json(json_str)

    server_event.send(sender=ErlyVideoEvent, event_info=event_info)
    
    return HttpResponse()


@csrf_exempt
@test_access
def publish_auth(request):
    """
    Авторизация при побликации потока
    """
    func = ERLYVIDEO_PUBLISH_AUTH_FUNC if ERLYVIDEO_PUBLISH_AUTH_FUNC else public_auth_sample
    if func(request.GET['ip'], request.GET['file'], request.GET['user_id'], request.GET['session_id']):
        publish_auth.send(sender=User, ip=request.GET['ip'], file=request.GET['file'], user_id=request.GET['user_id'],
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
    func = ERLYVIDEO_PLAY_AUTH_FUNC if ERLYVIDEO_PLAY_AUTH_FUNC else play_auth_sample
    if func(request.GET['ip'], request.GET['file'], request.GET['user_id'], request.GET['session_id']):
        play_auth.send(sender=User, ip=request.GET['ip'], file=request.GET['file'], user_id=request.GET['user_id'],
            session_id=request.GET['session_id'])
        return HttpResponse()
    else:
        return HttpResponseForbidden()