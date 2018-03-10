# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from . import models
import json
import math
import uuid
import time
import datetime


from django.forms import forms
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse, Http404, render_to_response,HttpResponseRedirect,redirect
from django.http import JsonResponse
from django.views.generic.edit import DeleteView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.conf.urls import handler404, handler500, handler403
from django.views.decorators.http import require_http_methods
from .admin_utils import check_login
from django.template import RequestContext
from django.db.models import Q
from django.utils.html import escapejs
from django.core.urlresolvers import reverse


''' 新后台相关页面视图 '''
@require_http_methods(["GET", "POST"])
def page_not_found(request):
    response = render_to_response('/base/404.html', context=RequestContext(request))
    response.status_code = 404
    return response

@require_http_methods(["GET", "POST"])
def permition_denied(request):
    response = render_to_response('/base/500.html', context=RequestContext(request))
    response.status_code = 500
    return response

@require_http_methods(["GET", "POST"])
@csrf_exempt
def login(req):
    if req.method == "GET":
        return render(req, 'admina/login.html')
    if req.method == "POST":
        account = req.POST["account"]
        passwd = req.POST["passwd"]

        responseData = {
            "status": 0,
            "message": ""
        }

        try:
            admin = models.Admin.objects.get(Account=account)
        except Exception as e:
            print(e)
            responseData["status"] = 0
            responseData["message"] = "用户名或密码错误"
            return HttpResponse(json.dumps(responseData))
        else:
            if admin.Password == passwd:
                responseData["status"] = 1
                responseData["message"] = "登陆成功"
                admin.Uuid = uuid.uuid1()
                admin.save()
                req.session["admin_uuid"] = str(admin.Uuid)
                response = HttpResponse(json.dumps(responseData))
                response.set_cookie('admin_account', admin.Account)
                return response
            else:
                responseData["status"] = 0
                responseData["message"] = "用户名或密码错误"
                return HttpResponse(json.dumps(responseData))

@require_http_methods(["GET"])
@check_login()
@csrf_exempt
def logout(req):
    responseData = {
        'status': 1,
        'message': 'success'
    }
    try:
        del req.session["admin_uuid"]
        response = HttpResponse(json.dumps(responseData))
        response.set_cookie('admin_account', None)
        return response
    except Exception as e:
        print(e)
        responseData['status'] = 0
        responseData['message'] = str(e)
        return HttpResponse(json.dumps(responseData))


# 用户管理
@csrf_exempt
@check_login()
@require_http_methods(["GET", "POST"])
def index(req):
    if req.method == "GET":
        return render(req, 'admina/index.html')
    if req.method == "POST":
        pass


@csrf_exempt
@check_login()
@require_http_methods(["GET", "POST"])
def user_add(req):
    if req.method == "GET":
        userLabels = models.UserLabel.objects.filter(IsUse=True)
        return render(req, 'admina/user_add.html', {
            'UserLabels': userLabels
        })
    else:
        resData = {
            "status": 0,
            "message": ""
        }
        # 获取传入数据
        postData = req.POST
        user_name = postData.get('user_name')
        user_account = postData.get('user_account')
        user_identity = postData.get('user_identity')
        user_passwd = postData.get('user_passwd')
        user_email = postData.get('user_email')
        user_sex = postData.get('user_sex')
        user_school = postData.get('user_school')
        user_institutde = postData.get('user_institutde')
        user_major = postData.get('user_major')
        user_tags = postData.get('Tags').split(',')
        user_introduction  = postData.get('user_introduction')

        if req.FILES:
            user_img = req.FILES.get('Img')
        else:
            user_img = None

        try:
            user = models.User.objects.create(
                UserName=user_name,
                Account=user_account,
                PassWord=user_passwd,
                Identity=user_identity,
                Sex=user_sex,
                Email=user_email,
                Img=user_img,
                Introduction=user_introduction,
                School=user_school,
                Institude=user_institutde,
                Major=user_major
            )
            user.save()
            for label in user_tags:
                user_label = models.UserLabel.objects.get(Id=label)
                user2userlabel = models.User2UserLabel.objects.create(
                    user=user,
                    userLabel=user_label,
                    Uuid=uuid.uuid4()
                )
                user2userlabel.save()
            resData['status'] = 1
            resData['message'] = 'success'
        except Exception as e:
            resData['message'] = str(e)
        return HttpResponse(JsonResponse(resData))


