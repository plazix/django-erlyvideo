# -*- coding: utf-8 -*-

import functools

from django.http import HttpResponseForbidden

from djerlyvideo.conf.settings import ERLYVIDEO_ACCESS_IPS


def test_access(f):
    @functools.wraps(f)
    def wrapper(request, *args, **kw):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR', None)
        if x_forwarded_for:
            remote_addr = x_forwarded_for.split(',')[0].strip()
        else:
            remote_addr = request.META.get('REMOTE_ADDR', None)
        
        if (ERLYVIDEO_ACCESS_IPS is None) or (remote_addr in ERLYVIDEO_ACCESS_IPS):
            return f(request, *args, **kw)
        return HttpResponseForbidden()
    return wrapper
