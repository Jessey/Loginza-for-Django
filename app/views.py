from django.shortcuts import render_to_response

from Test.loginza.loginza import *

def view(request):
 
    render_to_response('templates/index.html', locals)
    
def check(request):
    is_error = False
    lgnz = LoginzaAPI()
    
    try: 
        if request.META['token']:
            user_prof = lgnz.getAuthInfo(request.META['token'])
    except:
        is_error = True
        
    return HttpResponse('ololo')