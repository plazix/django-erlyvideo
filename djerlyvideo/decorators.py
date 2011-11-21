# -*- coding: utf-8 -*-

import functools
import socket

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponseForbidden

from djerlyvideo.models import Server
from djerlyvideo.utils import get_remote_address


__SERVER_IPS = []


def test_access(f):
    @functools.wraps(f)
    def wrapper(request, *args, **kw):
        global __SERVER_IPS

        remote_addr = get_remote_address(request)
        servers = Server.objects.active().all()
        for server in servers:
            ip = socket.gethostbyname(server.host)
            __SERVER_IPS.append(ip)

        if remote_addr in __SERVER_IPS:
            return f(request, *args, **kw)
        return HttpResponseForbidden()
    return wrapper


@receiver(post_save, sender=Server)
def server_post_save(**kwargs):
    global __SERVER_IPS
    __SERVER_IPS = []