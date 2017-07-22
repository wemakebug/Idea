# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from itertools import chain

from itertools import islice
from django.shortcuts import render,HttpResponse,Http404,render_to_response,HttpResponseRedirect

from admina.models import Creation2ProjectLabel, Creation, ProjectLabel, Comment, User, Praise
# Create your views here.
from idear.views import Check_User_Cookie


def creations(req):
    '''
    创意灵感一级二级页面项目显示
    '''
    projectLabels = ProjectLabel.objects.all()
    creations = Creation.objects.all()
    if req.method == 'GET':
        sign = req.GET['sign']
        #如果是所有项目
        if sign == "all":
            creations = creations
        #如果有特殊标签
        else:
            CreationLabelObjs = Creation2ProjectLabel.objects.filter( projectLabel = sign)
            creations = Creation.objects.filter(Img = "null")
            for obj in CreationLabelObjs:
                creations = chain(creations,Creation.objects.filter(Id = int(obj.creation.Id)))
        return render_to_response('creation/index.html',{'creations':creations,'projectLabels':projectLabels})
    else:
        id = req.POST['creationId']
        creations = Creation.objects.fitler(id = id)
        comments = Comment.objects.fitler(creation = id).order_by('Date')
        user = Creation.objects.get(id = id).user
        return render_to_response('creations/sec_creations.html',{'creations':creations,'comments':comments})