@csrf_exempt
@check_login()
@require_http_methods(["GET", "POST"])
def user_all(req, page=None):
    ItemPerPage = 15
    if req.method == "GET":
        user_count = models.User.objects.exclude(Q(Identity=3)).count()
        pages = math.ceil(user_count/ItemPerPage)
        if(page):
            users = models.User.objects.all()[(int(page)-1)*ItemPerPage:(int(page))*ItemPerPage]
        else:
            users = models.User.objects.all()[0:ItemPerPage]
        return render(req, 'admina/user_all.html', {"users": users, 'pages': range(1, int(pages)+1)})
    else:
        deleteId = req.POST['deleteId']
        resData = {
            "status": 0,
            "message": ""
        }
        try:
            print("try to delete user with id= " + deleteId)
            user = models.User.objects.get(Id=deleteId)
            user.Identity = 3
            resData['status'] = 1
            resData['message'] = 'success!'
            return HttpResponse(json.dumps(resData))
        except:
            print("Failed to delete User with id= " + deleteId)
            resData["message"] = "服务器异常"
            return HttpResponse(json.dumps(resData))
        finally:
            resData["status"] = 1
            resData["message"] = "Success"
            return HttpResponse(json.dumps(resData))


@csrf_exempt
@check_login()
@require_http_methods(["GET", "POST"])
def user_detail(req, userid=None):
    '''
    获取用户详情
    :param req:
    :param userid:
    :return:
    '''
    if req.method == "GET":
        if userid:
            print("Try to find user with Id" + userid)
            try:
                user = models.User.objects.get(Id=userid)
                user_labels = models.UserLabel.objects.all()
            except Exception as e:
                print(e)
                return render(req, 'admina/user_all.html')
            return render(req, 'admina/user_detail.html', {"user": user, "user_labels":user_labels})
            pass
        else:
            return render(req, 'admina/user_all.html')
    else:
        pass

@csrf_exempt
@check_login()
@require_http_methods(["GET", "POST"])
def user_introduction(req, uid=None):
    '''
    编辑用户自我介绍
    :param req:
    :param uid:
    :return:
    '''
    if req.method == "GET":
        if uid:
            pass
        else:
            return render(req, "admina/user_introduction.html")
    else:
        pass

@csrf_exempt
@check_login()
@require_http_methods(["GET", "POST"])
def user_timeline(req, uid=None):
    '''
    用户时间线查询 后期功能
    :param req:
    :param uid:
    :return:
    '''
    if req.method == "GET":
        if uid:
            pass
        else:
            return render(req, 'admina/user_timeline')


# 项目管理
@csrf_exempt
@check_login()
@require_http_methods(["GET", "POST"])
def project_all(req, page=None):
    if req.method == "GET":
        itemPerPage = 12
        projectCount = models.Project.objects.count()
        Pages = math.ceil(projectCount / itemPerPage)
        print("total page is " + str(Pages))

        labels = models.ProjectLabel.objects.all()

        if(page):
            projects = models.Project.objects.all()[(int(page)-1)*itemPerPage:]
        else:
            projects = models.Project.objects.all()[:itemPerPage]

        return render(req, 'admina/project_all.html', {"projects": projects, "Pages": range(1, int(Pages+1)),"Labels": labels})
    else:
        resData = {
            "ProjectName": "",
            "ProjsctStartTime": "",
            "ImgPath": "",
            "ProjectStatue":0,
            "ProjectUserNumber": 0,
            "projectUserId": "",
            "projectUserName": "",

            "status":0,
            "message":""
        }

        projectId = req.POST["projectId"]
        try:
            project = models.Project.objects.get(Id=projectId)
            resData["ProjectName"] = project.ProjectName
            resData["ProjsctStartTime"] = project.StartTime.strftime("%Y-%m-%d")
            resData["ImgPath"] = str(project.Img)
            resData["ProjectStatue"] = project.Statue
            resData["ProjectUserNumber"] = project.Number
            if(models.ProjectUser.objects.filter(Q(project=project) & Q(Identity=3))):
                resData["projectUserName"] = models.ProjectUser.objects.filter(Q(project=project) & Q(Identity=3))[0].user.UserName
                resData["projectUserId"]  = models.ProjectUser.objects.filter(Q(project=project) & Q(Identity=3))[0].user.Id

            resData["status"] = 1
            resData["message"] = "Success"
        except Exception as e:
            print(e)
            resData["message"] = "服务器异常"
            resData["status"] = 0
        finally:
            return HttpResponse(json.dumps(resData))

