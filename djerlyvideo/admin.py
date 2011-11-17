# -*- coding: utf-8 -*-

from django.contrib import admin

from djerlyvideo.models import Server


class ServerAdmin(admin.ModelAdmin):
    list_display = ('name', 'host', 'group', 'admin_connections', 'last_success_ping', 'is_broken', 'is_active')
    list_filter = ('group')
    search_fields = ('name', 'host', 'group')

    fieldsets = (
        (None, {
            'fields': ('name', 'host', 'rtmp_port', 'group', 'is_active'),
        }),
        (u'Настройки', {
            'fields': ('max_connections', ),
        }),
        (u'API', {
            'fields': ('api_port', 'api_user', 'api_password'),
        }),
    )

admin.site.register(Server, ServerAdmin)