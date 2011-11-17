# -*- coding: utf-8 -*-

from django.dispatch import Signal


server_event = Signal(providing_args=['server', 'event_info'])

publish_auth = Signal(providing_args=['server', 'ip', 'file', 'user_id', 'session'])

play_auth = Signal(providing_args=['server', 'ip', 'file', 'user_id', 'session'])
