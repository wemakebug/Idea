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
        try:
            account = req.COOKIES.get('account')
            username = req.COOKIES.get('username')
            try:
                user = models.Admin.objects.get(Account=account)
                if user.UserName == username:
                    return render(req, 'first/index.html')
                else:
                    return render(req, 'first/login.html')
            except:
                return render(req, 'first/login.html')
        except:
            return render(req, 'first/login.html')
    if req.method == "POST":
        result = {
        }
        try:
            account = req.POST["account"]
            password = req.POST["password"]
            try:
                user = models.User.objects.get(Account=account)
                if user.Identity == 3 and user.PassWord == password:
                    result['username'] = user.UserName
                    result['account'] = user.Account
                    result['status'] = 1
                    return HttpResponse(json.dumps(result), content_type="application/json")
                elif user.Identity != 3 and user.PassWord == password:
                    result['status'] = 2
                    return HttpResponse(json.dumps(result), content_type="application/json")
                elif user.Identity == 3 and user.PassWord != password:
                    result['status'] = 3
                    return HttpResponse(json.dumps(result), content_type="application/json")
            except:
                result['status'] = 4
                return HttpResponse(json.dumps(result), content_type="application/json")
        except:
            result['status'] = 0
            return HttpResponse(json.dumps(result), content_type="application/json")
'''
退出登陆函数，删除相应的cookie并且跳转到指定页面
'''
def logout(req):
    if req.method == "GET":
        try:
            response = HttpResponseRedirect('login')
            response.delete_cookie('User')
            response.delete_cookie('UUID')
            response.delete_cookie('currentpage')
            return response
        except:
            return HttpResponseRedirect('index')

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
