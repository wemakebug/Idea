from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response,render

@csrf_exempt
def index(req):
    return render_to_response('first/index.html')

@csrf_exempt
def user_label(req):
    if req.method == "GET":
        return render(req, 'second/Label_User.html')
    if req.method == "POST":
        pass

def user_project(req):
    if req.method == "GET":
        return render(req, 'second/Label-Project.html')
    if req.method == "POST":
        pass