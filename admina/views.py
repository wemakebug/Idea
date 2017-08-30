# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_exempt
from admina import models
from models import User
import json
from django.core.paginator import Paginator
from django.shortcuts import render,HttpResponse,Http404,render_to_response,HttpResponseRedirect
import uuid

# Create your views here.


@csrf_exempt
def login(req):
    if req.method == "GET":
        if req.session.get('account') == None:
            return render(req, 'first/login.html')
        else:
            return render(req, 'first/index.html')
    if req.method == "POST":
        result = {
        }
        account = req.POST["account"].lower().strip()
        password = req.POST["password"]
        print "well"
        if models.Admin.objects.filter(Account=account):
            user = models.Admin.objects.get(Account=account)
            if user.Password == password:
                result['status'] = 1
                req.session['account'] = account
                result['account'] = account
                result['message'] = '登陆成功'
                return HttpResponse(json.dumps(result), content_type="application/json")
            elif user.Password != password:
                result['status'] = 0
                result['message'] = '用户名或密码错误'
                return HttpResponse(json.dumps(result), content_type="application/json")
        else:
            result['status'] = 0
            result['message'] = '用户名或密码错误'
            return HttpResponse(json.dumps(result), content_type="application/json")

def logout(req):
    '''
    注销
    :param req: 
    :return: login.html
    '''
    if req.method == "GET":
        del req.session['account']
        for cookie in req.COOKIES:
            del cookie
        return render(req, 'first/login.html')
    if req.method == "POST":
        pass


@csrf_exempt
def score_rank(req):
    if req.method == "GET":
        currentpage = 1
        scoreRank = models.Score.objects.all().order_by('Id')
        page = Paginator(scoreRank, 6)
        scoreRank = page.page(currentpage).object_list
        return render_to_response('second/Score_rank.html', {'ScoreRank': scoreRank})
    if req.method == "POST":
        pass

@csrf_exempt
def score_user(req):
    if req.method == "GET":
        currentpage = 1
        scoreUser = models.User.objects.all().order_by('Id')
        page = Paginator(scoreUser, 6)
        scoreUser = page.page(currentpage).object_list
        print scoreUser[1].Id
        return render_to_response('second/Score_user.html', {'ScoreUser': scoreUser})
    if req.method == "POST":
        pass


@csrf_exempt
def score_record(req):
    if req.method == "GET":
        currentpage = 1
        scoreChanges = models.ScoreChange.objects.all().order_by('Id')
        page = Paginator(scoreChanges, 6)
        scoreChanges = page.page(currentpage).object_list
        return render_to_response('second/Score_record.html', {'ScoreChanges': scoreChanges})
    if req.method == "POST":
        pass

@csrf_exempt
def UserManager(req):
    Users = models.User.objects.all().order_by('Id')
    UsersList = []
    for user in Users:
        OneUser = {}
        OneUser["UserName"] = user.UserName
        OneUser["Sex"] = user.Sex
        OneUser["RegistTime"] = str(user.RegistTime)
        OneUser["Score"] = user.Score
        UsersList.append(OneUser)
    return HttpResponse(json.dumps(UsersList))
