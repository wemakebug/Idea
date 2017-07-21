# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,Http404,render_to_response,HttpResponseRedirect

from admina.models import Project2ProjectLabel, Creation, ProjectLabel, Comment, User
# Create your views here.
from idear.views import Check_User_Cookie


def creations(req):
    '''
    创意灵感一级二级页面项目显示
    '''
    if req.method == 'GET':
        sign = req.GET['sign']
        if sign != "":
            Creation2ProjectLabelObj = Project2ProjectLabel.objects.get( projectLabel = sign)
            creations = Creation2ProjectLabelObj.Creation2ProjectLabel_Creation_set.all()
        else:
            creations = Creation.objects.all()
            projectLabels = ProjectLabel.objects.all()
        return render_to_response('creations/index.html',{'creations':creations,'projectLabels':projectLabels})
    else:
        id = req.POST['creationId']
        creations = Creation.objects.fitler(id = id)
        comments = Comment.objects.fitler(creation = id).order_by('Date')
        user = Creation.objects.get(id = id).user
        return render_to_response('creations/sec_creations.html',{'creations':creations,'comments':comments})

