# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from itertools import chain
import json
import time
import time

import uuid
from .Idea_util.varidate import user_must_login
from itertools import chain
import re

from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, HttpResponse, render_to_response, get_object_or_404, Http404
from django.db.models import Q
from datetime import datetime

from .Idea_util.getUserImg import decode_img
from .Idea_util.varidate import remove_script
from admina import models

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils.html import escapejs,strip_tags
from django.views.decorators.http import require_http_methods

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from .Idea_util.ImgVerification import generate_verify_image
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

''' 页面统一功能视图'''
def index(req):
    '''
    返回首页页面
    :param req:
    :return:
    '''
    if req.method == "GET":
        array = []
        array2 = []
        arrayFive = []
        proFive = []
        projects = models.Project.objects.filter(Q(Statue=1)|Q(Statue=2)|Q(Statue=3)|Q(Statue=4))
        users = models.ProjectUser.objects.all()
        for user in users:
            print user.project.Id,user.project.ProjectName
        label = models.Project2ProjectLabel.objects.all()
        creations = models.Creation.objects.filter(IsUse=1)
        for creation in creations:
            result = {}
            creacount = models.Praise.objects.filter(creation=creation).count()
            result[0] = creation
            result[1] = creacount
            array.append(result)
        array = sorted(array, key=lambda array: array[1],reverse=True)
        creationArray = array[0:5]
        for c in creationArray:
            arrayFive.append(c[0])
        for project in projects:
            res = {}
            procount = models.Praise.objects.filter(project=project).count()
            res[0] = project
            res[1] = procount
            array2.append(res)
        array2 = sorted(array2, key=lambda array2: array2[1],reverse=True)
        proBest = array2[0][0]
        proTwo = array2[1][0]
        print proTwo.Id,proTwo.ProjectName
        projectArray = array2[2:10]
        for p in projectArray:
            proFive.append(p[0])
        return render_to_response('idea/index.html',{"projects": projects,"labels":label,"proBest":proBest,
                                                     "proTwo":proTwo,"creationArray":arrayFive,"proArray":proFive,"users":users})
    if req.method == "POST":
        pass

# 权限管理
@require_http_methods(["GET", "POST"])
@csrf_exempt
def login(req):
    '''
    登陆界面的处理
    :param req:
    :return: 
    '''
    if req.method == 'GET':
        return render(req, 'idea/login.html')
    else:
        resData = {
            'status': 0,
            'message': ''
        }
        try:
            user_email = req.POST['email']
            passwd = str(req.POST['password'])
            user = models.User.objects.get(Email=user_email)
            user.Uuid = uuid.uuid4()  # 防止异地登陆
            if user.PassWord == passwd.strip():
                req.session['user_email'] = user_email
                req.session['user_uuid'] = str(user.Uuid)
                resData['status'] = 1
                resData['message'] = 'success'
            else:
                resData['message'] = '邮箱或密码错误'
        except Exception as e:
            print(e)
        response = HttpResponse(JsonResponse(resData))
        response.set_cookie('user_email', user_email)
        return response


@require_http_methods(["POST"])
@csrf_exempt
def get_user_img(req):
    '''
    动态获取用户图片
    :param req:
    :return:
    '''
    result = {
        'status': 0,
        'message': None,
        'img_path': None,
    }
    try:
        email = req.COOKIES.get('user_email')
    except:
        result['status'] = 0
        result['message'] = '尚未登陆'
        return HttpResponse(json.dumps(result))
    else:
        try:
            user = models.User.objects.get(Email=email)
        except Exception as e:
            print(e)
            result['status'] = 0
            result['message'] = '获取数据异常'
            return HttpResponse(json.dumps(result))
        else:
            try:
                result['status'] = 1
                result['message'] = '路径获取成功'
                img_path = user.Img.url
                result['img_path'] = img_path
            except Exception as e:
                print(e)
                result['status'] = 1
                result['message'] = '用户暂未上传图片'
                img_path = '/photos/photos/user/None.png'
                result['img_path'] = img_path
                return HttpResponse(json.dumps(result))
            else:
                return HttpResponse(json.dumps(result))


@require_http_methods(["POST"])
@csrf_exempt
def get_follow_count(req):
    '''
    动态获取关注数量
    :param req: 
    :return: 
    '''

    result = {
        'status': 0,
        'message': None,
        'userfollow': None,
    }
    try:
        email = req.COOKIES.get('user_email')
        user = models.User.objects.get(Email=email)
        userfollow = models.Follow.objects.filter(Q(user=user) & Q(Follower_id__isnull=False)).count()
        result['userfollow'] = userfollow
        result['status'] = 1
        result['message'] = '显示数量'
    except:
        result['status'] = 0
        result['message'] = '尚未登陆'
        return HttpResponse(json.dumps(result))
    else:
        return HttpResponse(json.dumps(result))


@require_http_methods(["POST"])
@csrf_exempt
def get_praise_count(req):
    '''
    动态获取点赞数量
    :param req: 
    :return: 
    '''

    result = {
        'status': 0,
        'message': None,
        'userpraise': None,
    }
    try:
        email = req.COOKIES.get('user_email')
        user = models.User.objects.get(Email=email)
        userpraise = models.Praise.objects.filter(user=user).count()
        result['userpraise'] = userpraise
        result['status'] = 1
        result['message'] = '显示数量'
    except:
        result['status'] = 0
        result['message'] = '尚未登陆'
        return HttpResponse(json.dumps(result))
    else:
        return HttpResponse(json.dumps(result))


@require_http_methods(["POST"])
@csrf_exempt
def get_user_name(req):
    '''
    动态获取用户名字
    :param req: 
    :return: 
    '''

    result = {
        'status': 0,
        'message': None,
        'username': None,
    }
    try:
        email = req.COOKIES.get('user_email')
        user = models.User.objects.get(Email=email)
        result['username'] = user.UserName
        result['status'] = 1
        result['message'] = '显示数量'
    except:
        result['status'] = 0
        result['message'] = '尚未登陆'
        return HttpResponse(json.dumps(result))
    else:
        return HttpResponse(json.dumps(result))





@require_http_methods(["GET", "POST"])
@csrf_exempt
def regist(req):
    '''
    注册页面发邮件
    :param req: 
    :return: 在客户端留下username 和 email 的cookie 以及uuid session
    '''
    if req.method == 'GET':
        return render_to_response('idea/regist.html')
    if req.method == "POST":
        result = {
            'message': None,
            'status': 0,
            'username': None,
            'email': None,
            'uuid': None
        }
        try:
            email = req.POST['Email']
            username = req.POST['UserName']
        except:
            result['status'] = 0
            result['message'] = '获取信息失败！'
            return HttpResponse(json.dumps(result))
        else:
            if models.User.objects.filter(Email=email):
                result['status'] = 1
                result['message'] = '邮箱已经被注册'
                return HttpResponse(json.dumps(result))
            elif models.User.objects.filter(UserName=username):
                result['status'] = 3
                result['message'] = '姓名已被注册'
                return HttpResponse(json.dumps(result))
            else:
                result['status'] = 2
                result['message'] ='邮箱已验证完成'
                img, code = generate_verify_image()
                req.session['generate_verify_image'] = code
                send_mail('欢迎注册WE创', '您的验证码是'+ str(code), '472303924@qq.com',
                          [email],  fail_silently=True)
                return HttpResponse(json.dumps(result))


@csrf_exempt
def inCode(req):
    '''
    注册页面判断验证码并注册
    :param req:
    :return:
    '''
    if req.method == 'GET':
        return render_to_response('idea/regist.html')
    if req.method == "POST":
        result = {
            'message': None,
            'status': 0,
            'username': None,
            'emial': None,
            'uuid': None
        }
        try:
            username = req.POST['UserName']
            email = req.POST['Email']
            password = req.POST['Passwd']
            incode = req.POST['incode']
            sessionCode = req.session['generate_verify_image']
        except:
            result['status'] = 0
            result['message'] = '获取信息失败'
            return HttpResponse(json.dumps(result))
        else:
            if models.User.objects.filter(Email=email):
                result['status'] = 1
                result['message'] = '邮箱已经被注册'
                return HttpResponse(json.dumps(result))
            elif models.User.objects.filter(UserName=username):
                result['status'] = 2
                result['message'] = '姓名已被注册'
                return HttpResponse(json.dumps(result))
            elif incode.lower() != sessionCode.lower():
                result['status'] = 3
                result['message'] = '验证码错误'
                return HttpResponse(json.dumps(result))
            else:
                try:
                    models.User.objects.create(Email=email, UserName=username, PassWord=password, Uuid=uuid.uuid4())
                    user = models.User.objects.get(Email=email)
                    user.Img = 'photos/2017/09/19/user/default_cdNstvn.jpg'
                    req.session['user_uuid'] = str(user.Uuid)
                    result['email'] = email
                    result['username'] = username
                    result['message'] = '注册成功，正在调转'
                    result['status'] =4

                    req.session['user_email'] = email
                    response = HttpResponse(json.dumps(result))
                    response.set_cookie('user_email', email)

                    return HttpResponse(json.dumps(result))
                except Exception as e:
                    print(e)
                    result['status'] = 0
                    result['message'] = '服务器异常!!'
                    return HttpResponse(json.dumps(result))


