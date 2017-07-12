# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,Http404

# Create your views here.

def login(req):
    if req.method == "GET":
        return render(req, 'login.html')
    if req.method == "POST":
        userName = ''
        loginStatue = 0
        try:
            username = req.POST["username"]
            password = req.POST["password"]
        except:
            loginStatue = 3
            result = {
                'loginStatue': loginStatue,
                'username': userName
            }
            HttpResponse(result)
