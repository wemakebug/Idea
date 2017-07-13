# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from admina import models
import json
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
