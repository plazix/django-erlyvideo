# -*- coding: utf-8 -*-

from urllib2 import build_opener, HTTPBasicAuthHandler

from django.utils import simplejson


class ServerApi(object):
    API_STREAMS_URI = '/erlyvideo/api/streams/'
    API_STREAM_URI = '/erlyvideo/api/stream/%s/'
    API_STREAM_HEALTH_URI = '/erlyvideo/api/stream_health/%s/' # true, {"error":"unknown"}

    __opener = None

    def __init__(self, host, port=8082, user='', password=''):
        if user and password:
            auth = HTTPBasicAuthHandler()
            auth.add_password('Django', '%s:%s' % (host, port), user, password)
            self.__opener(auth)
        else:
            self.__opener = build_opener()

    def __request(self, url):
        data = self.__opener(url)
        data = ''.join(data)
        return simplejson.loads(data)

    def get_filelist(self):
        # todo написать
        pass

    def get_streams(self):
        data = self.__request(self.API_STREAMS_URI)
        return data['streams']

    def get_stream_health(self, name):
        # todo написать
        pass

    def get_stream(self, name):
        data = self.__request(self.API_STREAM_URI % name)
        return data['stream']

    def get_licenses(self):
        # todo написать
        pass


"""
{"streams":[{"client_count":0,"created_at":1318939915,"host":"default","last_dts":1865,"last_dts_at":1318939917,"name":"test_1","registrator":true,"ts_delay":1629,"type":"live","url":"test_1"}]}


{"stream":{"last_dts_at":1318939943,"ts_delay":12,"url":"test_1","type":"live","client_count":0,"clients":[],"created_at":1318939915,"host":"default","last_dts":28162,"last_dts_at":[1318,939943,294754],"name":"test_1","registrator":true,"type":"live","url":"test_1"}}
"""