@csrf_exempt
@require_http_methods(["POST"])
def logout(req):
    '''
    注销界面
    :param req: 
    :return: 
    '''
    resData = {
        "status": 0,
        "message": ''
    }
    del req.session['user_email']
    del req.session['user_uuid']
    resData['status'] = 1
    resData['message'] = "已删除 session"
    # resData['message'] = "用户尚未登陆"
    response = HttpResponse(JsonResponse(resData))
    response.delete_cookie('user_email')
    return response



@csrf_exempt
def obtainVerify(req):
    """
    获取验证码
    :param req: 
    :return: 
    """
    sender = '472303924@qq.com'
    if req.method == 'POST':
        email = req.POST['email']
        img, verify_str = generate_verify_image()
        req.session['verify_str'] = verify_str
        send_mail('欢迎进入WE创', '您的验证码为' + verify_str , sender, [email], fail_silently=True)
        return render_to_response('idea/forgetPassword.html')


@csrf_exempt
def forgetPassword(req):
    '''
    忘记密码页面
    :param req: 
    :return: 
    '''
    if req.method == 'GET':
        return render_to_response('idea/forgetPassword.html')

    if req.method == 'POST':
        email = req.POST['email']
        newPassword = req.POST['newPassword']
        identifyingcode = req.POST['identifyingcode']
        verify_str = req.session['verify_str']
        if verify_str == identifyingcode:
            try:
                models.User.objects.filter(Email=email).update(PassWord=newPassword)
                data = 1        # 1: 重置密码成功
            except:
                data = -1       # -1: 重置密码失败
        else:
            data = -1
    return HttpResponse(data)


''' 功能页面相关视图结束'''

''' 团队页面相关视图'''


def team(req):
    '''
    团队页面
    :param req: 
    :return: 
    '''
    if req.method == 'GET':
        ''' 标签查询'''
        sign = req.GET['sign']
        if sign == "all":
            teams = models.User.objects.filter(Identity=2)
            User2UserLabel = models.User2UserLabel.objects.all()
            labels = models.UserLabel.objects.all()
            return render_to_response('team/team.html', {"teams": teams, "labels": labels,'User2UserLabel': User2UserLabel})
        elif int(sign):
            labels = models.UserLabel.objects.all()
            labels_0 = models.UserLabel.objects.filter(pk=sign)
            # user_2_userLable = models.User2UserLabel.objects.filter(Q(userLabel=labels) & Q(user__Identity=2))
            user_2_userLable = models.User2UserLabel.objects.filter(userLabel=labels_0).filter(user__Identity=2)
            User2UserLabel = models.User2UserLabel.objects.all()
            teams = []
            for obj in user_2_userLable:
                teams.append(obj.user)
            return render_to_response('team/team.html', {"teams": teams, "labels": labels, 'User2UserLabel': User2UserLabel})

    if req.method == 'POST':
        pass

@csrf_exempt
def teamdetails(req, teamid):
    '''
    团队详情页面 所有team 按照创建时间排序
    :param req: 
    :param teamid: 团队ID
    :return: 
    '''
    if req.method == 'GET':
        email = req.COOKIES.get('user_email')
        if email:
            try:
                this_team = models.User.objects.get(Q(pk=teamid) & Q(Identity=2))
                labels = models.User2UserLabel.objects.filter(Q(user__Id=teamid))
                counts = models.Follow.objects.filter(Follower=this_team).count()
                teamcounts = models.Praise.objects.filter(user_prised=this_team).count()
                comments = models.Comment.objects.filter(commited_user_id=teamid).order_by("-Date")
                user = models.User.objects.get(Email=email)
                comment_id = models.Comment.objects.filter(Q(commited_user_id=teamid) & Q(user=user))
                team_history_project = models.ProjectUser.objects.filter(Q(user__Id=teamid) & Q(project__Statue=4))
                team_project_label = models.Project2ProjectLabel.objects.all()
                commentlist = []

                for comment in comments:
                    if comment.commentedId is None:
                        newcomment = []
                        newcomment.append(comment)
                        commentlist.append(newcomment)

                for comlist in commentlist:
                    for comment in comments:
                        if str(comlist[0].Uuid)==str(comment.commentedId):
                            comlist.append(comment)

            except Exception as e:
                return Http404
            return render_to_response('team/teamdetails.html', {"team": this_team, "labels": labels, "counnt": counts, "comments": commentlist, "teamcounts": teamcounts, "id": comment_id, "user": user, "team_history_project": team_history_project, "team_project_label": team_project_label})
        else:
            try:
                this_team = models.User.objects.get(Q(pk=teamid) & Q(Identity=2))
                labels = models.User2UserLabel.objects.filter(Q(user__Id=teamid))
                counts = models.Follow.objects.filter(Follower=this_team).count()
                teamcounts = models.Praise.objects.filter(user_prised=this_team).count()
                comments = models.Comment.objects.filter(commited_user_id=teamid).order_by("-Date")
                # user = models.User.objects.get(Email=email)
                # comment_id = models.Comment.objects.filter(Q(commited_user_id=teamid) & Q(user=user))
                team_history_project = models.ProjectUser.objects.filter(Q(user__Id=teamid) & Q(project__Statue=4))
                team_project_label = models.Project2ProjectLabel.objects.all()
                commentlist = []

                for comment in comments:
                    if comment.commentedId is None:
                        newcomment = []
                        newcomment.append(comment)
                        commentlist.append(newcomment)

                for comlist in commentlist:
                    for comment in comments:
                        if str(comlist[0].Uuid) == str(comment.commentedId):
                            comlist.append(comment)

            except Exception as e:
                return Http404
            return render_to_response('team/teamdetails.html',
                                      {"team": this_team, "labels": labels, "counnt": counts, "comments": commentlist,
                                       "teamcounts": teamcounts, "team_history_project": team_history_project, "team_project_label": team_project_label})
    if req.method == 'POST':
        content = req.POST["string"]
        result = {
            "status": 0,
            "string": None
        }
        try:
            user_email = req.COOKIES.get('user_email')
            user = models.User.objects.get(Email=user_email)
            userteam = models.User.objects.get(Q(Id=teamid) & Q(Identity=2))
            result["status"] = 1
            result["string"] = "成功"
        except Exception as e:
            result["status"] = 0
            result["string"] = "空"
            return HttpResponse(json.dumps(result))
        else:
            models.Comment.objects.create(user=user, commited_user=userteam, Content=content, Uuid=uuid.uuid4())
            return HttpResponse(json.dumps(result))


@csrf_exempt
def teamcomment(req):
    if req.method == 'POST':
        reply_content = req.POST["strings"]
        teamid = req.POST["team_id"]
        commentid = req.POST["comment_id"]
        user_email = req.COOKIES.get('user_email')
        result = {
            'status': 0,
            'message': '',
        }
        try:
            user = models.User.objects.get(Email=user_email)
            userteam = models.User.objects.get(Q(Id=teamid) & Q(Identity=2))
            Comment1 = models.Comment.objects.filter(Id=commentid)
            result = {
                'status': 1,
                'message': 'success',
            }
        except Exception as e:
            print(e.message)
            result["status"] = 0
            result["string"] = "空"
            return HttpResponse(json.dumps(result))
        else:
            # print(locals())
            models.Comment.objects.create(user=user, commited_user=userteam, Content=reply_content, commentedId=Comment1[0].Uuid, Uuid=uuid.uuid4())
            return HttpResponse(json.dumps(result))


@csrf_exempt
def teamattend(req):
    '''
    团队详情的关注显示
    :param req: 
    :return: 
    '''
    if req.method == 'POST':
        type = int(req.POST['type'])
        if type == 2:
            try:
                team_mark = req.POST['team_mark']
                email = req.COOKIES.get('user_email')
                user = models.User.objects.get(Email=email)
                FollowUser = models.Follow.objects.filter(Follower_id=team_mark, user_id=user.Id)
                if len(FollowUser) > 0:
                    status = 2
                else:
                    status = 1
            except Exception as e:
                return HttpResponse('404')
            else:
                return HttpResponse(status)
        elif type == 1:
            try:
                team_mark = req.POST['team_mark']
                email = req.COOKIES.get('user_email')
                user = models.User.objects.get(Email=email)
                FollowUser = models.Praise.objects.filter(user_prised_id=team_mark, user_id=user.Id)
                if len(FollowUser) > 0:
                    status = 2
                else:
                    status = 1
            except Exception as e:
                return HttpResponse('404')
            else:
                return HttpResponse(status)
    if req.method == 'GET':
        pass


@csrf_exempt
def teamhelpapplication(req, teamhelpid=None):
    '''
    团队帮助申请
    :param req: 
    :param teamhelpid: 
    :return: 
    '''
    useremail = req.COOKIES.get('user_email')
    if req.method == 'GET':
        try:
            teamhelp = models.User.objects.get(Id=teamhelpid)

        except:
            return HttpResponse('404')
        else:
            users = models.User.objects.filter(Email=useremail)
            if int(teamhelp.Identity) == 2:
                return render_to_response('team/teamhelpapplication.html', {'teamhelp': teamhelp,'users':users})
            else:
                return HttpResponse('404')
    if req.method == 'POST':
        result = {
            'message': None,
            'status': 0,
            'users': None,
            'emial': None,
            'describe':None,
            'uuid': None
        }

        try:
            email = req.POST['user_email']
            describe = req.POST['sHTML']
            users = models.User.objects.filter(Email=email)[0]

        except:
            result['status'] = 0
            result['message'] = '获取信息失败'
            return HttpResponse(json.dumps(result))
        else:
            teamhelp = models.User.objects.get(Id=teamhelpid)
            models.HelpApplication.objects.create(Email=email, AppliedTeam=teamhelp, Applier=users, Describe=describe)
            result['status'] = 1
            result['message'] = '成功'
            return HttpResponse(json.dumps(result))



