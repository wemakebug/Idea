# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render,HttpResponse,Http404,render_to_response,HttpResponseRedirect
from django.db.models import Q
from admina import models
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
import uuid
import re,base64
from idear.Idea_util.ImgVerification import generate_verify_image
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


'''
登陆验证函数，如需登陆，调此函数即可，仍需调试
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
            user = models.User.objects.get(Email=user_cookie)
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
        return render_to_response('idea/index.html')
    if req.method == "POST":
        pass

@csrf_exempt
def login(req):
    '''
    登陆界面的处理
    :param req: 
    :return: 
    '''
    if req.method == "GET":
        return render_to_response('idea/login.html')
    if req.method == "POST":
        result = {}
        result['status'] = None
        result['message'] = ''
        result['username'] = None
        result['UUID'] = None
        email = req.POST['email']
        password = req.POST['password']
        if models.User.objects.filter(Q(Email=email)):
            user = models.User.objects.get(Email=email)
            if user.PassWord == password:
                user.Uuid = uuid.uuid1()
                result['status'] = 1
                result['username'] = user.UserName
                req.session['uuid'] = user.Uuid
                result['message'] = '登陆成功'
                return HttpResponse(json.dumps(result))
            elif user.PassWord != password:
                result['status'] = 0
                result['message'] = '用户名或密码错误'
                return HttpResponse(json.dumps(result))
        else:
            result['status'] = 0
            result['message'] = '用户名或密码错误'
            return HttpResponse(json.dumps(result))



def varidate_char(str, max_length=20):
    '''
    非法字符验证
    :param sql: 
    :param max_length: 
    :return: False  表示字符串中含有非法字符    True 表示字符串中不含有非法字符
    '''
    if len(str) > max_length:
        return False
    dirty_stuff = ["\"", "\\", "/", "*", "'", "=", "-", "#", ";", "<", ">", "+", "%", "$", "(", ")", "%", "@","!"]
    for char in str:
        if char in dirty_stuff:
            return False
    return True

def varidate_emial(str,max_length=20):
    if len(str) > max_length:
        return False
    if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", str) != None:
        return True
    else:
        return False

@csrf_exempt
def regist(req):
    '''
    注册页面
    :param req: 
    :return: 在客户端留下username 和 email 的cookie 以及uuid session
    '''
    if req.method == 'GET':
        return render_to_response('idea/regist.html')
    if req.method == "POST":
        result = {
            'message': None,
            'status': 0,
            'username': None,
            'account': None,
            'uuid': None
        }
        username = req.POST['UserName']
        email = req.POST['Email']
        password = req.POST['Passwd']
        print('well')
        if not (varidate_char(username) and varidate_emial(email)):
            result['message'] = '输入非法字符'
            result['status'] = 0
            return HttpResponse(json.dumps(result))
        elif models.User.objects.filter(Email=email):
            result['status'] = 0
            result['message'] = '邮箱已经被注册'
            return HttpResponse(json.dumps(result))
        elif models.User.objects.filter(UserName=username):
            result['status'] = 0
            result['message'] = '姓名已被注册'
            return HttpResponse(json.dumps(result))
        else:
            try:
                models.User.objects.create(Email=email, UserName=username, PassWord=password, Uuid=uuid.uuid1())
                user = models.User.objects.get(Email=email)
                req.session['uuid'] = user.Uuid
                result['username'] = username
                result['account'] = email
                result['message'] = '注册成功，正在调转'
                result['status'] = 1
                return HttpResponse(json.dumps(result))
            except:
                result['status'] = 0
                result['message'] = '服务器异常'
                return HttpResponse(json.dumps(result))


def team(req):
    '''
    团队页面
    '''
    if req.method == 'GET':
        teams = models.User.objects.all().filter(Identity=2)

        return render_to_response('team/team.html', {'teams': teams})
    if req.method == 'POST':
        pass

def teamdetails(req):
    if req.method == 'GET':
            return render_to_response('team/teamdetails.html')
    if req.method == 'POST':
        pass

def teamhelpapplication(req):
    if req.method == 'GET':
        return render_to_response('team/teamhelpapplication.html')
    if req.method == 'POST':
        pass
# 忘记密码
def forgetPassword(req):
    if req.method == 'GET':
        stream, strs = generate_verify_image(save_img=False)
        stream = base64.b64encode(stream.getvalue()).encode('ascii')
        return render_to_response('idea/forgetPassword.html',{'img': stream})

'''
创意页面
'''
def creation(req):
    if req.method == 'GET':
        return render_to_response('creation/index.html')
    if req.method == "POST":
        pass
'''

招募项目详情
'''
def redetails(req):
    if req.method == 'GET':
        return render_to_response('project/redetails.html')
    if req.method == 'POST':
        pass
'''
招募项目申请表
'''

def apply(req):
    if req.method == 'GET':
        return render_to_response('project/apply.html')
    if req.method == 'POST':
        pass


''''
测试页面
'''
@csrf_exempt
def test(req,param):
    if req.method == "GET":
        print param
        teams = models.User.objects.all().filter(Identity=2)
        return render_to_response('team/test.html', {'teams': teams})
    if req.method == "POST":
        data = req.POST["data"]
        print data
        return HttpResponse(data)