@csrf_exempt
@check_login()
@require_http_methods(["POST"])
def project_delete(req, deleteId):
    resData = {
        "status": 0,
        "message":""
    }
    try:
        print("Try to delete Project with ID " + deleteId)
        models.Project.objects.get(Id=deleteId).delete()
        resData["message"] = "Success"
        resData["status"] = 1
    except Exception as e:
        resData["message"] = "服务器异常"
        resData["status"] = 0
    finally:
        return HttpResponse(json.dumps(resData))


@csrf_exempt
@check_login()
@require_http_methods(["GET", "POST"])
def project_add(req):
    '''
    项目添加页面
    :param req:
    :return:
    '''
    if req.method == "GET":
        if req.COOKIES.get('1111'):
            2333333333
        else:
            return login(req)
        projectLabels = models.ProjectLabel.objects.all().order_by("-Id")
        user = models.User.objects.all()
        return render(req, 'admina/project_add.html', {
            "ProjectLabels": projectLabels,
            "users": user,
        })
    else:
        resData = {
            'status': 0,
            'message': ''
        }

        post_data = req.POST
        project_name = post_data.get('project_name')
        poject_start_time = post_data.get('project_start_time')
        project_status = post_data.get('project_status')
        project_end_time = post_data.get('project_end_time')
        project_predict_number = post_data.get('predict_number')
        project_user_id = post_data.get('project_user')
        project_tags = post_data.get('Tags')

        # 处理数据

        poject_start_time = poject_start_time.split('-')
        poject_start_time = datetime.datetime(
            int(poject_start_time[0]),
            int(poject_start_time[1]),
            int(poject_start_time[2]))
        project_end_time = project_end_time.split('-')
        project_end_time = datetime.datetime(
            int(project_end_time[0]),
            int(project_end_time[1]),
            int(project_end_time[2]))

        if req.FILES:
            project_img = req.FILES.get('Img')
        else:
            project_img = None
        if project_tags:
            project_tags = project_tags.split(',')
        else:
            project_tags = []
        project_introduction = post_data.get('project_introduction')
        project_process = post_data.get('project_process')
        project_summary = post_data.get('project_summary')

    try:
        user = models.User.objects.get(Id=project_user_id)
        project = models.Project.objects.create(
            ProjectName=project_name,
            Description=project_introduction,
            StartTime=poject_start_time,
            EndTime=project_end_time,
            Statue=project_status,
            Number=project_predict_number,
            Img=project_img,
            Summary=project_summary,
            Progress=project_process,
            Uuid=uuid.uuid4()
        )
        project.save()
        project_user = models.ProjectUser.objects.create(
            user=user,
            project=project,
            Identity=1,
            Uuid=uuid.uuid4()
        )
        project_user.save()

        resData['status'] = 1
        resData['message'] = 'success'
    except Exception as e:
        print e
        resData['message'] = str(e)
    return HttpResponse(JsonResponse(resData))