def service(req):
    '''
    服务页面
    :param req:
    :return:
    '''
    if req.method == 'GET':
        return render_to_response('idea/service.html')
    if req.method == "POST":
        pass


def ordinance(req):
    '''
    隐私条例页面详情
    :param req:
    :return:
    '''
    if req.method == 'GET':
        return render_to_response('idea/ordinance.html')
    if req.method == "POST":
        pass


''' 团队页面相关视图结束  '''

''' 创意灵感 页面相关部分开始'''


@csrf_exempt
def creations(req):
    '''
    创意灵感一级二级页面项目显示
    '''

    # userId = int(req.COOKIES.get('user'))
    userId = 3
    try:
        if req.method == 'GET':
            sign = req.GET['sign']
            # 如果是所有项目
            if sign == "all":
                creations = models.Creation.objects.filter(IsUse=True).order_by("-Date")
            # 如果有特殊标签
            else:
                CreationLabelObjs = models.Creation2ProjectLabel.objects.filter(projectLabel=sign)
                creations = []
                for obj in CreationLabelObjs:
                    creations.append(obj.creation)

            projectLabels = models.ProjectLabel.objects.all()
            praises = models.Praise.objects.all()
            follows = models.Follow.objects.all()
            return render_to_response('creation/index.html',
                                      {'creations': creations, 'projectLabels': projectLabels, 'userId': userId,
                                       'follows': follows, 'praises': praises, 'IsUse': True})
    except Exception as e:
        print(e)
        return HttpResponse("<script type='text/javascript'>alert('数据有异常，请稍后再试')</script>")


def crdetails(req):
    '''
    创意详情
    :param req: 
    :return: 
    '''
    if req.method == 'GET':
        creationId = req.GET['creationId']
        creation = models.Creation.objects.get(Id=creationId)
        labels = models.Creation2ProjectLabel.objects.filter(creation_id=creationId)
        comments = models.Comment.objects.filter(creation_id = creationId).order_by("-Date")
        commentlist = []
        for comment in comments:    #将所有的第一条回复添加进来 结果:[[head],[head]]
            if comment.commentedId is None:
                newcomment = []   
                newcomment.append(comment)
                commentlist.append(newcomment) #    [[head],[head],[head],[head]]

        for comlist in commentlist:    # 对每个列表循环  结果: [ [head,hui,hui],[head,hui,hui],[head] ]
            for comment in comments:
                if str(comlist[0].Uuid)==str(comment.commentedId):
                    comlist.append(comment)   
                       #   [[head,hui,hui],[head,hui,hui ],[head],[head]]

        alllables = []  # 找出本创意所有的标签
        for label in labels:
            alllables.append(label.projectLabel.Id)
        alllables = list(set(alllables))

        creation2crojectLabels = models.Creation2ProjectLabel.objects.filter(projectLabel_id__in = alllables)    #所有相关标签的 所有的 标签2项目
        return render_to_response('creation/crdetails.html',{"creation":creation,"comments":commentlist,"creation2crojectLabels":creation2crojectLabels[:2],"labels":labels[:3]})

    if req.method == "POST":
        pass


@csrf_exempt
def crcreate(req):
    '''
    创意灵感创建页面
    :param req:
    :return:
    '''
    if req.method == 'GET':
        obj = models.ProjectLabel.objects.all()
        user_email = req.COOKIES.get('user_email')
        username = models.User.objects.get(Email=user_email)
        return render_to_response('creation/crcreate.html', {"labels": obj,"username":username})
    if req.method == "POST":
        result = {
            'status': 0,
            'message': '',
        }
        name = req.POST["name"]
        img = req.POST["coverMap"]
        base64Code = img.split(',')[1]
        fileext = img.split(',')[0].split(';')[0].split('/')[1]
        Img = decode_img(base64Code, datetime.strftime(datetime.now(), "%Y-%m-%d=%H:%M:%S"), fileext)
        describe = req.POST["describe"]
        isUse = req.POST["isUse"]
        labels = req.POST["labels"].split("*")

        try:
            user_email = req.COOKIES.get('user_email')
            user = models.User.objects.get(Email=user_email)

            if isUse=="暂存":
                isUse = False
            else:
                isUse = True
            creation = models.Creation.objects.create(user=user, Name=name, Describe=describe,IsUse=isUse,Img=Img, Uuid=uuid.uuid4());
            creation.save()

            for label in labels[:-1]:
                Label = models.ProjectLabel.objects.get(ProjectLabelName=label)
                creation2ProjectLabel = models.Creation2ProjectLabel.objects.create(projectLabel=Label, creation=creation)
                creation2ProjectLabel.save()

            result = {
                'status': 1,
                'message': 'success',
            }
        except Exception as e :
            print(e)
            result['message'] = str(e)
        return HttpResponse(json.dumps(result))


@csrf_exempt
def crreport(req):
    '''
    创意举报
    :param req:
    :return:
    '''

    if req.method == 'GET':
        user_email = req.COOKIES.get('user_email')
        username = models.User.objects.get(Email=user_email)
        return HttpResponse("TRUE")
    if req.method == 'POST':
        result = {
            'status': 0,
            'message': '',
        }
        try:
            creationId = req.POST["creationId"]
            creation = models.Creation.objects.get(pk=creationId)
            reason = req.POST["reason"]
            user_email = req.COOKIES.get('user_email')
            user = models.User.objects.get(Email=user_email)
            models.Report.objects.create(user=user, creation=creation, Reason=reason)

            result = {
                'status': 1,
                'message': 'success',
            }
            return HttpResponse(json.dumps(result))
        except Exception as e:
            print(e)
            result['message'] = str(e)
            return HttpResponse(json.dumps(result))

@csrf_exempt
def rdcreport(req):
    '''
    创意评论举报
    :param req:
    :return:
    '''

    if req.method == 'GET':
        user_email = req.COOKIES.get('user_email')
        username = models.User.objects.get(Email=user_email)
        return HttpResponse("TRUE")
    if req.method == 'POST':
        result = {
            'status': 0,
            'message': '',
        }
        try:

            rdcreason = req.POST["rdcreason"]
            commentId = req.POST["commentId"]
            print(commentId)
            comment = models.Comment.objects.get(pk=commentId)
            user_email = req.COOKIES.get('user_email')
            user = models.User.objects.get(Email=user_email)
            models.Report.objects.create(user=user, comment=comment, Reason=rdcreason, Uuid=uuid.uuid4())

            result = {
                'status': 1,
                'message': 'success',
            }
            return HttpResponse(json.dumps(result))
        except Exception as e:
            print(e)
            result['message'] = str(e)
            return HttpResponse(json.dumps(result))


@csrf_exempt
def attend(req):
    '''
    Id的关注类型
    1为被关注创意
    2为被关注项目
    3为被关注用户

    status
    状态值：0为操作失败，1为关注成功，2 为取消关注成功
    '''
    status = 0
    try:
        Id = req.POST['Id']
        userId = req.POST['userId']
        attendType = int(req.POST['attendType'])

        if attendType == 1:
            FollowCreation = models.Follow.objects.filter(creation_id = Id, user_id = userId)
            if len(FollowCreation) > 0:
                FollowCreation.delete()
                status = 2
            else:
                models.Follow.objects.create(creation_id=Id, user_id=userId)
                status = 1

        elif attendType == 2:
            FollowProject = models.Follow.objects.filter(project_id = Id, user_id = userId)
            if len(FollowProject) > 0:
                FollowProject.delete()
                status = 2
            else:
                models.Follow.objects.create(project_id=Id, user_id=userId)
                status = 1

        elif attendType == 3:
            FollowUser = models.Follow.objects.filter(Follower_id = Id, user_id = userId)
            if len(FollowUser) > 0:
                FollowUser.delete()
                status = 2
            else:
                models.Follow.objects.create(Follower_id=Id, user_id=userId)
                status = 1
        return HttpResponse(status)
    except:
        return HttpResponse(status)


@csrf_exempt
def team_attend(req):
    '''
    团队详情关注
    :param req: 
    :return: 
    '''
    if req.method == 'POST':
        result = {
            'status': 0,
            'message': '',
        }
        try:
            email = req.COOKIES.get('user_email')
            team_mark = req.POST["team_mark"]
            user = models.User.objects.get(Email=email)
            userId = user.Id
            FollowUser = models.Follow.objects.filter(Follower_id=team_mark, user_id=userId)
            if len(FollowUser) > 0:
                FollowUser.delete()
                result["status"] = 2
                result["message"] = "删除记录"
            else:
                models.Follow.objects.create(Follower_id=team_mark, user_id=userId).save()
                result["status"] = 1
                result["message"] = "创建记录"
        except Exception as e:
            print(e.message)
            return HttpResponse(json.dumps(result))
        else:
            return HttpResponse(json.dumps(result))

