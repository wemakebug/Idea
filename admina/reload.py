from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response,render
from admina import models
from django.core.paginator import Paginator

@csrf_exempt
def index(req):
    return render_to_response('first/index.html')

@csrf_exempt
def label_user(req):
    if req.method == "GET":
        currentpage = 1
        userlabel = models.UserLabel.objects.all().order_by('Id')
        page = Paginator(userlabel, 6)
        userLabel = page.page(currentpage).object_list
        print userLabel
        return render_to_response('second/Label_User.html', {'UserLabel': userLabel})
    if req.method == "POST":
        pass

def label_project(req):
    if req.method == "GET":
        currentpage = 1
        projectlabel = models.ProjectLabel.objects.all().order_by('Id')
        page = Paginator(projectlabel, 6)
        projectLabel = page.page(currentpage).object_list
        print projectLabel
        return render_to_response('second/Label_Project.html', {'ProjectLabel ': projectLabel})
    if req.method == "POST":
        pass
