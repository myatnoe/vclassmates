from django.http import HttpResponse
from django.utils import simplejson as json
from utils import get_name_pairs, get_raw_html

def index(request):
    return HttpResponse("Welcome to the backend")

def get_classmates(request):
    sid = request.GET.get('sid', '91178')
    password = request.GET.get('password', 'puvGQf92')

    url = "http://leo3.rp.edu.sg/classman/class/class_roster.asp?courseid={3F90B8C8-46F4-498C-8646-716E82BD7275}&classcode=C316-2-E64C-C"

    name_pairs = get_name_pairs(sid, password, url)
    return HttpResponse(json.dumps(name_pairs), mimetype='application/json')
    

    
     