@csrf_exempt
def team_star(req):
    '''
    团队详情的点赞
    :param req: 
    :return: 
    '''
    if req.method == 'POST':
        result = {
            'status': 0,
            'message': '',
        }
        try:
            email = req.COOKIES.get('user_email')
            team_mark = req.POST["team_mark"]
            user = models.User.objects.get(Email=email)
            userId = user.Id
            FollowUser = models.Praise.objects.filter(user_prised_id=team_mark, user_id=userId)
            if len(FollowUser) > 0:
                FollowUser.delete()
                result["status"] = 2
                result["message"] = "删除记录"
            else:
                models.Praise.objects.create(user_prised_id=team_mark, user_id=userId).save()
                result["status"] = 1
                result["message"] = "创建记录"
        except Exception as e:
            print(e.message)
            return HttpResponse(json.dumps(result))
        else:
            return HttpResponse(json.dumps(result))


@csrf_exempt
def star(req):
    '''
    点赞
    1为创意
    2为项目
    3为个人/团队

    status
    状态值：0为失败，1为成功， 2为取消点赞成功
    '''
    status = 0
    try:
        Id = req.POST["Id"]
        userId = req.POST["userId"]
        starType = int(req.POST["starType"])
        if starType == 1:    #如果是创意
            try:
                p = models.Praise.objects.get(creation_id=Id, user_id=userId).delete()    #尝试取消点赞
                status = 2
            except:
                p = models.Praise.objects.create(creation_id=Id, user_id=userId)
                status = 1
            return HttpResponse(status)
        elif starType ==2:
            try:
                p = models.Praise.objects.get(project_id=Id, user_id=userId).delete()
                status = 2
            except:
                p = models.Praise.objects.create(project_id=Id, user_id=userId)
                status = 1

            return HttpResponse(status)
        elif starType ==3:
            PraiseUser = models.Praise.objects.filter(user_prised_id=Id, user_id=userId)
            if len(PraiseUser) > 0:
                PraiseUser.delete()
                status = 2
            else:
                models.Praise.objects.create(user_prised_id=Id, user_id=userId)
                status = 1
            # try:
            #     PraiseUser = Praise.objects.get(user_prised_id=Id, user_id=userId).delete()
            #     status = 2
            # except:
            #     PraiseUser = Praise.objects.create(user_prised_id=Id, user_id=userId)
            #     status = 1
        return HttpResponse(status)
    except Exception as e:
        print(e)
        return HttpResponse(status)

@csrf_exempt
def comment(req):
    '''
    创意评论
    :param req:
    :return:
    '''
    if req.method =='GET':
        user_email = req.COOKIES.get('user_email')
        username = models.User.objects.get(Email=user_email)
        return HttpResponse("TRUE")
    if req.method =='POST':
        result = {
            'status': 0,
            'message': '',
        }
        try:
            user_email = req.COOKIES.get('user_email')
            user = models.User.objects.get(Email=user_email)
            creationId = req.POST["creationId"]
            creation = models.Creation.objects.get(pk = creationId)
            content = req.POST["content"]
            models.Comment.objects.create(user=user, creation=creation, Content=content, Uuid=uuid.uuid4())
            result = {
                'status': 1,
                'message': 'success',
            }

            return HttpResponse(json.dumps(result))


        except Exception as e:
            print(e)
            result['message'] = str(e)
            return HttpResponse(json.dumps(result))

@csrf_exempt
def rcomment(req):
    '''
    创意评论回复
    :param req:
    :return:
    '''
    if req.method =='GET':
        user_email = req.COOKIES.get('user_email')
        username = models.User.objects.get(Email=user_email)
        return HttpResponse("TRUE")
    if req.method =='POST':
        result = {
            'status': 0,
            'message': '',
        }
        try:
            user_email = req.COOKIES.get('user_email')
            user = models.User.objects.get(Email=user_email)
            creationId = req.POST["creationId"]
            creation = models.Creation.objects.get(pk = creationId)
            commentedId = req.POST["commentedId"]
            content = req.POST["content"]
            models.Comment.objects.create(user=user, creation=creation, Content=content, commentedId=commentedId, Uuid=uuid.uuid4())
            result = {
                'status': 1,
                'message': 'success',
            }

            return HttpResponse(json.dumps(result))


        except Exception as e:
            print(e)
            result['message'] = str(e)
            return HttpResponse(json.dumps(result))


''' 创意灵感 页面相关部分结束'''

''' 招募项目 相关页面开始'''


def apply(req):
    '''
    招募项目申请表
    '''
    if req.method == 'GET':
        return render_to_response('project/apply.html')
    if req.method == 'POST':
        pass


'''

提出建议页面详情
'''


def advice(req):
    if req.method == 'GET':
        return render_to_response('idea/advice.html')
    if req.method == "POST":
        pass


'''

招募项目详情
'''

def redetails(req):
    '''
        招募项目详情
        :param req:
        :return:
    '''
    if req.method == 'GET':
        projectId = req.GET['projectId']
        project = models.Project.objects.get(Id=projectId)
        user = models.ProjectUser.objects.get(project_id=projectId)
        labels = models.Project2ProjectLabel.objects.filter(project_id=projectId)
        comments = models.Comment.objects.filter(project_id=projectId).order_by("-Date")
        commentlist = []
        for comment in comments:
            if comment.commentedId is None:
                newcomment = []
                newcomment.append(comment)
                commentlist.append(newcomment)
        for comlist in commentlist:
            for comment in comments:
                if str(comlist[0].Uuid) == str(comment.commentedId):
                    comlist.append(comment)
        alllables = []  # 找出本项目所有的标签
        for label in labels:
            alllables.append(label.projectLabel.Id)
        alllables = list(set(alllables))
        project2projectLabel = models.Project2ProjectLabel.objects.filter(projectLabel_id__in=alllables)  # 所有相关标签的 所有标签2项目
        recruit = models.Recruit.objects.filter(project__Id=projectId)
        if recruit.exists():
            recruit = recruit[0]

        a = recruit.EndTime.strftime("%Y-%m-%d %H:%M:%S")
        timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
        timeStamp = int(time.mktime(timeArray))

        try:
            useremail = req.COOKIES.get('user_email')
            preuser = models.User.objects.get(Email=useremail)
            projectfollow = models.Follow.objects.filter(Q(project__Id=projectId)&Q(user=preuser))
            projectpraise = models.Praise.objects.filter(Q(project__Id=projectId) & Q(user=preuser))
            if projectfollow.count() is 0 :
                fstatus = 0
            else:
                fstatus = 1
            if projectpraise.count() is 0:
                pstatus = 0
            else:
                pstatus = 1

            return render_to_response('project/redetails.html',
                                  {"project": project, "project2projectLabels": project2projectLabel[:2],
                                   "labels": labels[:3], "user": user, "recruit": recruit, "EndTime": timeStamp,
                                    "fstatus":fstatus,"pstatus":pstatus, "comment": commentlist,"preuser":preuser })
        except:
            return render_to_response('project/redetails.html',{"project": project, "project2projectLabels": project2projectLabel[:2],
                                   "labels": labels[:3], "user":user, "recruit": recruit, "EndTime": timeStamp, "comment":commentlist,})


    if req.method == "POST":
         pass

@csrf_exempt
def prattendadd(req):
        '''
        项目关注增加
        :param req:
        :return:
        '''
        if req.method == 'POST':
            status = 0
            try:
                projectId = req.POST['projectId']
                project = models.Project.objects.get(Id=projectId)
                useremail = req.COOKIES.get('user_email')
                preuser = models.User.objects.get(Email=useremail)
                models.Follow.objects.create(user=preuser, project=project)
                status = 1
                return HttpResponse(status)

            except Exception as e:
                print(e)
                return HttpResponse(status)


@csrf_exempt
def prattenddelete(req):
        '''
        项目关注删除
        :param req:
        :return:
        '''
        if req.method == 'POST':
            status = 0
            try:
                projectId = req.POST['projectId']
                project = models.Project.objects.get(Id=projectId)
                useremail = req.COOKIES.get('user_email')
                preuser = models.User.objects.get(Email=useremail)
                models.Follow.objects.filter(user=preuser, project=project).delete()
                status = 1
                return HttpResponse(status)

            except Exception as e:
                print(e)
                return HttpResponse(status)

@csrf_exempt
def prpraiseadd(req):
        '''
        项目点赞增加
        :param req:
        :return:
        '''
        if req.method == 'POST':
            status = 0
            try:
                projectId = req.POST['projectId']
                project = models.Project.objects.get(Id=projectId)
                useremail = req.COOKIES.get('user_email')
                preuser = models.User.objects.get(Email=useremail)
                models.Praise.objects.create(user=preuser, project=project)
                status = 1
                return HttpResponse(status)

            except Exception as e:
                print(e)
                return HttpResponse(status)


@csrf_exempt
def prpraisedelete(req):
        '''
        项目点赞删除
        :param req:
        :return:
        '''
        if req.method == 'POST':
            status = 0
            try:
                projectId = req.POST['projectId']
                project = models.Project.objects.get(Id=projectId)
                useremail = req.COOKIES.get('user_email')
                preuser = models.User.objects.get(Email=useremail)
                models.Praise.objects.filter(user=preuser, project=project).delete()
                status = 1
                return HttpResponse(status)

            except Exception as e:
                print(e)
                return HttpResponse(status)