@csrf_exempt
@check_login()
@require_http_methods(["GET", "POST"])
def project_detail(req, id=None):
    if req.method == "GET":
        if id:
            try:
                users = models.User.objects.all()
                projectLabels = models.ProjectLabel.objects.all()
                project = models.Project.objects.get(Id=id)
                project_user = models.ProjectUser.objects.filter(project=project, Identity=1) or None # 这里的身份后期要改为 1 目前好多项目的项目用户不存在
                return render(req, 'admina/project_detail.html', {
                    'project': project,
                    'users': users,
                    'ProjectLabels': projectLabels,
                    'project_user': project_user
                })
            except Exception as e:
                print(e)
                return redirect(reverse('admina:project_all', args=(1,)))
        else:
            return redirect(reverse('admina:project_all', args=(1,)))
    else:
        pass


@csrf_exempt
@check_login()
@require_http_methods(["GET", "POST"])
def project_recmanage(req, uid=None):
    '''
    招募
    :param
    :return:
    '''
    if req.method == "GET":
        if uid:
            pass
        else:
            return render(req, "admina/project_recmanage.html")
    else:
        pass


@csrf_exempt
@check_login()
@require_http_methods(["GET", "POST"])
def project_recruit(req, uid=None):
    '''
    招募表管理，若 uid 存在为修改，否则为创建
    :param req:
    :param uid:
    :return:
    '''
    if req.method == "GET":
        if uid:
            pass
        else:
            try:
                projects = models.Project.objects.all()
            except Exception as e:
                print(e)
                projects = None
            return render(req, "admina/project_recruit.html",{
                'Projects': projects
            })
    else:
        # uid 不存在未新建， uid存在为修改
        if uid:
            pass
        else:
            resData = {
                "status": 1,
                "message": ""
            }
            data = req.POST
            recruit_project_id = data.get('recruit_project')
            recruit_start_time = data.get('recruit_start_time')
            recruit_state = data.get('recruit_state')
            recruit_end_time = data.get('recruit_end_time')
            is_use = data.get('is_use')
            recruit_predict_number = data.get('recruit_predict_number')
            recruit_number = data.get('recruit_number')
            recruit_describe = data.get('recruit_describe')

            try:
                recruit_project = models.Project.objects.get(Id=recruit_project_id)

                if recruit_start_time:
                    recruit_start_time = recruit_start_time.split('-')
                    recruit_start_time = datetime.datetime(
                        int(recruit_start_time[0]),
                        int(recruit_start_time[1]),
                        int(recruit_start_time[2]),
                    )
                else:
                    recruit_start_time = None
                if recruit_end_time:
                    recruit_end_time = recruit_start_time.split('-')
                    recruit_end_time = datetime.datetime(
                        int(recruit_end_time[0]),
                        int(recruit_end_time[1]),
                        int(recruit_end_time[2]),
                    )
                else:
                    recruit_end_time = None

                recruit = models.Recruit.objects.create(
                    project=recruit_project,
                    StartTime=recruit_start_time,
                    EndTime=recruit_end_time,
                    Describe=recruit_describe,
                    Times=recruit_state,
                    State=is_use,
                    PredictNumber=recruit_predict_number,
                    RecruitedNumber=recruit_number
                )
                recruit.save()
                resData['status'] = 1
                resData['message'] = 'success'

            except Exception as e:
                print(e)
                resData['message'] = str(e)
            return HttpResponse(JsonResponse(resData))


# 标签管理
@csrf_exempt
@check_login()
@require_http_methods(["GET", "POST"])
def label_project(req, uid=None):
    """
    添加项目标签
    :param req: 
    :param uid: 
    :return: 
    """
    if req.method == "GET":
        Labels = models.ProjectLabel.objects.all().order_by('-Id')
        return render(req, 'admina/label_project.html', {
            'Labels': Labels
        })
    if req.method == 'POST':
        lableId = req.POST['lableId']
        lableName = req.POST['lableName']
        isUse = req.POST['isUse']
        if isUse == '可用':
            isUse = True
        else:
            isUse = False
        try:
            existingLable = models.ProjectLabel.objects.filter(Id=lableId)
            print existingLable
            if existingLable:
                models.ProjectLabel.objects.filter(Id=lableId).update(ProjectLabelName=lableName, IsUse=isUse)
                data = 0       # 0;修改标签
            else:
                models.ProjectLabel.objects.create(ProjectLabelName=lableName, IsUse=isUse)
                data = 1       # 1：添加标签
        except Exception as e:
            print (e)
            data = -1
        finally:
            return HttpResponse(data)


