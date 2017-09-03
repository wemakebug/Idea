# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_exempt
from admina import models
import json
from django.shortcuts import render,HttpResponse,Http404,render_to_response,HttpResponseRedirect
import uuid
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.

def loginCheck(req):
    '''
    登陆状态验证
    :param req: 
    :return: 验证失败直接调转登陆界面，成功则继续执行
    '''
    if req.session.get('account') == None:
        return render(req, 'first/login.html')
    else:
        pass

@csrf_exempt
def login(req):
    if req.method == "GET":
        if req.session.get('account') == None:
            return render_to_response('first/login.html')
        else:
            return render_to_response('second/User_detail.html')
    if req.method == "POST":
        result = {
        }
        account = req.POST["account"].lower().strip()
        password = req.POST["password"]

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
        if req.session.get('account') == None:
            pass
        else:
            del req.session['account']
        response = render_to_response('first/login.html')
        if req.COOKIES.get('account'):
            response.delete_cookie('account')
        else:
            pass
        return render_to_response('first/login.html')
    if req.method == "POST":
        pass

@csrf_exempt
def score_rank(req):
    if req.method == "GET":
        currentpage = 1
        dataperpage = 6
        scoreRank = models.Score.objects.all().order_by('Id')
        page = Paginator(scoreRank, dataperpage)
        scoreRank = page.page(currentpage).object_list
        return render_to_response('second/Score_rank.html', {'ScoreRank': scoreRank})
    if req.method == "POST":
        pass

@csrf_exempt
def score_user(req, page):
    if req.method == "GET":
        currentpage = int(page)
        try:
            record_per_page = int(req.COOKIES.get('record_per_page'))
        except:
            record_per_page = 6
        scoreUser = models.User.objects.all().order_by('Id')
        scoreUser_count = models.User.objects.count()
        page = Paginator(scoreUser, record_per_page)
        scoreUser = page.page(currentpage).object_list
        return render_to_response('second/User_score.html', {'ScoreUser': scoreUser, 'count': scoreUser_count})
    if req.method == "POST":
        result = {}
        try:
            id = req.POST['id']
            confirmed = req.POST['confirm']
            if confirmed:
                try:
                    user = models.User.objects.get(Id=id)
                    user.delete()
                except:
                    result['message'] = '用户不存在'
                    result["status"] = 0
                    return HttpResponse(json.dumps(result))
        except:
            result['message'] = '服务器异常'
            result["status"] = 0
            return HttpResponse(json.dumps(result))


@csrf_exempt
def score_record(req):
    if req.method == "GET":
        currentpage = 1
        scoreChanges = models.ScoreChange.objects.all().order_by('Id')
        page = Paginator(scoreChanges, 6)
        scoreChanges = page.page(currentpage).object_list
        return render_to_response('second/Score_record.html', {'ScoreChanges': scoreChanges})
    if req.method == "POST":
        result = {}
        try:
            id = req.POST['id']
            confirmed = req.POST['confirm']
            if confirmed:
                try:
                    user = models.User.objects.get(Id=id)
                    user.delete()
                except:
                    result['message'] = '用户不存在'
                    result["status"] = 0
                    return HttpResponse(json.dumps(result))
        except:
            result['message'] = '服务器异常'
            result["status"] = 0
            return HttpResponse(json.dumps(result))


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
