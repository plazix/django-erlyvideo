# -*- coding: utf-8 -*-

from django.dispatch import Signal


server_event = Signal(providing_args=["event_info"])

publish_auth = Signal(providing_args=['ip', 'file', 'user_id', 'session'])

play_auth = Signal(providing_args=['ip', 'file', 'user_id', 'session'])
