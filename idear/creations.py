# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from admina import models
from django.shortcuts import render,HttpResponse,Http404,render_to_response,HttpResponseRedirect

# Create your views here.
from idear.views import Check_User_Cookie

'''
获取表中全部Creation对象
'''
def Get_creation(req):
     if True:    #
        try:
            creations = models.Creation.objects.all().order_by('Id')
            for creation in creations:
                userName = creation.user.UserName
                userimg = creation.user.Img
                description = creation.Describe

            return HttpResponse('Well')
        except:
            return HttpResponse('Bad')
