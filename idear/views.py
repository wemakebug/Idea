# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render,HttpResponse,Http404,render_to_response,HttpResponseRedirect
from admina import models
from admina.models import Project
import uuid
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


'''
登陆验证函数，如需登陆，调此函数即可
@:return 状态值，可通过为true
@:COOKIE name = User_acconunt
@:COOKIE name = UUID
'''
@csrf_exempt
def Check_User_Cookie(req):
    loginStatus = False
    try:
        user_cookie = req.COOKIES["account"]
        user_uuid_code = req.COOKIES["uuid"]
        try:
            user = models.User.objects.get(Account=user_cookie)
            if user_uuid_code == user_uuid_code:
                loginStatus = True
                return loginStatus
        except:
            return loginStatus
    except:
        return loginStatus

'''
首页
'''
def index(req):
    if req.method == "GET":
        return render(req, 'idea/index.html')
    if req.method == "POST":
        pass
'''
登陆页面
'''
@csrf_exempt
def login(req):
    if req.method == "GET":
        return render(req, 'idea/login.html')
    if req.method == "POST":
        result = {}
        result['status'] = None
        result['message'] = ''
        result['username'] = None
        result['UUID'] = None
        try:
            account = req.POST['account']
            password = req.POST['password']
            try:
                user = models.User.objects.get(Account=account)
                user.Uuid = uuid.uuid1()
                if user.PassWord == password:
                    result['status'] = 1
                    result['username'] = user.UserName
                    result['UUID'] = user.Uuid
                    result['message'] = '登陆成功'
                    return HttpResponse(json.dumps(result))
                elif user.PassWord != password:
                    result['status'] = 0
                    result['message'] = '用户名或密码错误'
                    return HttpResponse(json.dumps(result))
            except:
                result['status'] = 0
                result['message'] = '用户名或密码错误'
                return HttpResponse(json.dumps(result))
        except:
            result['status'] = 0
            result['message'] = '服务器数据获取异常'
            return HttpResponse(json.dumps(result))

'''
注册页面
'''
def regist(req):
    if req.method == 'GET':
        return render(req, 'idea/regist.html')
    if req.method == "POST":
        pass

'''
团队页面
'''
def team(req):
    if req.method == 'GET':
        return render(req, 'team/team.html')
    if req.method == 'POST':
        pass

def teamdetails(req):
    if req.method == 'GET':
        return render(req, 'team/teamdetails.html')
    if req.method == 'POST':
        pass

# 忘记密码
def forgetPassword(req):
    if req.method == 'GET':
        return render(req, 'idea/forgetPassword.html')

'''
创意页面
'''
def creation(req):
    if req.method == 'GET':
        return render(req, 'creation/index.html')
    if req.method == "POST":
        pass
'''

招募项目详情
'''
def redetails(req):
    if req.method == 'GET':
        return render(req, 'project/redetails.html')
    if req.method == 'POST':
        pass
'''
招募项目申请表
'''

def apply(req):
    if req.method == 'GET':
        return render(req, 'project/apply.html')
    if req.method == 'POST':
        pass



  

'''
招募项目
'''
@csrf_exempt
def projects(req):
    if req.method == "GET":
	    projects = Project.objects.all()
	    return render_to_response('project/recruit.html', {'projects': projects})
    else:
	    # return render_to_response('project/projects.html')
	    projects = Project.objects.all()
	    return render_to_response('project/recruit.html', {'projects': projects})



