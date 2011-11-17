# -*- coding: utf-8 -*-

from erlyvideo import erlyvideo_session_string

from djerlyvideo.conf.settings import ERLYVIDEO_SECRET_KEY
from djerlyvideo.models import Server


__docformat__ = "restructuredtext"


def get_session_string(user_id, additional_data={}):
    return erlyvideo_session_string(ERLYVIDEO_SECRET_KEY, user_id, additional_data)


def select_server():
    pass