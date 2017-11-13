# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_exempt
from . import models
import json
from django.shortcuts import render, HttpResponse, Http404, render_to_response, HttpResponseRedirect
import uuid
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.conf.urls import handler404, handler500, handler403
from django.views.decorators.http import require_http_methods
from .admin_utils import check_login
from django.template import RequestContext

''' 新后台相关页面视图'''
@require_http_methods(["GET", "POST"])
def page_not_found(request):
    response = render_to_response('/base/404.html', context=RequestContext(request))
    response.status_code = 404
    return response

@require_http_methods(["GET", "POST"])
def permition_denied(request):
    response = render_to_response('/base/500.html',context=RequestContext(request))
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
        return render(req, 'admina/user_add.html')
    if req.method == "POST":
        pass


@csrf_exempt
@check_login()
@require_http_methods(["GET", "POST"])
def user_all(req):
    if req.method == "GET":
        return render(req, 'admina/user_all.html')
    else:
        pass

@csrf_exempt
@check_login()
@require_http_methods(["GET", "POST"])
def user_detail(req, uid=None):
    if req.method == "GET":
        if uid:
            pass
        else:
            return render(req, 'admina/user_detail.html')
    else:
        pass

@csrf_exempt
@check_login()
@require_http_methods(["GET", "POST"])
def user_introduction(req, uid=None):
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
    if req.method == "GET":
        if uid:
            pass
        else:
            return render(req, 'admina/user_timeline')


# 项目管理
@csrf_exempt
@check_login()
@require_http_methods(["GET", "POST"])
def project_all(req):
    if req.method == "GET":
        return render(req, 'admina/project_all.html')
    else:
        pass

@csrf_exempt
@check_login()
@require_http_methods(["GET", "POST"])
def project_add(req):
    if req.method == "GET":
        return render(req, 'admina/project_add.html')
    else:
        pass

@csrf_exempt
@check_login()
@require_http_methods(["GET", "POST"])
def project_detail(req, uid=None):
    if req.method == "GET":
        if uid:
            pass
        else:
            return render(req, 'admina/project_detail.html')
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
def projet_recruit(req, uid=None):
    if req.method == "GET":
        if uid:
            pass
        else:
            return render(req, "admina/project_recruit.html")
    else:
        pass


# 标签管理
@csrf_exempt
@check_login()
@require_http_methods(["GET", "POST"])
def label_project(req, uid=None):
    if req.method == "GET":
        if uid:
            pass
        else:
            return render(req, 'admina/label_project.html')
    else:
        pass

@csrf_exempt
@check_login()
@require_http_methods(["GET", "POST"])
def label_user(req, uid=None):
    if req.method == "GET":
        if uid:
            pass
        else:
            return render(req, 'admina/label_user.html')
    else:
        pass

@csrf_exempt
@check_login()
@require_http_methods(["GET", "POST"])
def label_relation(req, uid=None):
    if req.method == "GET":
        if uid:
            pass
        else:
            return render(req, '/admina/label_relation.html')
    else:
        pass

#  创意管理
@csrf_exempt
@check_login()
@require_http_methods(["GET", "POST"])
def creation_all(req, uid=None):
    if req.method == "GET":
        if uid:
            pass
        else:
            return render(req, 'admina/creation_all.html')
    else:
        pass

@csrf_exempt
@check_login()
@require_http_methods(["GET", "POST"])
def creation_add(req, uid=None):
    if req.method == "GET":
        if uid:
            pass
        else:
            return render(req, 'admina/creation_add.html')
    else:
        pass


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