@csrf_exempt
def deleteProjectLable(req):
    """
    删除项目标签
    :param req: 
    :return: 
    """
    if req.method == 'POST':
        try:
            ProjectLabelName = req.POST['lableName']
            ProjectLabel = models.ProjectLabel.objects.get(ProjectLabelName=ProjectLabelName)
            ProjectLabel.IsUse = False
            ProjectLabel.save()
            data = 1
        except Exception as e:
            print (e)
            data = -1
        finally:
            return HttpResponse(data)




@csrf_exempt
@check_login()
@require_http_methods(["GET", "POST"])
def label_user(req, uid=None):
    """
    添加个人标签
    :param req: 
    :param uid: 
    :return: 
    """
    if req.method == "GET":
        Labels = models.UserLabel.objects.all().order_by("-Id")
        ProjectLabels = models.ProjectLabel.objects.all().order_by("-Id")
        return render(req, 'admina/label_user.html', {
            'Labels': Labels,
            'ProjectLabels': ProjectLabels,

        })
    if req.method == 'POST':
        lableId = req.POST['lableId']
        lableName = req.POST['lableName']
        isUse = req.POST['isUse']
        ProjectLabelName = req.POST['projectLabel']
        if isUse == '可用':
            isUse = True
        else:
            isUse = False
        try:
            existingLable = models.UserLabel.objects.filter(Id=lableId)
            projectLabel = models.ProjectLabel.objects.filter(ProjectLabelName=ProjectLabelName)[0]
            if existingLable:
                models.UserLabel.objects.filter(Id=lableId).update(projectLabel=projectLabel, IsUse=isUse, Name=lableName)
                data = 0        # 0：修改标签
            else:
                models.UserLabel.objects.create(projectLabel=projectLabel, IsUse=isUse, Name=lableName)
                data = 1        # 1: 添加标签成功
        except Exception as e:
            print(e)
            data = -1       # -1: 添加标签失败
        return HttpResponse(data)


@csrf_exempt
def deleteUserLable(req):
    """
    删除个人标签
    :param req: 
    :return: 
    """
    if req.method == 'POST':
        try:
            lableName = req.POST['lableName']
            Lable = models.UserLabel.objects.get(Name=lableName)
            Lable.IsUse = False
            Lable.save()
            data = 1    # 删除成功
        except Exception as e:
            print (e)
            data = -1   # 删除失败
        finally:
            return HttpResponse(data)




#  创意管理
@check_login()
@require_http_methods(["GET", "POST"])
@csrf_exempt
def creation_all(req, page=1, category=None):
    '''
    :param page: 当前查询创意的页数
    '''
    page = int(page) or 1
    if req.method == "GET":
        itemsPerPage = 18
        pages = math.ceil(float(models.Creation.objects.count()) / float(itemsPerPage))# 计算页数
        print pages
        Labels = models.ProjectLabel.objects.all()
        Creations = models.Creation.objects.all()[(page-1)*itemsPerPage:page*itemsPerPage]
        return render(req, 'admina/creation_all.html', {
            "Labels": Labels,
            "category": category,
            "pages": range(1, int(int(pages) + 1)),
            "Creations": Creations
        })
    else:
        resData = {
            "status": 0,
            "message": "",
            "creationImg": None,
            "creationName": None,
            "creationUserName": None,
            "creationUserId": None
        }
        try:
            creationId = req.POST["creationId"]
            creation = models.Creation.objects.get(Id=creationId)
            resData["status"] = 1
            resData["creationImg"] = creation.Img.url
            resData["creationName"] = creation.Name
            resData["creationUserName"] = creation.user.UserName
            resData["creationUserId"] = creation.user.Id
            resData["creationContent"] = creation.Describe
        except Exception as e:
            print(e)
            resData["message"] = "获取数据异常"
        return HttpResponse(JsonResponse(resData)) # 诡异，去掉HttpResponse就不行,好像是因为默认编码的问题


