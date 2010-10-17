from django.core.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import render_to_response


from Test.loginza.loginza import *

def index(request):
    c = {}
    c.update(csrf(request))

    is_error = False
    lgnz = LoginzaAPI()
   
    try: 
        if request.POST.get('token'):
            user_prof = lgnz.getAuthInfo(request.POST.get('token'))
            cnst = lgnz.API_URL
    except:
        is_error = True
        
    return render_to_response('templates/index.html', locals(), context_instance=RequestContext(request))
    
def check(request):
    c = {}
    c.update(csrf(request))
        
    return HttpResponse('ololo')