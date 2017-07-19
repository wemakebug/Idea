# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from admina.models import Project
from django.shortcuts import HttpResponse,Http404,render_to_response,HttpResponseRedirect

# Create your views here.

"""
项目
"""
def projects(req):
	if req.method == "GET":
		return render_to_response('project/projects.html')
		# projects = Project.objects.all()
		# return HttpResponse(projects)