@csrf_exempt
@check_login()
@require_http_methods(["GET", "POST"])
def creation_category(req, page):
    '''
    创意分类视图
    :param reqm:
    :param page:
    :return: Html to creation with specified category
    '''
    if req.method == "GET":
        if not page:
            return render(req, 'admina/creation_all.html')
        else:
            return render(req, 'admina/creation_all.html')
    else:
        return render(req, 'admina/creation_all.html')


@csrf_exempt
@check_login()
@require_http_methods(["GET", "POST"])
def creation_add(req, uid=None):
    '''
    创意添加，暂时没有处理上传文件的格式
    :param req:
    :param uid:
    :return:
    '''
    if req.method == "GET":
        users = models.User.objects.all().order_by("UserName")
        labels = models.ProjectLabel.objects.all()
        if uid:
            pass
        else:
            return render(req, 'admina/creation_add.html', {
                "labels": labels,
                "users": users,

            })
    else:
        resData = {
            "status": 0,
            "message": ""
        }
        try:
            data = req.POST
            print data.get('creation_user')
            creation_user_id = data.get('creation_user')
            print data.get('creation_init_time')
            creatino_init_time = data.get('creation_init_time')
            print creatino_init_time
            creation_is_use = data.get('IsUse')
            creatino_init_time = data.get('creation_init_time')
            creation_name = escapejs(data.get('creation_name'))
            creation_tagids = data.get(u'Tags')
            creation_descibe = data.get(u'creation_descibe')
            print creation_tagids
            print locals()
            if(req.FILES):
                creation_img = req.FILES.get('Img')
            else:
                creation_img = None
            if creatino_init_time:
                creatino_init_time = creatino_init_time.split('-')
                creatino_init_time = datetime.datetime(
                    int(creatino_init_time[0]),
                    int(creatino_init_time[1]),
                    int(creatino_init_time[2]))
            else:
                creatino_init_time = datetime.datetime.now()
            if int(creation_is_use) == 1:
                creation_is_use = False
            else:
                creation_is_use = True
            user = models.User.objects.get(Id=creation_user_id)
            creation = models.Creation.objects.create(
                user=user,
                IsUse=creation_is_use,
                Date=creatino_init_time,
                Name=creation_name,
                Img=creation_img,
                Describe=creation_descibe
            )
            creation.save()
            for tagid in creation_tagids.split(','):
                tag = models.ProjectLabel.objects.get(Id=tagid)
                creation2ProjectLabel = models.Creation2ProjectLabel.objects.create(creation=creation, projectLabel=tag)
                creation2ProjectLabel.save()
            resData['message'] = '创建成功'
            resData['status'] = 1
        except Exception as e:
            print(e)
            resData['message'] = str(e)
        return HttpResponse(JsonResponse(resData))

@csrf_exempt
@check_login()
@require_http_methods(["POST"])
def creation_delete(req):
    '''
    删除创意,将IsUse状态置为False
    :param req:
    :return:
    '''
    resData = {
        "status": 0,
        "message": ""
    }
    try:
        creationId = req.POST['creationId']
        creation = models.Creation.objects.get(Id=creationId)
        creation.IsUse = False
        creation.save()
        resData["status"] = 1
        resData["message"] = "Success"
    except Exception as e:
        print(e)
        resData["message"] = "服务器异常！"
    finally:
        return JsonResponse(resData)

@csrf_exempt
@check_login()
@require_http_methods(["POST"])
def creation_modify(req):
    '''
    创意修改
    :param req:
    :return: Json 信息
    '''
    resData = {
        "status": 0,
        "message": ""
    }
    try:
        creationId = req.POST["creationId"]
        creationName = escapejs(req.POST["creationName"])
        creationDesc = escapejs(req.POST["creationDesc"])
        creation = models.Creation.objects.get(Id=creationId)
        creation.Describe = creationDesc
        creation.Name = creationName
        creation.save()
        resData["status"] = 1
        resData["message"] = "success!"
    except Exception as e:
        print(e)
        resData["message"] = "服务器异常!"
    return JsonResponse(resData)

