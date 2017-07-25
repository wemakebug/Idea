# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from itertools import chain

from itertools import islice
from django.shortcuts import render,HttpResponse,Http404,render_to_response,HttpResponseRedirect

from admina.models import Creation2ProjectLabel, Creation, ProjectLabel, Comment, User, Praise, Follow
# Create your views here.
from idear.views import Check_User_Cookie

from django.shortcuts import get_object_or_404

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def creations(req):
    '''
    创意灵感一级二级页面项目显示
    '''
    projectLabels = ProjectLabel.objects.all()
    creations = Creation.objects.all()
    praises = Praise.objects.all()
    follows = Follow.objects.all()
    userId = int(req.COOKIES.get('user'))

    # try:
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
        return render_to_response('creation/index.html',{'creations':creations,'projectLabels':projectLabels,'userId':userId,'follows':follows,'praises':praises})

    else:
        id = req.POST['creationId']
        creation = get_object_or_404(Creation,pk = id)
        comments = Comment.objects.fitler(creation = id).order_by('Date')
        user = creation.user
        return render_to_response('creations/sec_creations.html',{'creation':creation,'comments':comments,'user':user})
    # except:
    #      return HttpResponse("<script type='text/javascript'>alert('数据有异常，请稍后再试')</script>")


@csrf_exempt
def star(req):
    '''
    点赞
    1为创意
    2为项目

    status
    状态值：0为失败，1为成功
    '''
    status = 0
    try:
        Id = req.POST["Id"]
        userId = req.POST["userId"]
        starType = int(req.POST["starType"])
        if starType == 1:
            p = Praise.objects.get_or_create(creation_id = Id, user_id = userId)
            status = 1
            return HttpResponse(status)
        else:
            p = Praise.objects.get_or_create(project_id = Id, user_id = userId)
            status = 1
            return HttpResponse(status)
    except:
        return HttpResponse(status)
    


@csrf_exempt
def attend(req):
    '''
    Id的关注类型
    1为被关注创意
    2为被关注项目
    3为被关注用户

 
    status
    状态值：0为失败，1为成功
    '''
    status = 0
    try:
        Id = req.POST['Id']
        userId = req.POST['userId']
        attendType = int(req.POST['attendType'])
        if attendType == 1:
            p = Follow.objects.get_or_create(creation_id = Id, user_id = userId)
            status = 1
            return HttpResponse(status)
        elif attendType == 2:
            p = Follow.objects.get_or_create(project_id = Id, user_id = userId)
            status = 1
            return HttpResponse(status)
        elif attendType == 3:
            F = Follow.objects.get_or_create(Follower_id = Id, user_id = userId)
            status = 1
            return HttpResponse(status)
    except:
        return HttpResponse(status)



