# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from admina.models import Creation
from django.shortcuts import render,HttpResponse,Http404,render_to_response,HttpResponseRedirect

# Create your views here.


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
def login(req):
    if req.method == "GET":
        return render(req, 'idea/login.html')
    if req.method == "POST":
        pass
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
        return render(req, 'idea/team.html')
    if req.method == 'POST':
        pass

'''
创意页面
'''
def creation(req):
    if req.method == 'GET':
        return render(req, 'creation/index.html')
    if req.method == "POST":
        pass

# 忘记密码
def forgetPassword(req):
    if req.method == 'GET':
        return render(req, 'idea/forgetPassword.html')
'''
招募项目
'''
def recruit(req):
    if req.method == 'GET':
        return render(req, 'project/recruit.html')
    if req.method == 'POST':
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
招募项目详情
'''

def apply(req):
    if req.method == 'GET':
        return render(req, 'project/apply.html')
    if req.method == 'POST':
        pass



  

