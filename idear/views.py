# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render,HttpResponse,Http404,render_to_response,HttpResponseRedirect
from admina import models
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
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
        user_cookie = req.COOKIES["email"]
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
            email = req.POST['email']
            password = req.POST['password']
            try:
                user = models.User.objects.get(Email=email)
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
@csrf_exempt
def regist(req):
    if req.method == 'GET':
        return render(req, 'idea/regist.html')
    if req.method == "POST":
        result = {}
        username = req.POST['name']
        email = req.POST['email']
        password = req.POST['password']
        if models.User.objects.filter(Email=email):
            result['status'] = 0
            result['message'] = '邮箱已经被注册'
            print '邮箱已经被注册'
            return HttpResponse(json.dumps(result))

        elif models.User.objects.filter(UserName=username):
            result['status'] = 0
            result['message'] = '姓名已被注册'
            print '姓名已被注册'
            return HttpResponse(json.dumps(result))
        else:
            try:
                models.User.objects.create(Email=email, UserName=username, PassWord=password, Uuid=uuid.uuid1())
                user = models.User.objects.get(Email=email)
                result['username'] = username
                result['UUID'] = str(user.Uuid)
                result['message'] = '注册成功，正在调转'
                result['status'] = 1
                print '注册成功，正在调转'
                return HttpResponse(json.dumps(result))
            except:
                result = {
                    "message": '服务器状态异常',
                    "status": 0
                }
                return HttpResponse(json.dumps(result))

'''
团队页面
'''
def team(req):
    if req.method == 'GET':
        teams = models.User.objects.all().filter(Identity=2)
        return render_to_response('team/team.html', {'teams': teams})
    if req.method == 'POST':
        pass

def teamdetails(req):
    if req.method == 'GET':
        return render(req, 'team/teamdetails.html')
    if req.method == 'POST':
        pass

def teamhelpapplication(req):
    if req.method == 'GET':
        return render(req, 'team/teamhelpapplication.html')
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



def test(req):
    if req.method == "GET":
        teams = models.User.objects.all().filter(Identity=2)
        return render_to_response('team/test.html', {'teams': teams})