@csrf_exempt
def preport(req):
        '''
        项目举报
        :param req:
        :return:
        '''

        if req.method == 'GET':
            user_email = req.COOKIES.get('user_email')
            username = models.User.objects.get(Email=user_email)
            return HttpResponse("TRUE")
        if req.method == 'POST':
            result = {
                'status': 0,
                'message': '',
            }
            try:
                projectId = req.POST["projectId"]
                project = models.Project.objects.get(pk=projectId)
                reason = req.POST["reason"]
                user_email = req.COOKIES.get('user_email')
                user = models.User.objects.get(Email=user_email)
                models.Report.objects.create(user=user, project=project, Reason=reason)

                result = {
                    'status': 1,
                    'message': 'success',
                }
                return HttpResponse(json.dumps(result))
            except Exception as e:
                print(e)
                result['message'] = str(e)
                return HttpResponse(json.dumps(result))


@csrf_exempt
def pcreport(req):
        '''
        项目评论举报
        :param req:
        :return:
        '''

        if req.method == 'GET':
            user_email = req.COOKIES.get('user_email')
            username = models.User.objects.get(Email=user_email)
            return HttpResponse("TRUE")
        if req.method == 'POST':
            result = {
                'status': 0,
                'message': '',
            }
            try:
                commentId = req.POST["commentId"]
                comment = models.Comment.objects.get(pk=commentId)
                reason = req.POST["reason"]
                user_email = req.COOKIES.get('user_email')
                user = models.User.objects.get(Email=user_email)
                models.Report.objects.create(user=user, comment=comment, Reason=reason)

                result = {
                    'status': 1,
                    'message': 'success',
                }
                return HttpResponse(json.dumps(result))
            except Exception as e:
                print(e)
                result['message'] = str(e)
                return HttpResponse(json.dumps(result))

@csrf_exempt
def project_comment(req):
    '''
    项目评论
    :param req:
    :return:
    '''


    status = 0
    if req.method == 'POST':
        try:
            useremail = req.session.get('user_email')
            username = models.User.objects.get(Email=useremail)
            projectId = req.POST["projectId"]
            content = req.POST["content"]
            user = models.User.objects.get(UserName=username)
            project = models.Project.objects.get(pk=projectId)
            models.Comment.objects.create(user=user, project=project, Content=content)
            status = 1
            return HttpResponse(status)


        except Exception as e:
            print(e)
            return HttpResponse(status)

    if req.method == 'GET':


        return HttpResponse("TRUE")

@csrf_exempt
def prcomment(req):
    '''
    项目评论回复
    :param req:
    :return:
    '''
    if req.method =='GET':
        user_email = req.COOKIES.get('user_email')
        username = models.User.objects.get(Email=user_email)
        return HttpResponse("TRUE")
    if req.method =='POST':
        result = {
            'status': 0,
            'message': '',
        }
        try:
            user_email = req.COOKIES.get('user_email')
            user = models.User.objects.get(Email=user_email)
            projectId = req.POST["projectId"]
            print(projectId)
            project = models.Project.objects.get(pk = projectId)
            commentedId = req.POST["commentedId"]
            content = req.POST["content"]
            models.Comment.objects.create(user=user, project=project, Content=content, commentedId=commentedId, Uuid=uuid.uuid4())
            result = {
                'status': 1,
                'message': 'success',
            }

            return HttpResponse(json.dumps(result))


        except Exception as e:
            print(e)
            result['message'] = str(e)
            return HttpResponse(json.dumps(result))

@csrf_exempt
def recruit_apply(req):
    '''
       招募项目申请
    '''

    status = 0
    if req.method == 'POST':
        try:

            useremail = req.session.get('user_email')
            projectId = req.POST["projectId"]
            content = req.POST["describe"]
            remove_script(content)
            user = models.User.objects.get(Email=useremail)
            recruit = models.Recruit.objects.get(project=projectId)
            models.Apply.objects.create(user=user, recruit=recruit, Describe=content)
            status = 1
            return HttpResponse(status)
        except Exception as e:
            print(e.message)

        finally:
            return HttpResponse(status)




@csrf_exempt
def projects(req):
    '''
    项目一级页面显示
    '''
    try:
        if req.method == 'GET':
            sign = req.GET['sign']
            #  如果是所有项目
            if sign == "all":
                pprojects = models.Project.objects.filter(Q(Statue=1)|Q(Statue=2)|Q(Statue=3)|Q(Statue=4)).order_by('Id')
                array2 = []
                projects = []
                recruit = [1, 3]

                for project in pprojects:
                    res = {}
                    procount = models.Praise.objects.filter(project=project).count()
                    res[0] = project
                    res[1] = procount
                    array2.append(res)

                array2 = sorted(array2, key=lambda array2: array2[1], reverse=True)
                for p in array2:
                    projects.append(p[0])
                proBest = array2[0][0]
                return render_to_response('project/projects.html',
                                          {'projectLabels': models.ProjectLabel.objects.all(), "projects": projects,
                                           "recruit": recruit, "proBest": proBest})

            else:

                projects = []
                ProjectLabelObjs = models.Project2ProjectLabel.objects.filter(projectLabel=sign)
                for obj in ProjectLabelObjs:
                    projects.append(obj.project)
                recruit = [1, 3]


            return render_to_response('project/projects.html', {'projectLabels':models.ProjectLabel.objects.all() , "projects":projects, "recruit":recruit })
        else:
            id = req.POST['projectId']
            project = get_object_or_404(models.Project, pk=id)
            comments = models.Comment.objects.fitler(project=id).order_by('Date')
            return render_to_response('project/projects.html',
                                      {'comments': comments})
    except Exception as e:
        print(e)
        return HttpResponse("<script type='text/javascript'>alert('数据有异常，请稍后再试')</script>")
''' 招募项目相关页面结束'''
@csrf_exempt
def recruit(req):
    '''
    招募项目筛选项目显示
    '''
    try:
        if req.method == 'GET':
            sign = req.GET['sign']
            #  如果是所有项目
            if sign == "all":
                projects = models.Project.objects.filter(Q(Statue=1)|Q(Statue=3)).order_by('Id')
                projectLabels = models.ProjectLabel.objects.all()
                recruit = [1, 3]
            return render_to_response('project/projects.html', {'projectLabels': projectLabels[:4], "projects":projects, "recruit":recruit})
        else:
            id = req.POST['projectId']
            project = get_object_or_404(models.Project, pk=id)
            comments = models.Comment.objects.fitler(project=id).order_by('Date')
            return render_to_response('project/projects.html',
                                      {'comments': comments})
    except Exception as e:
        print(e)
        return HttpResponse("<script type='text/javascript'>alert('数据有异常，请稍后再试')</script>")

''' 开发项目相关页面开始'''

@csrf_exempt
def deprojects(req):
    '''
    开发项目 筛选
    '''
    try:
        if req.method == 'GET':
            sign = req.GET['sign']
            #  如果是所有项目
            if sign == "all":
                projects = models.Project.objects.filter(Q(Statue=2)|Q(Statue=4)).order_by("Id")
                projectLabels = models.ProjectLabel.objects.all()
                recruit = [1, 3]
            return render_to_response('project/projects.html', {'projectLabels': projectLabels , "projects": projects, "recruit":recruit})

        else:
            id = req.POST['projectId']
            project = get_object_or_404(models.Project, pk=id)
            comments = models.Comment.objects.fitler(project=id).order_by('Date')
            return render_to_response('project/deprojects.html',
                                      {'comments': comments})
    except Exception as e:
        print(e)
        return HttpResponse("<script type='text/javascript'>alert('数据有异常，请稍后再试')</script>")


@csrf_exempt
def starttime(req):
    '''
    开发项目一级页面项目显示
    '''
    try:
        if req.method == 'GET':
            sign = req.GET['sign']
            #  如果是所有项目
            if sign == "all":
                projects = models.Project.objects.all().order_by("StartTime")
                recruit = [1, 3]
            return render_to_response('project/projects.html', {'projectLabels': models.ProjectLabel.objects.all() , "projects": projects, "recruit":recruit})

        else:
            id = req.POST['projectId']
            project = get_object_or_404(models.Project, pk=id)
            comments = models.Comment.objects.fitler(project=id).order_by('Date')
            return render_to_response('project/deprojects.html',
                                      {'comments': comments})
    except Exception as e:
        print(e)
        return HttpResponse("<script type='text/javascript'>alert('数据有异常，请稍后再试')</script>")


@csrf_exempt
def praisecount(req):
    '''
    开发项目一级页面项目显示
    '''
    try:
        if req.method == 'GET':
            sign = req.GET['sign']
            #  如果是所有项目
            if sign == "all":
                pprojects = models.Project.objects.all()
                recruit = [1, 3]
                array2 = []
                projects=[]

                for project in pprojects:
                    res = {}
                    procount = models.Praise.objects.filter(project=project).count()
                    res[0] = project
                    res[1] = procount
                    array2.append(res)
            array2 = sorted(array2, key=lambda array2: array2[1], reverse=True)
            for p in array2:
                projects.append(p[0])
            proBest = array2[0][0]

            return render_to_response('project/projects.html', {'projectLabels': models.ProjectLabel.objects.all() , "projects": projects, "recruit":recruit,"array2":array2})

        else:
            id = req.POST['projectId']
            project = get_object_or_404(models.Project, pk=id)
            comments = models.Comment.objects.fitler(project=id).order_by('Date')
            return render_to_response('project/deprojects.html',
                                      {'comments': comments})
    except Exception as e:
        print(e)
        return HttpResponse("<script type='text/javascript'>alert('数据有异常，请稍后再试')</script>")


