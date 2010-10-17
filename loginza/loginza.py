# -*- coding: utf-8 -*-

from django.http import HttpResponse
import urllib2
import simplejson

class LoginzaAPI():
    VERSION = '1.0'
    API_URL = 'http://loginza.ru/api/'
    WIDGET_URL = 'https://loginza.ru/api/widget'
    
    def getAuthInfo(self, token):
        tkn = token
        return self.apiRequert('authinfo', token)
    
    def getWidgetUrl (self, return_url='', provider='', overlay=''):
        params = []
        
        if not return_url:
            params['token_url'] = self.currentUrl()
        else:
            params['token_url'] = return_url;
            
        if provider != '':
            params['provider'] = provider
            
        if overlay:
            params['overlay'] = overlay
            
        return self.WIDGET_URL + '?' + self.http_build_query(params)
        
    def currentUrl(self, request):
        url = []
        if request.META['HTTPS'] and request.META['HTTPS'] == 'on':
            url['sheme'] = "https"
            url['port'] = '443'
        else:
            url['sheme'] = 'http'
            url['port'] = '80'
        
        url['host'] = request.META['HTTP_HOST']
        
        if request.META['REQUEST_URI']:
            url['request'] = request.META['REQUEST_URI']
        else:
            url['request'] = request.META['SCRIPT_NAME'] + request.META['PATH_INFO']
            query = request.META['QUERY_STRING']
            if query:
                url['request'] += '?' + query
        return url['sheme'] + '://' + url['host'] + url['request']
        
    def apiRequert(self, method, params):
        url = self.API_URL + method + '?token=' + params
        return simplejson.loads(urllib2.urlopen(url).read())
