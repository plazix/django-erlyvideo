# -*- coding: utf-8 -*-

import logging

from conf.settings import ERLYVIDEO_AUTO_SAVE_SESSIONS


__all__ = ['get_version']

logger = logging.getLogger('djerlyvideo')

VERSION = (0, 2, 0, 'alpha', 1)


def get_version():
    version = '%s.%s' % (VERSION[0], VERSION[1])
    if VERSION[2]:
        version = '%s.%s' % (version, VERSION[2])
    if VERSION[3:] == ('alpha', 0):
        version = '%s pre-alpha' % version
    else:
        if VERSION[3] != 'final':
            version = "%s %s" % (version, VERSION[3])
            if VERSION[4] != 0:
                version = '%s %s' % (version, VERSION[4])
    return version


if ERLYVIDEO_AUTO_SAVE_SESSIONS:
    from datetime import datetime
    from erlyvideo.models import ErlyvideoEvent
    from django.dispatch import receiver
    from models import Session
    from signals import server_event

    @receiver(server_event)
    def server_event_callback(server, event_info, **kwargs):
        if event_info.event not in [ErlyvideoEvent.STREAM_STARTED, ErlyvideoEvent.STREAM_STOPPED,
                                    ErlyvideoEvent.USER_PLAY, ErlyvideoEvent.USER_STOP]:
            return

        try:
            active_session = Session.objects.get(server=server, stream=event_info.stream,
                stream_name=event_info.stream_name, finish_at=None)
        except Session.DoesNotExist:
            active_session = None

        if event_info.event in [ErlyvideoEvent.STREAM_STARTED, ErlyvideoEvent.USER_PLAY]:
            if active_session:
                logger.warning('Session "%s-%s" already exists and active.' % (event_info.stream, event_info.stream_name))
                active_session.finish_at = datetime.today()
                active_session.save()

            session_type = Session.TYPE_BROADCAST if ErlyvideoEvent.STREAM_STARTED == event_info.event else Session.TYPE_PLAY
            session = Session(server=server, type=session_type, stream=event_info.stream,
                stream_name=event_info.stream_name, user=event_info.user_id)
            session.save()

        if event_info.event in [ErlyvideoEvent.STREAM_STOPPED, ErlyvideoEvent.USER_STOP]:
            if active_session:
                active_session.finish_at = datetime.today()
                active_session.save()
            else:
                logger.warning('Session "%s-%s" not found.' % (event_info.stream, event_info.stream_name))
