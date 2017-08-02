from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response,render
from admina import models
from django.core.paginator import Paginator

@csrf_exempt
def index(req):
    return render_to_response('second/User_detail.html')

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


def index(req):
    if req.method == "GET":
        return render(req, 'include/Base.html')
    if req.method == "POST":
        pass

def user_detail(req):
    if req.method == "GET":
        return render(req, 'second/User_detail.html')

def util1(req):
    if req.method == "GET":
        return render(req, 'util/form_layout.html')

def util2(req):
    if req.method == "GET":
        return render(req, 'util/form_samples.html')

def util3(req):
    if req.method == "GET":
        return render(req, 'util/ui_modals.html')

def util4(req):
    if req.method == "GET":
        return render(req, 'util/table_editable.html')