@csrf_exempt
def commentcount(req):
    '''
    开发项目一级页面项目显示
    '''
    try:
        if req.method == 'GET':
            sign = req.GET['sign']
            #  如果是所有项目
            if sign == "all":
                pprojects = models.Project.objects.all()
                recruit = [1, 3]
                array2 = []
                projects=[]

                for project in pprojects:
                    res = {}
                    procount = models.Comment.objects.filter(project=project).count()
                    res[0] = project
                    res[1] = procount
                    array2.append(res)
            array2 = sorted(array2, key=lambda array2: array2[1], reverse=True)
            for p in array2:
                projects.append(p[0])


            return render_to_response('project/projects.html', {'projectLabels': models.ProjectLabel.objects.all() , "projects": projects, "recruit":recruit,"array2":array2})

        else:
            id = req.POST['projectId']
            project = get_object_or_404(models.Project, pk=id)
            comments = models.Comment.objects.fitler(project=id).order_by('Date')
            return render_to_response('project/deprojects.html',
                                      {'comments': comments})
    except Exception as e:
        print(e)
        return HttpResponse("<script type='text/javascript'>alert('数据有异常，请稍后再试')</script>")

@csrf_exempt
def dedetails(req):
    '''
    开发项目二级页面详情
    '''
    if req.method == 'GET':
        projectId = req.GET['projectId']
        project = models.Project.objects.get(Id=projectId)
        user = models.ProjectUser.objects.get(project_id=projectId)
        labels = models.Project2ProjectLabel.objects.filter(project_id=projectId)
        praises = models.Praise.objects.all()
        comments = models.Comment.objects.filter(project_id=projectId).order_by("-Date")
        commentlist = []
        for comment in comments:
            if comment.commentedId is None:
                newcomment = []
                newcomment.append(comment)
                commentlist.append(newcomment)
        for comlist in commentlist:
            for comment in comments:
                if str(comlist[0].Uuid) == str(comment.commentedId):
                    comlist.append(comment)
        alllables = []  # 找出本项目所有的标签
        for label in labels:
            alllables.append(label.projectLabel.Id)
        alllables = list(set(alllables))
        project2projectLabel = models.Project2ProjectLabel.objects.filter(projectLabel_id__in=alllables)  # 所有相关标签的 所有标签2项目


        try:
            useremail = req.COOKIES.get('user_email')
            preuser = models.User.objects.get(Email=useremail)
            projectfollow = models.Follow.objects.filter(Q(project__Id=projectId) & Q(user=preuser))
            projectpraise = models.Praise.objects.filter(Q(project__Id=projectId) & Q(user=preuser))
            print(projectpraise)
            if projectfollow.count() is 0:
                fstatus = 0
            else:
                fstatus = 1

            if projectpraise.count() is 0:
                pstatus = 0
            else:
                pstatus = 1

            return render_to_response('project/dedetails.html',
                                  {"project": project, "project2projectLabels": project2projectLabel[:2],
                                   "labels": labels[:3], "user": user,
                                     'praises': praises, "fstatus":fstatus,"pstatus":pstatus,"comment": commentlist,"preuser":preuser })
        except:
            return render_to_response('project/dedetails.html',{"project": project, "project2projectLabels": project2projectLabel[:2],
                                   "labels": labels[:3], "user":user,'praises': praises,"comment":commentlist,})


    if req.method == "POST":
         pass


''' 开发项目相关页面结束'''



'''个人中心相关页面'''

@csrf_exempt
def homepage(req):
    if req.method == 'GET':
        user_email = req.COOKIES.get('user_email')
        user = models.User.objects.get(Email=user_email)
        userfollow = models.Follow.objects.filter(user=user).count()
        userpraise = models.Praise.objects.filter(user=user).count()
        return render_to_response(['personal/homepage.html','personal/unread_messages.html'], {"user": user, "userfollow": userfollow, "userpraise": userpraise})
    if req.method == 'POST':
        pass


@csrf_exempt
def release(req):
    '''
    发布项目页面
    :param req:
    :return:
    '''
    if req.method == 'GET':
        obj = models.ProjectLabel.objects.all()
        user_email = req.COOKIES.get('user_email')
        username = models.User.objects.get(Email=user_email)
        return render_to_response('personal/release.html', {"labels": obj,"username":username})
    if req.method == "POST":
        resData= {
            'status': 0,
            'message': ''
        }
        ProjectName = req.POST["proTitle"]
        img = req.POST["coverMap"]
        base64Code = img.split(',')[1]
        fileext = img.split(',')[0].split(';')[0].split('/')[1]
        Img = decode_img(base64Code, datetime.strftime(datetime.now(), "%Y-%m-%d=%H:%M:%S"),fileext)
        Description = req.POST["rhtml"]
        recruit = req.POST["recruit"]
        Description = remove_script(Description)
        # Summary = Description
        Number = int(req.POST["numPerson"])
        EndTime = req.POST["endTime"]
        EndTime = datetime.strptime(EndTime, "%Y/%m/%d")
        proLabels = req.POST["proLabels"].split('*')
        Statue = int(req.POST["statue"])
        Identity = 1
        State = 1
        Time = 1
        RecruitedNumber = 0
        print EndTime
        try:
            user_email = req.COOKIES.get('user_email')
            user = models.User.objects.get(Email=user_email)
            project = models.Project.objects.create(ProjectName=ProjectName,Description=Description,Number=Number,
                                                    StartTime=datetime.now(), EndTime=EndTime,Statue=Statue,
                                                    Img=Img,Uuid=uuid.uuid4())
            project.save()
            for label in proLabels[:-1] :
                Label = models.ProjectLabel.objects.get(ProjectLabelName=label)
                project2ProjectLabel = models.Project2ProjectLabel.objects.create(projectLabel=Label,project= project,Uuid=uuid.uuid4() )
            project2ProjectLabel.save()
            models.ProjectUser.objects.create(user=user,project=project,Identity=Identity).save()
            models.Recruit.objects.create(project=project,StartTime=datetime.now(), EndTime=EndTime,Describe=recruit,
                                          State=State,Times=Time,PredictNumber=Number,RecruitedNumber=RecruitedNumber,
                                          Uuid=uuid.uuid4()).save()
            resData['status'] = 1
            resData['message'] = 'success'
        except Exception as e :
            print(e)
            resData['message'] = str(e)
        return HttpResponse(json.dumps(resData))


@csrf_exempt
def editprofile(req):
    if req.method == 'GET':
        email = req.COOKIES.get('user_email')
        try:
            user = models.User.objects.get(Email=email)
        except Exception as e:
            print(e.message)
        else:
            return render_to_response('personal/editprofile.html', {"user": user})
    if req.method == 'POST':
        email = req.COOKIES.get('user_email')
        username = req.POST["username"]
        school = req.POST["school"]
        institude = req.POST["institude"]
        major = req.POST["major"]
        sex = req.POST["sex"]
        print (sex)
        result = {
            "status": 0,
            "string": ''
        }
        try:
            models.User.objects.filter(Email=email).update(UserName=username, School=school, Institude=institude, Major=major, Sex=sex)
        except Exception as e:
            print(e)
            result["status"] = 0
            result["string"] = "空"
            return HttpResponse(json.dumps(result))
        else:
            # print(locals())
            return HttpResponse(json.dumps(result))


@csrf_exempt
def unread_messages(req):
    '''
    未读消息
    :param req:
    :return:
    '''
    if req.method == 'GET':
        try:
            email = req.COOKIES.get('user_email')
            if email:
                messageuse = models.Message.objects.filter(IsUse=True)
                if messageuse:
                    user = models.User.objects.get(Email=email)
                    message_content = messageuse.filter(Q(user=user) & Q(IsRead=False))
            else:
                return render_to_response('idea/index.html')
        except Exception as e:
            print(e)
            return HttpResponse("<script type='text/javascript'>alert('数据有异常，请稍后再试')</script>")
        else:
            return render_to_response('personal/unread_messages.html', {"message_content": message_content})
    if req.method == 'POST':
        messageId = req.POST["messageId"]
        result = {
            "status": 0,
            "string": ''
        }
        try:
            message = models.Message.objects.get(Id=messageId)
            message.IsUse = False
            message.save()
            result['status'] = 1
            result['string'] = 'success'
        except Exception as e:
            print (e)
        else:
            return HttpResponse(json.dumps(result))


@csrf_exempt
def show_messages(req):
    '''
    展示未读消息详情
    :param req:
    :return:
    '''
    infoId = models.Message.objects.get(Id=req.POST['infoId'])
    list = {}
    list['Date'] = infoId.Date.strftime("%Y/%m/%d")
    list['Priority'] = infoId.Priority
    list['Content'] = infoId.Content
    return HttpResponse(json.dumps(list))


@csrf_exempt
def unread_read(req):
    '''
    未读消息点击查看置为已读
    :param req:
    :return:
    '''
    if req.method == 'POST':
        messageId = req.POST["infoId"]
        result = {
            "status": 0,
            "string": ''
        }
        try:
            message = models.Message.objects.get(Id=messageId)
            message.IsRead = True
            message.save()
            result['status'] = 1
            result['string'] = 'success'
        except Exception as e:
            print (e)
        else:
            return HttpResponse(json.dumps(result))


