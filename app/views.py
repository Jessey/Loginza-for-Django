# -*- coding: utf-8 -*-

from django.core.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import render_to_response


from Test.loginza.loginza import *
from Test.loginza.loginza_userprofile import *

def index(request):
    c = {}
    c.update(csrf(request))

    is_error = False
    lgnz = LoginzaAPI()
   
    try: 
        if request.POST.get('token'):
            user_prof = lgnz.getAuthInfo(request.POST.get('token'))
            request.session["is_auth"] = True
            request.session["profile"] = user_prof
        elif request.GET.get('quit'):
            del request.session["is_auth"]
            # Вышли
    except:
        is_error = True
        
    try: 
        if request.session["is_auth"]:
            usr_profile = LoginzaUserProfile(request.session["profile"])
    except:
        is_error = True
        
    return render_to_response('templates/index.html', locals(), context_instance=RequestContext(request))
