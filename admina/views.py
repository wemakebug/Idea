# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_exempt
from admina import models
from models import User
import json
from django.shortcuts import render,HttpResponse,Http404,render_to_response

# Create your views here.

@csrf_exempt
def login(req):
    if req.method == "GET":
        try:
            account = req.COOKIES.get('account')
            username = req.COOKIES.get('account')
            try:
                user = models.User.objects.get(Account=account)
                if user.UserName == username :
                    return render(req, 'index.html')
                else:
                    return render(req, 'login.html')
            except:
                return render(req, 'login.html')
        except:
            return render(req, 'login.html')
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
                    return HttpResponse(json.dumps(result),content_type="application/json")
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
@csrf_exempt
def index(req):
    return render_to_response('index.html')


@csrf_exempt
def UserManager(req):
    Users = models.User.objects.all()
    UsersList = []
    for user in Users:
        OneUser = {}
        OneUser["UserName"] = user.UserName
        OneUser["Sex"] = user.Sex
        OneUser["RegistTime"] = str(user.RegistTime)
        OneUser["Score"] = user.Score
        UsersList.append(OneUser)
    print UsersList
    return HttpResponse(json.dumps(UsersList))