@csrf_exempt
def read_message(req):
    '''
    已读消息
    :param req:
    :return:
    '''
    if req.method == 'GET':
        try:
            email = req.COOKIES.get('user_email')
            if email:
                messageuser = models.Message.objects.filter(IsUse=True)
                if messageuser:
                    user = models.User.objects.get(Email=email)
                    message_contents = messageuser.filter(Q(user=user) & Q(IsRead=True))
            else:
                return render_to_response('idea/index.html')
        except Exception as e:
            print(e)
            return HttpResponse("<script type='text/javascript'>alert('数据有异常，请稍后再试')</script>")
        else:
            return render_to_response('personal/read_message.html', {"message_contents": message_contents})
    if req.method == 'POST':
        messageId = req.POST["messageId"]
        result = {
            "status": 0,
            "string": ''
        }
        try:
            message = models.Message.objects.get(Id=messageId)
            message.IsUse = False
            message.save()
            result['status'] = 1
            result['string'] = 'success'
        except Exception as e:
            print (e)
        else:
            return HttpResponse(json.dumps(result))



@csrf_exempt
def allFollow(req):
    '''
    总关注页面
    :param req:
    :return:
    '''
    if req.method == 'GET':
        email = req.COOKIES.get('user_email')
        user = models.User.objects.get(Email=email)
        follows = models.Follow.objects.filter(Q(user=user))
        return render_to_response(['personal/profollow.html ','personal/creationfollow.html'], {"follows": follows})
    if req.method == 'POST':
        pass


@csrf_exempt
def profollow(req):
    '''
    关注项目页面
    :param req:
    :return:
    '''
    if req.method == 'GET':
        email = req.COOKIES.get('user_email')
        user = models.User.objects.get(Email=email)
        follows = models.Follow.objects.filter(Q(user=user))
        return render_to_response('personal/profollow.html ', {"follows": follows})
    if req.method == 'POST':
        proId = req.POST["proId"]
        result = {
            "status": 1,
            "string": 'success'
        }
        try:
            project = models.Project.objects.get(Id=proId)
            email = req.COOKIES.get('user_email')
            user = models.User.objects.get(Email=email)
            follow = models.Follow.objects.get(user=user, project=project)
            follow.delete()
        except Exception as e:
            print(e)
            result['message'] = e
        return HttpResponse(json.dumps(result))


@csrf_exempt
def creationfollow(req):
    '''
    关注灵感页面
    :param req:
    :return:
    '''
    if req.method == 'GET':
        email = req.COOKIES.get('user_email')
        user = models.User.objects.get(Email=email)
        follows = models.Follow.objects.filter(Q(user=user))
        return render_to_response('personal/creationfollow.html', {"follows": follows})
    if req.method == 'POST':
        creationId = req.POST["creationId"]
        result = {
            "status": 1,
            "string": 'success'
        }
        try:
            creation = models.Creation.objects.get(Id=creationId)
            email = req.COOKIES.get('user_email')
            user = models.User.objects.get(Email=email)
            follow = models.Follow.objects.get(user=user, creation=creation)
            follow.delete()
        except Exception as e:
            print(e)
            result['message'] = e
        return HttpResponse(json.dumps(result))



@csrf_exempt
def userfollow(req):
    '''
    关注用户页面
    :param req:
    :return:
    '''
    if req.method == 'GET':
        return render_to_response('personal/userfollow.html')
    if req.method == 'POST':
        pass

@csrf_exempt
def following_user(req):
    '''
    我关注用户页面
    :param req:
    :return:
    '''
    if req.method == 'GET':
        email = req.COOKIES.get('user_email')
        user = models.User.objects.get(Email=email)
        follows = models.Follow.objects.filter(Q(Follower=user))
        return render_to_response('personal/following_user.html',{"follows": follows})
    if req.method == 'POST':
        following_Id = req.POST["following_Id"]
        result = {
            "status": 1,
            "string": 'success'
        }
        try:
            following_user = models.User.objects.get(Id=following_Id)
            email = req.COOKIES.get('user_email')
            follower = models.User.objects.get(Email=email)
            follow = models.Follow.objects.get(user=following_user,Follower=follower)
            follow.delete()
        except Exception as e:
            print(e)
            result['message'] = e
        return HttpResponse(json.dumps(result))


@csrf_exempt
def follower_user(req):
    '''
    关注我的用户页面
    :param req:
    :return:
    '''
    if req.method == 'GET':
        email = req.COOKIES.get('user_email')
        user = models.User.objects.get(Email=email)
        follows = models.Follow.objects.filter(Q(user=user))
        return render_to_response('personal/follower_user.html',{"follows": follows})
    if req.method == 'POST':
        pass


@csrf_exempt
def perCreation(req):
    '''
    个人中心创意灵感
    :param req:
    :return:
    '''
    if req.method == 'GET':
        user_email = req.COOKIES.get('user_email')
        creation = models.Creation.objects.filter(Q(user__Email=user_email) & Q(IsUse=True))
        return render_to_response('personal/perCreation.html',{"creation":creation})
    if req.method == 'POST':
        result = {
            'message': None,
            'status': 0,
            'creationId': None,
            'uuid': None
        }
        try:
            creationId = req.POST['creationId']
            models.Creation.objects.filter(Id=creationId).update(IsUse=False)
            result['status'] = 1
            result['message'] = '更改成功'
            return HttpResponse(json.dumps(result))
        except:
            result['status'] = 0
            result['message'] = '获取信息失败'
            return HttpResponse(json.dumps(result))



@csrf_exempt
def PM(req):
    '''
    个人中心发布项目及草稿删除
    :param req:
    :return:
    '''
    if req.method == 'GET':
        user_email = req.COOKIES.get('user_email')
        projectUser = models.ProjectUser.objects.filter(Q(user__Email=user_email) & Q(Identity=1)&~Q(project__Statue=0))
        project = []
        for obj in projectUser:
            project.append(obj.project)
        return render_to_response('personal/PM.html',{'project':project})
    if req.method == 'POST':
        result = {
            'message': None,
            'status': 0,
            'creationId': None,
            'uuid': None
        }
        try:
            projectId = req.POST['projectId']
            models.Project.objects.filter(Id=projectId).update(Statue=6)
            result['status'] = 1
            result['message'] = '更改成功'
            return HttpResponse(json.dumps(result))
        except:
            result['status'] = 0
            result['message'] = '获取信息失败'
            return HttpResponse(json.dumps(result))


@csrf_exempt
def PM_join(req):
    '''
    个人中心参与的项目
    :param req:
    :return:
    '''
    user_email = req.COOKIES.get('user_email')
    if req.method == 'GET':
        projectUser = models.ProjectUser.objects.filter(Q(user__Email=user_email) & Q(Identity=0))
        project = []
        for obj in projectUser:
            project.append(obj.project)
        return render_to_response('personal/PM_join.html',{'project':project,})
    if req.method == 'POST':
        # result = {
        #     'message': None,
        #     'status': 0,
        #     'creationId': None,
        #     'uuid': None
        # }
        # try:
        #     projectId = req.POST['projectId']
        #     models.ProjectUser.objects.filter(Q(project__Id=projectId)&Q(user__Email=user_email)).update(Identity=3)
        #     user = models.ProjectUser.objects.filter(Q(project__Id=projectId)&Q(Identity=1)).values('user')
        #
        #     user0 ={{ProjectUser0.user.Id}}
        #     user = models.User.object.filter(Id=user0)
        #     models.Message.objects.create(user=user,Content=123).save()
        #     result['status'] = 1
        #     result['message'] = '更改成功'
        #     return HttpResponse(json.dumps(result))
        # except:
        #     result['status'] = 0
        #     result['message'] = '获取信息失败'
        #     return HttpResponse(json.dumps(result))
        pass


@csrf_exempt
def PM_draft(req):
    '''
    个人中心暂存的项目发布
    :param req:
    :return:
    '''
    if req.method == 'GET':
        user_email = req.COOKIES.get('user_email')
        projectUser = models.ProjectUser.objects.filter(Q(user__Email=user_email) & Q(project__Statue=0))
        project = []
        for obj in projectUser:
            project.append(obj.project)
        return render_to_response('personal/PM_draft.html',{'project':project})
    if req.method == 'POST':
        result = {
            'message': None,
            'status': 0,
            'uuid': None
        }
        try:
            projectId = req.POST['projectId']
            models.Project.objects.filter(Id=projectId).update(Statue=1)
            result['status'] = 1
            result['message'] = '更改成功'
            return HttpResponse(json.dumps(result))
        except:
            result['status'] = 0
            result['message'] = '获取信息失败'
            return HttpResponse(json.dumps(result))


