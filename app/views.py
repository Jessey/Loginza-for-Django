from django.core.context_processors import csrf
from django.shortcuts import render_to_response

from Test.loginza.loginza import *

def index(request):
    return render_to_response('templates/index.html', locals())
    
def check(request):
    is_error = False
    lgnz = LoginzaAPI()
    
    try: 
        if request.META['token']:
            user_prof = lgnz.getAuthInfo(request.META['token'])
            cnst = lgnz.API_URL
    except:
        is_error = True
        
    return HttpResponse('ololo')