# 举报管理相关视图
@csrf_exempt
@check_login()
@require_http_methods(["GET", "POST"])
def report_comment(req):
    '''
    评论举报相关视图
    :param req:
    :return:
    '''
    if req.method == "GET":
        return render(req, 'admina/report_comment.html')
    else:
        pass

@csrf_exempt
@check_login()
@require_http_methods(["GET", "POST"])
def report_creation(req):
    '''
    创意举报相关视图
    :param req:
    :return:
    '''
    if req.method == "GET":
        return render(req, 'admina/report_creation.html')
    else:
        pass


@csrf_exempt
@check_login()
@require_http_methods(["GET", "POST"])
def report_user(req):
    '''
    用户举报相关视图
    :param req:
    :return:
    '''
    if req.method == "GET":
        return render(req, 'admina/report_user.html')
    else:
        pass

@csrf_exempt
@check_login()
@require_http_methods(["GET", "POST"])
def report_project(req):
    '''
    项目举报相关视图
    :param req:
    :return:
    '''
    if req.method == "GET":
        return render(req, 'admina/report_project.html')
    else:
        pass

# 评论管理相关视图
@csrf_exempt
@check_login()
@require_http_methods(["GET", "POST"])
def comment_statistic(req):
    '''
    用于显示评论统计状况的视图
    :param req:
    :return:
    '''
    if req.method == "GET":
        return render(req, 'admina/comment_all.html')
    else:
        pass

@csrf_exempt
@check_login()
@require_http_methods(["GET", "POST"])
def comment_creation(req):
    '''
    用于显示评论统计状况的视图
    :param req:
    :return:
    '''
    if req.method == "GET":
        Comments = models.Comment.objects.all().order_by('-Id')
        return render(req, 'admina/comment_creation.html', {"Comments": Comments})
    else:
        pass


@csrf_exempt
def deletecreation(req):
    """
    删除创意评论
    :param req: 
    :return: 
    """
    if req.method == 'POST':
        try:
            creation_comment = req.POST['creation_comment']
            creationcomment = models.Comment.objects.get(Id=creation_comment)
            print(creationcomment)
            creationcomment.IsUse = False
            creationcomment.save()
            data = 1
        except Exception as e:
            print (e)
            data = -1
        finally:
            return HttpResponse(data)

@csrf_exempt
@check_login()
@require_http_methods(["GET", "POST"])
def comment_project(req):
    '''
    用于显示评论统计状况的视图
    :param req:
    :return:
    '''
    if req.method == "GET":
        Comments = models.Comment.objects.all().order_by('-Id')
        return render(req, 'admina/comment_project.html', {"Comments": Comments})
    if req.method == 'POST':
        isUse = req.POST['isUse']
        project_comment_id = req.POST['project_comment_id']
        if isUse == '可用':
            isUse = True
        else:
            isUse = False
        try:
            project_comment = models.Comment.objects.filter(Id=project_comment_id)
            if project_comment:
                models.Comment.objects.filter(Id=project_comment_id).update(IsUse=isUse)
                data = 0  # 0：修改项目评论状态
            else:
                data = 1  # 1: 不存在此项目
        except Exception as e:
            print(e)
            data = -1  # -1: 失败
        return HttpResponse(data)


@csrf_exempt
def deleteComment(req):
    """
    删除项目评论
    :param req: 
    :return: 
    """
    if req.method == 'POST':
        try:
            project_comment = req.POST['project_comment']
            Projectcomment = models.Comment.objects.get(Id=project_comment)
            print(Projectcomment.user.UserName)
            Projectcomment.IsUse = False
            Projectcomment.save()
            data = 1
        except Exception as e:
            print (e)
            data = -1
        finally:
            return HttpResponse(data)



