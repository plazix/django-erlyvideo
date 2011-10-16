# -*- coding: utf-8 -*-

from hashlib import sha1
import base64
import hmac

from django.utils import simplejson

from erlyvideo.conf.settings import ERLYVIDEO_SECRET_KEY


__docformat__ = "restructuredtext"


def get_session_string(user, additional_data={}):
    """
    Формирует строку с данными сессии для erlyvideo

    :param request: ``django.contrib.auth.models.User``
    :param additional_data: дополнительные данные, которые необходимо передать erlyvideo
    :return: строка с данными сессии
    """

    session = {
        'user_id': user.id if user.is_authenticated() else None
    }
    session.update(additional_data)
    session_base64 = base64.b64encode(simplejson.dumps(session))
    session_signature = hmac.new(ERLYVIDEO_SECRET_KEY, session_base64, digestmod=sha1).hexdigest()
    return '%s--%s' % (session_base64, session_signature)
