# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from admina.models import Project,Project2ProjectLabel,ProjectUser
from django.shortcuts import HttpResponse,Http404,render_to_response,HttpResponseRedirect

from django.views.decorators.csrf import csrf_exempt

from itertools import chain

from itertools import islice
from django.shortcuts import render, HttpResponse, Http404, render_to_response, HttpResponseRedirect

from admina.models import Creation2ProjectLabel, Creation, ProjectLabel, Comment, User, Praise, Follow
# Create your views here.
from idear.views import Check_User_Cookie

from django.shortcuts import get_object_or_404

from django.views.decorators.csrf import csrf_exempt


# Create your views here.
'''
招募项目
'''
# @csrf_exempt
# def projects(req):
#     if req.method == "GET":
# 	    projects = Project.objects.all()
# 	    return render_to_response('project/recruit.html', {'projects': projects})
#     else:
# 	    projects = Project.objects.all()
# 	    return render_to_response('project/recruit.html', {'projects': projects})

@csrf_exempt
def projects(req):
	'''
    创意灵感一级二级页面项目显示
    '''
	projectLabels = ProjectLabel.objects.all()
	projects = Project.objects.all()
	try:
		if req.method == 'GET':
			sign = req.GET['sign']
		#  如果是所有项目
			if sign == "all":
				projects = projects
		#  如果有特殊标签
			else:
				ProjectLabelObjs = Project2ProjectLabel.objects.filter(projectLabel=sign)
				projects = Project.objects.filter(Img="null")
				for obj in ProjectLabelObjs:
					projects = chain(projects, Project.objects.filter(Id=int(obj.project.Id)))
			return render_to_response('project/recruit.html', {'projects': projects, 'projectLabels': projectLabels})

		else:
			id = req.POST['projectId']
			project = get_object_or_404(Project, pk=id)
			comments = Comment.objects.fitler(project=id).order_by('Date')
			user = project.user
			return render_to_response('project/recruit.html',
									  {'project': project, 'comments': comments, 'user': user})
	except:
		return HttpResponse("<script type='text/javascript'>alert('数据有异常，请稍后再试')</script>")


@csrf_exempt
def star(req):
	'''
    点赞
    1为创意
    2为项目

    status
    状态值：0为失败，1为成功
    '''
	status = 0
	try:
		Id = req.POST["Id"]
		userId = req.POST["userId"]
		starType = int(req.POST["starType"])
		if starType == 1:
			p = Praise.objects.get_or_create(creation_id=Id, user_id=userId)
			status = 1
			return HttpResponse(status)
		else:
			p = Praise.objects.get_or_create(project_id=Id, user_id=userId)
			status = 1
			return HttpResponse(status)
	except:
		return HttpResponse(status)


@csrf_exempt
def attend(req):
	'''
    Id的关注类型
    1为被关注创意
    2为被关注项目
    3为被关注用户


    status
    状态值：0为失败，1为成功
    '''
	status = 0
	# try:
	Id = req.POST['Id']
	userId = req.POST['userId']
	attendType = int(req.POST['attendType'])
	if attendType == 1:
		p = Follow.objects.create(creation_id=Id, user_id=userId)
		status = 1
		return HttpResponse(status)
	elif attendType == 2:
		p = Follow.objects.create(project_id=Id, user_id=userId)
		status = 1
		return HttpResponse(status)
	elif attendType == 3:
		F = Follow.objects.create(Follower_id=Id, user_id=userId)
		status = 1
		return HttpResponse(status)
	# except:
	#     return HttpResponse(status)




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


