# -*- coding: utf-8 -*-

from django.utils import simplejson


class ErlyVideoStats(object):
    def __init__(self, host=None, recv_oct=None, sent_oct=None, addr=None, user_id=None, session_id=None):
        self.host = host
        self.recv_oct = recv_oct
        self.sent_oct = sent_oct
        self.addr = addr
        self.user_id = user_id
        self.session_id = session_id


class ErlyVideoOptions(object):
    LIVE = 'live'

    def __init__(self, host=None, name=None, registrator=None, type=None, url=None, bytes_sent=None):
        self.host = host
        self.name = name
        self.registrator = registrator
        self.type = type
        self.url = url
        self.bytes_sent = bytes_sent

    def is_live(self):
        return self.type == self.LIVE


class ErlyVideoEvent(object):
    USER_CONNECTED          = 'user.connected'
    USER_DISCONNECTED       = 'user.disconnected'
    USER_PLAY               = 'user.play'
    USER_STOP               = 'user.stop'
    STREAM_CREATED          = 'stream.created'
    STREAM_STARTED          = 'stream.started'
    STREAM_SOURCE_LOST      = 'stream.source.lost'
    STREAM_SOURCE_REQUESTED = 'stream.source.requested'
    STREAM_STOPPED          = 'stream_stopped'
    SLOW_MEDIA              = 'slow.media'

    def __init__(self, event, host, user, user_id, session_id, stream, stream_name, options, stats):
        if event not in (self.USER_CONNECTED, self.USER_DISCONNECTED, self.USER_PLAY, self.USER_STOP,
                         self.STREAM_CREATED, self.STREAM_STARTED, self.STREAM_SOURCE_LOST,
                         self.STREAM_SOURCE_REQUESTED, self.STREAM_STOPPED, self.SLOW_MEDIA):
            pass

        self.event = event
        self.host = host
        self.user = user
        self.user_id = user_id
        self.session_id = session_id
        self.stream = stream
        self.stream_name = stream_name
        self.options = options
        self.stats = stats

    @classmethod
    def load_from_json(cls, json_str):
        data = simplejson.loads(json_str)

        options = ErlyVideoOptions(**data['stats']) if data['stats'] else None
        stats = ErlyVideoStats(**data['stats']) if data['stats'] else None

        return cls(
            data['event'], data['host'], data['user'], data['user_id'], data['session_id'], data['stream'],
            data['stream_name'], options, stats
        )