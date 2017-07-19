# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from admina.models import Creation

from django.shortcuts import render,HttpResponse,Http404,render_to_response,HttpResponseRedirect

# Create your views here.


'''
创意灵感一级界面
'''
def creations(req):
    if req.method == 'GET':
        creations = Creation.objects.all()
        return HttpResponse(creations)   
    else:
        pass 
