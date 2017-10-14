# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from itertools import chain
import json

from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, render_to_response, get_object_or_404, Http404
from django.db.models import Q
from admina.models import Creation2ProjectLabel, Creation, ProjectLabel, Comment, User, Praise, Follow, ProjectUser, \
    Project2ProjectLabel, Project
from admina import models

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import uuid
import re, base64

try:
    import cStringIO as StringIO
except ImportError:
    import StringIO

from idear.Idea_util.ImgVerification import generate_verify_image
from django.views.decorators.csrf import csrf_exempt


# Create your views here.







''' 页面统一功能视图'''
@csrf_exempt
def Check_User_Cookie(req):
    '''
    登陆验证函数，如需登陆，调此函数即可，仍需调试
    @:return 状态值，可通过为true
    @:COOKIE name = User_acconunt
    @:COOKIE name = UUID
    '''
    loginStatus = False
    try:
        user_cookie = req.COOKIES["email"]
        user_uuid_code = req.COOKIES["uuid"]
        try:
            user = models.User.objects.get(Email=user_cookie)
            if user_uuid_code == user_uuid_code:
                loginStatus = True
                return loginStatus
        except:
            return loginStatus
    except:
        return loginStatus

def varidate_char(str, max_length=20):
    '''
    非法字符验证
    :param sql: 
    :param max_length: 
    :return: False  表示字符串中含有非法字符    True 表示字符串中不含有非法字符
    '''
    if len(str) > max_length:
        return False
    dirty_stuff = ["\"", "\\", "/", "*", "'", "=", "-", "#", ";", "<", ">", "+", "%", "$", "(", ")", "%", "@", "!"]
    for char in str:
        if char in dirty_stuff:
            return False
    return True

def varidate_emial(str, max_length=20):
    '''
    邮箱格式验证
    :param str: 
    :param max_length: 
    :return: 
    '''
    if len(str) > max_length:
        return False
    if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", str) != None:
        return True
    else:
        return False

@csrf_exempt
def get_user_img(req):
    '''
    动态获取用户图片
    :param req: 
    :return: 
    '''
    if req.method == "GET":
        # user = models.User.objects.get(Email='chris156@123.com')
        # img = str(user.Img)
        # print img
        # return HttpResponse('ok')
        return Http404
    elif req.method == "POST":
        result = {
            'status': 0,
            'message': None,
            'img_path': None
        }
        try:
            email = req.COOKIES.get('email')
            username = req.COOKIES.get('username')
        except:
            result['status'] = 0
            result['message'] = '尚未登陆'
            return HttpResponse(json.dumps(result))
        else:
            try:
                user = models.User.objects.filter(Email=email)
            except:
                result['status'] = 0
                result['message'] = '获取数据异常'
                return HttpResponse(json.dumps(result))
            else:
                try:
                    img_path = user.Img
                    result['status'] = 1
                    result['message'] = '路径获取成功'
                    result['img_path'] = img_path
                except:
                    img_path = 'photos/2017/09/19/user/default_cdNstvn.jpg'
                    result['status'] = 1
                    result['message'] = '用户暂未上传图片'
                    result['img_path'] = img_path
                    return HttpResponse(json.dumps(result))
                else:
                    return HttpResponse(json.dumps(result))

@csrf_exempt
def test(req, param):
    ''''
    测试页面
    '''
    if req.method == "GET":
        teams = models.User.objects.all().filter(Identity=2)
        return render_to_response('team/test.html', {'teams': teams})
    if req.method == "POST":
        data = req.POST["data"]
        return HttpResponse(data)

def index(req):
    '''
    返回首页页面
    :param req: 
    :return: 
    '''
    if req.method == "GET":
        return render_to_response('idea/index.html')
    if req.method == "POST":
        pass

@csrf_exempt
def login(req):
    '''
    登陆界面的处理
    :param req: 
    :return: 
    '''
    if req.method == "GET":
        return render_to_response('idea/login.html')
    if req.method == "POST":
        result = {}
        result['email'] = None
        result['status'] = None
        result['message'] = ''
        result['username'] = None
        result['uuid'] = None
        try:
            email = req.POST['email']
            password = req.POST['password']
        except:
            result['status'] = 0
            result['message'] = '获取信息失败'
            return HttpResponse(json.dumps(result))
        else:
            if varidate_emial(email):
                if models.User.objects.filter(Q(Email=email)):
                    user = models.User.objects.get(Email=email)
                    if user.PassWord == password:
                        user.Uuid = uuid.uuid1()
                        result['status'] = 1
                        result['username'] = user.UserName
                        result['email'] = email
                        req.session['uuid'] = str(user.Uuid)
                        result['message'] = '登陆成功'
                        return HttpResponse(json.dumps(result))
                    elif user.PassWord != password:
                        result['status'] = 0
                        result['message'] = '用户名或密码错误'
                        return HttpResponse(json.dumps(result))
                else:
                    result['status'] = 0
                    result['message'] = '用户名或密码错误'
                    return HttpResponse(json.dumps(result))
            else:
                result['status'] = 0
                result['message'] = '帐号格式不正确'
                return HttpResponse(json.dumps(result))

