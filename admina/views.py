# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,Http404

# Create your views here.

def login(req):
    if req.method == "GET":
        return render(req, 'login.html')
    if req.method == "POST":
        pass