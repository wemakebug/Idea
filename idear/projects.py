# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from admina.models import Project
from django.shortcuts import HttpResponse,Http404,render_to_response,HttpResponseRedirect

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

"""
项目
"""
# @csrf_exempt
# def projects1(req):
# 	if req.method == "GET":
# 		projects = Project.objects.all()
# 		print projects
# 		return render_to_response('project/recruit.html',{'projects':projects})
# 	else:
# 		# return render_to_response('project/projects.html')
# 		projects = Project.objects.all()
# 		return render_to_response('project/recruit.html',{'projects':projects})

# @csrf_exempt
# def projects2(req):
# 		if req.method == "GET":
# 			projects = Project.objects.all()
# 			return render_to_response('project/apply.html', {'projects': projects})
# 		else:
# 			# return render_to_response('project/projects.html')
# 			projects = Project.objects.all()
# 			return render_to_response('project/apply.html', {'projects': projects})
#

@csrf_exempt
def projects(req):
		if req.method == "GET":
			projects = Project.objects.all()
			print projects
			return render_to_response('project/recruit.html', {'projects': projects})
		else:
			# return render_to_response('project/projects.html')
			projects = Project.objects.all()
			return render_to_response('project/recruit.html', {'projects': projects})

