# -*- coding: utf-8 -*-

from django.db import models
from django.utils import simplejson


#class ErlyvideoStream(object):
#    client_count = None
#    created_at = None
#    host = ''
#    last_dts = None
#    last_dts_at = None
#    name = ''
#    registrator = None
#    ts_delay = None
#    type = None
#    url = ''


class ErlyvideoStats(object):
    def __init__(self, host=None, recv_oct=None, sent_oct=None, addr=None, user_id=None, session_id=None):
        self.host = host
        self.recv_oct = recv_oct
        self.sent_oct = sent_oct
        self.addr = addr
        self.user_id = user_id
        self.session_id = session_id


class ErlyvideoOptions(object):
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


class ErlyvideoEvent(object):
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

        options = ErlyvideoOptions(**data['stats']) if data['stats'] else None
        stats = ErlyvideoStats(**data['stats']) if data['stats'] else None

        return cls(
            data['event'], data['host'], data['user'], data['user_id'], data['session_id'], data['stream'],
            data['stream_name'], options, stats
        )


class ServerManager(models.Manager):
    def active(self):
        """
        Активные сервера
        """
        return self.filter(is_active=True, is_broken=False)

    def find_server(self, group=None):
        """
        Поиск менее жагруженного сервера
        """
        queryset = self.order_by('-connections')
        if group:
            queryset = queryset.filter(group=group)
        return queryset.all()[0]


class Server(models.Model):
    name = models.CharField(u'Имя сервера', max_length=255)
    host = models.CharField(u'Хост', max_length=255)
    rtmp_port = models.CharField(u'RTMP порт', max_length=5, default='1935')
    group = models.CharField(u'Группа сервера', max_length=50, blank=True, null=True, default=None)
    max_connections = models.IntegerField(u'Максимальное число подключений', blank=True, null=True, default=None)
    api_port = models.CharField(u'Порт для обращения к API', max_length=5, default='8082')
    api_user = models.CharField(u'Имя пользователя', max_length=100, blank=True, null=True, default=None)
    api_password = models.CharField(u'Пароль', max_length=100, blank=True, null=True, default=None)
    is_active = models.BooleanField(u'Использовать', default=True)
    
    connections = models.IntegerField(default=0)
    is_broken = models.BooleanField(u'Недоступен', default=False)
    last_success_ping = models.DateTimeField(u'Последний раз отвечал')

    objects = ServerManager()

    class Meta:
        verbose_name = u'Сервер Erlyvideo'
        server_name_plural = u'Сервера Erlyvideo'

    def admin_connections(self):
        return '%s / %s' % (self.connections, self.max_connections)
    admin_connections.short_description = u'Соединений'