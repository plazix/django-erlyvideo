# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError

from djerlyvideo.conf import settings #as ev_settings


class Command(BaseCommand):
    def handle(self, *args, **options):
        pass
