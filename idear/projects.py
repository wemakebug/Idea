# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from admina.models import Project,ProjectUser,User
from django.shortcuts import HttpResponse,Http404,render_to_response,HttpResponseRedirect

from django.views.decorators.csrf import csrf_exempt

# Create your views here.
'''
招募项目
'''
@csrf_exempt
def projects(req):
    if req.method == "GET":
	    projects = Project.objects.all()
        # projects.StartTime = datetime.strptime(projects.StartTime(),"%Y/%m/%d")
	    return render_to_response('project/recruit.html', {'projects': projects})
    else:
	    # return render_to_response('project/projects.html')
	    projects = Project.objects.all()
	    return render_to_response('project/recruit.html', {'projects': projects})


def get_projects(req):
    if req.method == "GET":
        return Http404()
    if req.method == "POST":
        projects = Project.objects.all().order_by('Id').filter()
        account = req.COOKIES.get('account')
        user = User.objects.filter(Account=account)
        if account:
            projects = ProjectUser.objects.get(user=user)
            return render_to_response('project/recruit.html', {'projects': projects})
        else:
            return render_to_response('project/recruit.html', {'projects': projects})


