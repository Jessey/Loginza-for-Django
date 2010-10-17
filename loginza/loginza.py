# -*- coding: utf-8 -*-

from django.http import HttpResponse
import urllib2

class LoginzaAPI():
    VERSION = '1.0'
    API_URL = 'http://loginza.ru/api/'
    WIDGET_URL = 'https://loginza.ru/api/widget'
    
    def getAuthInfo(self, token):
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
        url = self.API_URL + '?' + self.http_build_query(params)
        
        responce = urllib2.urlopen(url).read()
        
        
    
    
    def http_build_query(self, params, convention="%s"):
      """
    
        This was ripped shamelessly from a PHP forum and ported to Python:
    
          http://www.codingforums.com/showthread.php?t=72179
    
        Essentially, it's a (hopefully perfect) replica of PHP's
        http_build_query() that allows you to pass multi-dimensional arrays
        to a URL via POST or GET.
    
      """
    
      from urllib import quote
    
      if len(params) == 0:
        return ""
      else:
        output = ""
        for key in params.keys():
    
          if type(params[key]) is dict:
            output = output + self.http_build_query(params[key], convention % (key) + "[%s]")
    
          elif type(params[key]) is list:
    
            i = 0
            newparams = {}
            for element in params[key]:
              newparams[str(i)] = element
              i = i + 1
    
            output = output + self.http_build_query(newparams, convention % (key) + "[%s]")
    
          else:
            key = quote(key)
            val = quote(str(params[key]))
            output = output + convention % (key) + "=" + val + "&"
    
      return output