@csrf_exempt
def regist(req):
    '''
    注册页面
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
            'emial': None,
            'uuid': None
        }
        try:
            username = req.POST['UserName']
            email = req.POST['Email']
            password = req.POST['Passwd']
        except:
            result['status'] = 0
            result['message'] = '获取信息失败'
            return HttpResponse(json.dumps(result))
        else:
            if not (varidate_char(username) and varidate_emial(email)):
                result['message'] = '输入非法字符'
                result['status'] = 0
                return HttpResponse(json.dumps(result))
            elif models.User.objects.filter(Email=email):
                result['status'] = 0
                result['message'] = '邮箱已经被注册'
                return HttpResponse(json.dumps(result))
            elif models.User.objects.filter(UserName=username):
                result['status'] = 0
                result['message'] = '姓名已被注册'
                return HttpResponse(json.dumps(result))
            else:
                try:
                    models.User.objects.create(Email=email, UserName=username, PassWord=password, Uuid=uuid.uuid1())
                    user = models.User.objects.get(Email=email)
                    user.Img = 'photos/2017/09/19/user/default_cdNstvn.jpg'
                    req.session['uuid'] = str(user.Uuid)
                    result['email'] = email
                    result['username'] = username
                    result['message'] = '注册成功，正在调转'
                    result['status'] = 1
                    return HttpResponse(json.dumps(result))
                except Exception as e:
                    print(e)
                    result['status'] = 0
                    result['message'] = '服务器异常!!'
                    return HttpResponse(json.dumps(result))

@csrf_exempt
def logout(req):
    '''
    注销界面
    :param req: 
    :return: 
    '''
    if req.method == "GET":
        response = render_to_response('idea/index.html')
        response.delete_cookie('username')
        response.delete_cookie('email')
        return response

def forgetPassword(req):
    '''
    忘记密码页面
    :param req: 
    :return: 
    '''
    if req.method == 'GET':
        stream, strs = generate_verify_image(save_img=False)
        # req.sessions['verifycode'] = strs
        stream = base64.b64encode(stream.getvalue()).encode('ascii')
        req.session['verificode'] = strs
        return render_to_response('idea/forgetPassword.html', {'img': stream})

''' 功能页面相关视图结束'''
















''' 团队页面相关视图'''
def team(req):
    '''
    团队页面
    :param req: 
    :return: 
    '''
    if req.method == 'GET':
        teams = models.User.objects.all().filter(Identity=2)
        return render_to_response('team/team.html', {'teams': teams})
    if req.method == 'POST':
        pass

def teamdetails(req, teamid):
    '''
    团队详情页面 所有team 按照创建时间排序
    :param req: 
    :param teamid: 团队ID
    :return: 
    '''
    if req.method == 'GET':
        try:
            this_team = models.User.objects.get(Q(pk=teamid) & Q(Identity=teamid))
            labels = models.User2UserLabel.objects.filter(Q(user__Id=teamid))
        except Exception as e :
            print(e.message)
            return Http404
        else:
            print(labels)
            return render_to_response('team/teamdetails.html', {"team": this_team, "labels":labels})
    if req.method == 'POST':
        pass

def teamhelpapplication(req, teamhelpid):
    '''
    团队帮助申请
    :param req: 
    :param teamhelpid: 
    :return: 
    '''
    if req.method == 'GET':
        try:
            teamhelp = models.User.objects.get(Id=teamhelpid)
        except:
            return HttpResponse('404')
        else:
            if int(teamhelp.Identity) == 2:
                return render_to_response('team/teamhelpapplication.html', {'teamhelp': teamhelp})
            else:
                return HttpResponse('404')
    if req.method == 'POST':
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

def service(req):
    '''
    服务条款页面详情
    :param req: 
    :return: 
    '''
    if req.method == 'GET':
        return render_to_response('idea/service.html')
    if req.method == "POST":
        pass



''' 团队页面相关视图结束  '''














''' 创意灵感 页面相关部分开始'''

def redetail(req):
    '''
    创意详情
    :param req: 
    :return: 
    '''
    if req.method == 'GET':
        return render_to_response('creation/redetail.html')
    if req.method == "POST":
        pass


@csrf_exempt
def creations(req):
    '''
    创意灵感一级二级页面项目显示  
    '''
    projectLabels = ProjectLabel.objects.all()
    creations = Creation.objects.all().order_by("Date")
    User_img = creations.values('user__Img')
    praises = Praise.objects.all()
    follows = Follow.objects.all()
    # userId = int(req.COOKIES.get('user'))
    userId = 3
    try:
        if req.method == 'GET':
            sign = req.GET['sign']
            # 如果是所有项目
            if sign == "all":
                creations = creations
            # 如果有特殊标签
            else:
                CreationLabelObjs = Creation2ProjectLabel.objects.filter(projectLabel=sign)
                creations = Creation.objects.filter(Img="null")
                for obj in CreationLabelObjs:
                    creations = chain(creations, Creation.objects.filter(Id=int(obj.creation.Id)))
            return render_to_response('creation/index.html',
                                      {'creations': creations, 'projectLabels': projectLabels, 'userId': userId,
                                       'follows': follows, 'praises': praises, "Imgs": User_img})

        else:
            id = req.POST['creationId']
            creation = get_object_or_404(Creation, pk=id)
            comments = Comment.objects.fitler(creation=id).order_by('Date')
            user = creation.user
            return render_to_response('/creation/sec_creations.html',
                                      {'creation': creation, 'comments': comments, 'user': user})
    except Exception as e:
        print(e)
        return HttpResponse("<script type='text/javascript'>alert('数据有异常，请稍后再试')</script>")


@csrf_exempt
def star(req):
    '''
    点赞
    1为创意
    2为项目

    status
    状态值：0为失败，1为关注成功, 2为取消关注成功
    '''
    status = 0
    try:
        Id = req.POST["Id"]
        userId = req.POST["userId"]
        starType = int(req.POST["starType"])
        if starType == 1:
            try:
                p = Praise.objects.get(creation_id=Id, user_id=userId).delete()
                status = 2
            except:
                p = Praise.objects.create(creation_id=Id, user_id=userId)
                status = 1
            return HttpResponse(status)
        else:
            try:
                p = Praise.objects.get(project_id=Id, user_id=userId).delete()
                status = 2
            except:
                p = Praise.objects.create(project_id=Id, user_id=userId)
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
    状态值：0为操作失败，1为关注成功，2 为取消关注成功
    '''
    status = 0
    try:
        Id = req.POST['Id']
        userId = req.POST['userId']
        attendType = int(req.POST['attendType'])
        if attendType == 1:
            try:
                p = Follow.objects.get(creation_id=Id, user_id=userId).delete()
                status = 2
            except:
                p = Follow.objects.create(creation_id=Id, user_id=userId)
                status = 1
            return HttpResponse(status)
        elif attendType == 2:
            try:
                p = Follow.objects.get(project_id=Id, user_id=userId).delete()
                status = 2
            except:
                p = Follow.objects.create(project_id=Id, user_id=userId)
                status = 1
            return HttpResponse(status)
        elif attendType == 3:
            try:
                F = Follow.objects.get(Follower_id=Id, user_id=userId).delete()
                status = 2
            except:
                p = Follow.objects.create(Follower_id=Id, user_id=userId)
                status = 1
            return HttpResponse(status)
    except:
        return HttpResponse(status)


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
    '''
    if req.method == 'GET':
        return render_to_response('project/redetails.html')
    if req.method == 'POST':
        pass

@csrf_exempt
def projects(req):
    '''
    创意灵感一级二级页面项目显示
    '''
    projectLabels = ProjectLabel.objects.all()
    projects = Project.objects.all()
    try:
        if req.method == 'GET':
            sign = req.GET['sign']
            #  如果是所有项目
            if sign == "all":
                projects = projects
            # 如果有特殊标签
            else:
                ProjectLabelObjs = Project2ProjectLabel.objects.filter(projectLabel=sign)
                projects = Project.objects.filter(Img="null")
                for obj in ProjectLabelObjs:
                    projects = chain(projects, Project.objects.filter(Id=int(obj.project.Id)))
            return render_to_response('project/recruit.html', {'projects': projects, 'projectLabels': projectLabels})

        else:
            id = req.POST['projectId']
            project = get_object_or_404(Project, pk=id)
            comments = Comment.objects.fitler(project=id).order_by('Date')
            user = project.user
            return render_to_response('project/recruit.html',
                                      {'project': project, 'comments': comments, 'user': user})
    except:
        return HttpResponse("<script type='text/javascript'>alert('数据有异常，请稍后再试')</script>")


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
            p = Praise.objects.get_or_create(creation_id=Id, user_id=userId)
            status = 1
            return HttpResponse(status)
        else:
            p = Praise.objects.get_or_create(project_id=Id, user_id=userId)
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
    # try:
    Id = req.POST['Id']
    userId = req.POST['userId']
    attendType = int(req.POST['attendType'])
    if attendType == 1:
        p = Follow.objects.create(creation_id=Id, user_id=userId)
        status = 1
        return HttpResponse(status)
    elif attendType == 2:
        p = Follow.objects.create(project_id=Id, user_id=userId)
        status = 1
        return HttpResponse(status)
    elif attendType == 3:
        F = Follow.objects.create(Follower_id=Id, user_id=userId)
        status = 1
        return HttpResponse(status)
        # except:
        #     return HttpResponse(status)


def get_projects(req):
    if req.method == "GET":
        return Http404()
    if req.method == "POST":
        projects = Project.objects.all().order_by('Id').filter()
        account = req.COOKIES.get('account')
        user = User.objects.filter(Account=account)
        if account:
            projects = ProjectUser.objects.get(user=user)
            return render_to_response('project/recruit.html', {'projects': projects})
        else:
            return render_to_response('project/recruit.html', {'projects': projects})

''' 招募项目相关页面结束'''


'''个人中心相关页面'''
def homepage(req):
    if req.method == 'GET':
        return render_to_response('personal/homepage.html')
    if req.method == 'POST':
        pass

'''个人中心相关页面结束'''