@csrf_exempt
def PM_content(req,projectid):
    '''
    个人中心项目管理
    :param req:
    :return:
    '''
    if req.method == 'GET':
        project = models.Project.objects.get(Id=projectid)

        user = models.ProjectUser.objects.filter(Q(project_id=projectid)&Q(Identity=0))
        firstUser = models.ProjectUser.objects.filter(Q(project_id=projectid)&Q(Identity=1))

        labels = models.ProjectLabel.objects.all()
        recruit = models.Recruit.objects.filter(project__Id=projectid)

        if recruit.exists():
            recruit = recruit[0]
        try:
            return render_to_response('personal/PM_content.html',{"project": project, "labels": labels,"firstUser":firstUser[0], "user": user, "recruit": recruit,})
        except:
            return render_to_response('personal/PM_content.html')

    if req.method == "POST":

        result = {
            'message': None,
            'status': 0,
            'picture':None,
            "tlabel":None,
            'uuid': None
        }

        try:

            proTitle = req.POST['proTitle']
            picture = req.POST['picture']
            Description = req.POST["rhtml"]
            Description = remove_script(Description)

            numPerson = req.POST['numPerson']
            EndTime = req.POST["endTime"]

            proLabels = req.POST['proLabels'].split('*')
            tlabel = req.POST['tlabel']
            postCon = req.POST['postCon']
            plan = req.POST['plan']
            img = req.FILES.get("coverMap")

            EndTime = datetime.strptime(EndTime,"%Y/%m/%d")

        except:
            result['status'] = 0
            result['message'] = '获取信息失败'
            return HttpResponse(json.dumps(result))
        else:
            if picture == '0':
                if tlabel == '0':
                    print plan
                    models.Project.objects.filter(Id=projectid).update(ProjectName=proTitle,Statue=plan,Description=Description,EndTime=EndTime)
                    models.Recruit.objects.filter(project__Id=projectid).update(PredictNumber=numPerson,Describe=postCon)
                    result['status'] = 1
                    result['message'] = '成功'
                    return HttpResponse(json.dumps(result))
                elif tlabel=='1':
                    for label in proLabels[:-1]:
                        Label = models.ProjectLabel.objects.get(ProjectLabelName=label)
                        models.Project2ProjectLabel.objects.filter(project__Id=projectid).update(projectLabel=Label)
                        models.Project.objects.filter(Id=projectid).update(ProjectName=proTitle, Statue=plan,
                                                                           Description=Description, EndTime=EndTime)
                        models.Recruit.objects.filter(project__Id=projectid).update(PredictNumber=numPerson,
                                                                                    Describe=postCon)
                        result['status'] = 1
                        result['message'] = '成功'
                    return HttpResponse(json.dumps(result))
            elif picture == '1':
                if tlabel == '0':
                    models.Project.objects.filter(Id=projectid).update(ProjectName=proTitle,Statue=plan,Description=Description,EndTime=EndTime,Img=img)
                    models.Recruit.objects.filter(project__Id=projectid).update(PredictNumber=numPerson,Describe=postCon)
                    result['status'] = 1
                    result['message'] = '成功'
                    return HttpResponse(json.dumps(result))
                elif tlabel=='1':
                    for label in proLabels[:-1]:
                        Label = models.ProjectLabel.objects.get(ProjectLabelName=label)
                        models.Project2ProjectLabel.objects.filter(project__Id=projectid).update(projectLabel=Label)
                        models.Project.objects.filter(Id=projectid).update(ProjectName=proTitle, Statue=plan,
                                                                           Description=Description, EndTime=EndTime,
                                                                           Img=img)
                        models.Recruit.objects.filter(project__Id=projectid).update(PredictNumber=numPerson,
                                                                                    Describe=postCon)
                        result['status'] = 1
                        result['message'] = '成功'
                    return HttpResponse(json.dumps(result))






@csrf_exempt
def delpeople(req):
    '''
    个人中心项目成员删除
    :param req:
    :return:
    '''

    try:
        result = {
            'message': None,
            'status': 0,
            'creationId': None,
            'uuid': None
        }
        try:
            projectId = req.POST['projectId']
            peopleId = req.POST['peopleId']
            models.ProjectUser.objects.filter(Q(project__Id=projectId) & Q(user__Id=peopleId)).update(Identity=3)
            result['status'] = 1
            result['message'] = '更改成功'
            return HttpResponse(json.dumps(result))
        except:
            result['status'] = 0
            result['message'] = '获取信息失败'
            return HttpResponse(json.dumps(result))
    except Exception as e:
        return HttpResponse(status)


@csrf_exempt
def personal_information(req):
    '''
    个人信息
    :param req:
    :return:
    '''
    if req.method == 'GET':
        try:
            email = req.COOKIES.get('user_email')
            print(email)
            if email:
                user = models.User.objects.get(Email=email)
            else:
                return render_to_response('idea/index.html')
        except Exception as e:
            print(e.message)
        else:
            return render_to_response('personal/personal_information.html', {"user": user})
    if req.method == 'POST':
        personal_input = req.POST["personal_input"]
        user_school = req.POST["user_school"]
        user_college = req.POST["user_college"]
        user_major = req.POST["user_major"]
        sex = req.POST["sex"]
        user_id = req.POST["user_id"]
        remove_script(personal_input)
        remove_script(user_school)
        remove_script(user_college)
        remove_script(user_major)
        result = {
            "status": 0,
            "string": ''
        }
        try:
            information = models.User.objects.get(Id=user_id)
            information.UserName = personal_input
            information.School = user_school
            information.Institude = user_college
            information.Major = user_major
            information.Sex = sex
            information.save()
            result['status'] = 1
            result['string'] = 'success'
        except Exception as e:
            print (e)
        else:
            return HttpResponse(json.dumps(result))


@csrf_exempt
@require_http_methods(["GET", "POST"])
def account_information(req):
    '''
    账号信息
    :param req: 
    :return:
    '''
    if req.method == 'GET':
        try:
            email = req.COOKIES.get('user_email')
            print(email)
            if email:
                user = models.User.objects.get(Email=email)
            else:
                return render_to_response('idea/index.html')
        except Exception as e:
            print(e)
            # result['status'] = 0
            # result['message'] = '更改失败'
        else:
            return render_to_response('personal/account_information.html', {"user": user})
    if req.method == 'POST':
        telphone = req.POST["telphone"]
        user_mark = req.POST["user_mark"]
        result = {
            "status": 0,
            "string": ''
        }
        remove_script(telphone)
        try:
            user_telphone = models.User.objects.get(Id=user_mark)
            user_telphone.Phone = telphone
            user_telphone.save()
            result['status'] = 1
            result['string'] = 'success'
        except Exception as e:
            print (e)
        else:
            return HttpResponse(json.dumps(result))


@csrf_exempt
def account_information_imgs(req):
    if req.method == 'POST':
        postData = req.POST
        user_mark = postData.get("user_mark")
        if req.FILES:
            user_img = req.FILES.get('Img')
        else:
            user_img = None
        result = {
            "status": 0,
            "string": ''
        }
        try:
            user_telphone = models.User.objects.get(Id=user_mark)
            user_telphone.Img = user_img
            user_telphone.save()
            result['status'] = 1
            result['string'] = 'success'
        except Exception as e:
            result['message'] = str(e)
        else:
            return HttpResponse(json.dumps(result))


@csrf_exempt
def change_password(req):
    '''

    更改密码
    :param req: 
    :return: 
    '''
    if req.method == 'GET':
        if req.method == 'GET':
            try:
                email = req.COOKIES.get('user_email')
                if email:
                    user = models.User.objects.get(Email=email)
                else:
                    return render_to_response('idea/index.html')
            except Exception as e:
                print(e)
            else:
                return render_to_response('personal/change_password.html', {"user": user})
    if req.method == 'POST':
        change_password_email = req.POST["change_password_email"]
        old_password = req.POST["old_password"]
        new_password = req.POST["new_password"]
        result = {
            "status": 0,
            "string": ''
        }
        try:
            user_password = models.User.objects.get(Email=change_password_email)
            if user_password.PassWord == old_password:
                user_password.PassWord = new_password
                user_password.save()
            result['status'] = 1
            result['string'] = 'success'
        except Exception as e:
            print(e)
        else:
            return HttpResponse(json.dumps(result))


@csrf_exempt
def personal_label(req):
    if req.method == 'GET':
        try:
            label_list = []
            email = req.COOKIES.get('user_email')
            if email:
                user_lable = models.UserLabel.objects.all()
                user = models.User.objects.get(Email=email)
                user_show_label = models.User2UserLabel.objects.filter(user=user)
                for user_show in user_show_label:
                    label_list.append(user_show.userLabel.Name)
            else:
                return render_to_response('idea/index.html')
        except Exception as e:
            print(e)
        else:
            return render_to_response('personal/personal_label.html', {"user_lable": user_lable, "user": user, "user_show_label":user_show_label, "label_list":label_list})
    if req.method == 'POST':
        proLabels = req.POST["proLabels"].split('*')
        label_mark = req.POST["label_mark"]
        result = {
            "status": 0,
            "string": ''
        }
        try:
            user = models.User.objects.get(Email=label_mark)
            for label in proLabels[:-1]:
                user_label = models.UserLabel.objects.get(Name=label)
                models.User2UserLabel.objects.create(user=user, userLabel=user_label).save()
            result['status'] = 1
            result['string'] = 'success'
        except Exception as e:
            print(e)
            result['message'] = str(e)
        return HttpResponse(json.dumps(result))


@csrf_exempt
def user_delete_personal_label(req):
    if req.method == 'POST':
        label = req.POST["label"]
        label_mark = req.POST["label_mark"]
        result = {
            "status": 0,
            "string": ''
        }
        try:
            user = models.User.objects.get(Email=label_mark)
            user_label = models.UserLabel.objects.get(Name=label)
            models.User2UserLabel.objects.filter(user=user, userLabel=user_label).delete()
            result['status'] = 1
            result['string'] = 'success'
        except Exception as e:
            print(e)
        else:
            return HttpResponse(json.dumps(result))
'''个人中心相关页面结束'''





