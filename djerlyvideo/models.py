# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models


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
        verbose_name_plural = u'Сервера Erlyvideo'

    def __unicode__(self):
        return '%s:%s' % (self.host, self.rtmp_port)

    def admin_connections(self):
        return '%s / %s' % (self.connections, self.max_connections)
    admin_connections.short_description = u'Соединений'


class SessionManager(models.Manager):
    pass


class Session(models.Model):
    TYPE_BROADCAST = 'broadcast'
    TYPE_PLAY = 'play'

    TYPE_CHOICES = (
        ('broadcast', TYPE_BROADCAST),
        ('play', TYPE_PLAY),
    )

    server = models.ForeignKey(Server, related_name='sessions')
    user = models.ForeignKey(User, blank=True, null=True, default=None, related_name='erlyvideo_sessions')
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    stream = models.CharField(max_length=50, db_index=True)
    stream_name = models.CharField(max_length=255, db_index=True)
    start_at = models.DateTimeField(auto_now_add=True)
    finish_at = models.DateTimeField(null=True, blank=True, default=None)

    objects = SessionManager()

    class Meta:
        ordering = ('-start_at',)
        verbose_name = 'Session'
        verbose_name_plural = 'Sessions'

    def __unicode__(self):
        return '%s-%s' % (self.stream, self.stream_name)