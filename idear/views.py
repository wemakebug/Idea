# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(req):
    if req.method == "GET":
        return render(req, 'index.html')
    if req.method == "POST":
        pass