# -*- coding: utf-8 -*-

from erlyvideo import erlyvideo_session_string

from djerlyvideo.conf.settings import ERLYVIDEO_SECRET_KEY


__docformat__ = "restructuredtext"


def get_session_string(user_id, additional_data=None):
    """
    Формирует и подписывает строку сессии для передачи серверу Erlyvideo

    :param user_id: ID пользователя, для аутентификации
    :param additional_data: дополнительные данные переданные как ``dict``
    :return: подписанную строку сессии
    """
    return erlyvideo_session_string(ERLYVIDEO_SECRET_KEY, user_id, additional_data)


def get_remote_address(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR', None)
    if x_forwarded_for:
        remote_addr = x_forwarded_for.split(',')[0].strip()
    else:
        remote_addr = request.META.get('REMOTE_ADDR', None)
    return remote_addr


def select_server():
    pass