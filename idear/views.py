# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


'''
首页
'''
def index(req):
    if req.method == "GET":
        return render(req, 'index.html')
    if req.method == "POST":
        pass
'''
登陆页面
'''
def login(req):
    if req.method == "GET":
        return render(req, 'login.html')
    if req.method == "POST":
        pass
'''
注册页面
'''
def regist(req):
    if req.method == 'GET':
        return render(req, 'regist.html')
    if req.method == "POST":
        pass
'''
团队页面
'''
def team(req):
    if req.method == 'GET':
        return render(req, 'team.html')
    if req.method == 'POST':
        pass

def forgetPassword(req):
    if req.method == 'GET':
        return render(req, 'forgetPassword.html')
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