from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response

@csrf_exempt
def index(req):
    return render_to_response('first/index.html')