@csrf_exempt
def show_project_comment(req):
    '''
    展示项目评论的变化状态
    :param req:
    :return:
    '''
    Comments = models.Comment.objects.all().order_by('-Id')
    status = []
    for i in Comments:
        ss = i.project
        comment_isuse = i.IsUse
        if ss:
            if comment_isuse == True:
                list = {}
                list['UserName'] = i.user.UserName
                list['ProjectName'] = i.project.ProjectName
                list['IsUse'] = "可用"
                list['Content'] = i.Content
                list['Id'] = i.Id
                status.append(list)
            else:
                list = {}
                list['UserName'] = i.user.UserName
                list['ProjectName'] = i.project.ProjectName
                list['IsUse'] = "不可用"
                list['Content'] = i.Content
                list['Id'] = i.Id
                status.append(list)
    return HttpResponse(json.dumps(status))




@csrf_exempt
@check_login()
@require_http_methods(["GET", "POST"])
def comment_user(req):
    '''
    用于显示评论统计状况的视图
    :param req:
    :return:
    '''
    if req.method == "GET":
        return render(req, 'admina/creation_user.html')
    else:
        pass

# 分值管理相关视图
@csrf_exempt
@check_login()
@require_http_methods(["GET", "POST"])
def score_rank(req):
    if req.method == "GET":
        ranks = models.Score.objects.all().order_by("-Id")
        return render(req, 'admina/score_rank.html', {
            "Ranks": ranks,

        })
    else:
        pass

@csrf_exempt
@check_login()
@require_http_methods(["GET", "POST"])
def score_record(req):
    if req.method == "GET":
        return render(req, 'admina/score_record.html', {

        })
    else:
        pass


# 关系管理相关视图
@csrf_exempt
@check_login()
@require_http_methods(["GET", "POST"])
def relation_praise(req):
    '''
    点赞管理相关视图， 对应 model ：Praise
    :param req:
    :return:
    '''
    if req.method == "GET":
        return render(req, 'admina/relation_praise.html', {})
    else:
        pass

@csrf_exempt
@check_login()
@require_http_methods(["GET", "POST"])
def relation_attention(req):
    '''
    关注管理相关视图， 对应 model : Fellow
    :param req:
    :return:
    '''
    if req.method == "GET":
        return render(req, 'admina/relation_attention.html', {})
    else:
        pass


# 消息管理相关视图
@csrf_exempt
@check_login()
@require_http_methods(["GET", "POST"])
def message_type(req):
    if req.method == "GET":
        return render(req, 'admina/message_type.html', {})
    else:
        pass
@csrf_exempt
@check_login()
@require_http_methods(["GET", "POST"])
def message_send(req):
    if req.method == "GET":
        return render(req, 'admian/message_send.html', {})
    else:
        pass

@csrf_exempt
@check_login()
@require_http_methods(["GET", "POST"])
def message_manage(req):
    if req.method == "GET":
        return render(req, 'admian/message_manage.html', {})
    else:
        pass

''' 将来可能弃用的代码 '''

def Profile(req):
    if req.method == "GET":
        username = 'chris'
        try:
            user = models.User.objects.get(UserName=username)
        except:
            raise Http404
        else:
            print(user.Img)
            return render(req, 'second/UserDetail.html', {"user": user})

@csrf_exempt
def PhotoGallary(req):
    if req.method == "GET":
        username = 'chris'
        try:
            user = models.User.objects.get(UserName=username)
        except:
            raise Http404
        else:
            try:
                Images = models.UserImageForge.objects.filter(user=user)
            except:
                Images = None
            else:
                return render(req, 'second/PhotoGallery.html', {'user': user,'Images': Images})
    if req.method == "POST":
        print("aa")
        result = {
            "status": 0,
            "message": ''
        }
        delete_image_id = req.POST['image_id']
        try:
            record = models.UserImageForge.objects.get(Id=delete_image_id)
        except:
            result["message"] = "服务器异常"
            return HttpResponse(json.dumps(result))
        else:
            record.delete()
            result["status"] = 1
            result["message"]="删除成功"
            return HttpResponse(json.dumps(result))



"""评论相关页面"""
"""评论相关页面"""
def comment_list(req):
    """用户相关的评论"""
    if req.method == 'GET':
        result = []
        users = models.User.objects.all()
        for user in users:
            comments = models.Comment.objects.filter(user=user)
            result.append(comments)
        result = zip(users, result)
        return render(req, 'second/UserCommentList.html',{"result":result})

