# -*- encoding:utf-8 -*-
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response,render
from . import models
from django.core.paginator import Paginator


@csrf_exempt
def label_user(req):
    if req.method == "GET":
        currentpage = 1
        userlabel = models.UserLabel.objects.all().order_by('Id')
        page = Paginator(userlabel, 6)
        userLabel = page.page(currentpage).object_list
        print(userLabel)
        return render_to_response('second/Label_User.html', {'UserLabel': userLabel})
    if req.method == "POST":
        pass

def label_project(req):
    if req.method == "GET":
        currentpage = 1
        projectlabel = models.ProjectLabel.objects.all().order_by('Id')
        page = Paginator(projectlabel, 6)
        projectLabel = page.page(currentpage).object_list
        return render_to_response('second/Label_Project.html', {'ProjectLabel ': projectLabel})
    if req.method == "POST":
        pass
# # Create your views here.
#
# def loginCheck(req):
#     '''
#     登陆状态验证
#     :param req:
#     :return: 验证失败直接调转登陆界面，成功则继续执行
#     '''
#     if req.session.get('account') == None:
#         return render(req, '/exAdmin/login.html')
#     else:
#         pass
#
#
# @csrf_exempt
# def login(req):
#     if req.method == "GET":
#         if req.session.get('account') == None:
#             return render_to_response('exAdmin/login.html')
#         else:
#             return render_to_response('second/User_detail.html')
#     if req.method == "POST":
#         result = {}
#         account = req.POST["account"].lower().strip()
#         password = req.POST["password"]
#         if models.Admin.objects.filter(Account=account):
#             user = models.Admin.objects.get(Account=account)
#             if user.Password == password:
#                 result['status'] = 1
#                 req.session['account'] = account
#                 result['account'] = account
#                 result['message'] = '登陆成功'
#                 return HttpResponse(json.dumps(result), content_type="application/json")
#             elif user.Password != password:
#                 result['status'] = 0
#                 result['message'] = '用户名或密码错误'
#                 return HttpResponse(json.dumps(result), content_type="application/json")
#         else:
#             result['status'] = 0
#             result['message'] = '用户名或密码错误'
#             return HttpResponse(json.dumps(result), content_type="application/json")
#
#
# def logout(req):
#     '''
#     注销
#     :param req:
#     :return: login.html
#     '''
#     if req.method == "GET":
#         if req.session.get('account') == None:
#             pass
#         else:
#             del req.session['account']
#         response = render_to_response('first/login.html')
#         if req.COOKIES.get('account'):
#             response.delete_cookie('account')
#         else:
#             pass
#         return render_to_response('first/login.html')
#     if req.method == "POST":
#         pass
#
#
# @csrf_exempt
# def score_rank(req):
#     if req.method == "GET":
#         if "id" in req.GET:
#             id = req.GET["id"]
#             try:
#                 models.Score.objects.get(pk=id).delete()
#                 return HttpResponse("删除成功")  # 删除成功
#             except Exception as e:
#                 print(e)
#                 return HttpResponse("数据异常，请刷新后重试")
#         else:
#             currentpage = 1
#             dataperpage = 6
#             scoreRank = models.Score.objects.all().order_by('-Id')
#             page = Paginator(scoreRank, dataperpage)
#             scoreRank = page.page(currentpage).object_list
#
#             L = []
#             for i in range(0, scoreRank.count()):
#                 info = {}
#                 info["num"] = i + 1
#                 info["score"] = scoreRank[i]
#                 L.append(info)
#
#             return render_to_response('second/Score_rank.html', {'L': L })
#     if req.method == "POST":
#         id = req.POST["id"]
#         Level = req.POST["Level"]
#         Value = req.POST["Value"]
#
#         score = models.Score.objects.filter(pk=id)
#         if score.exists():
#             score = score[0]
#         else:
#             score = models.Score()
#
#         score.Level = Level
#         score.Value = Value
#
#         try:
#             score.save()
#
#             if id == "0":
#                 return HttpResponse("保存成功")
#             else:
#                 return HttpResponse("修改成功")
#         except Exception as e:
#             print(e)
#             return HttpResponse("数据异常，请刷新后重试")
#
#
#
# @csrf_exempt
# def score_user(req, page):
#     if req.method == "GET":
#         currentpage = int(page)
#         try:
#             record_per_page = int(req.COOKIES.get('record_per_page'))
#         except:
#             record_per_page = 6
#         scoreUser = models.User.objects.all().order_by('Id')
#         scoreUser_count = models.User.objects.count()
#         page = Paginator(scoreUser, record_per_page)
#         scoreUser = page.page(currentpage).object_list
#         return render_to_response('second/User_score.html', {'ScoreUser': scoreUser, 'count': scoreUser_count})
#     if req.method == "POST":
#         result = {}
#         if req.session.get('account') == None:
#             result['message'] = '无权访问'
#             return HttpResponse(result['message'])
#         else:
#             try:
#                 data = req.POST
#
#             except:
#                 result['message'] = '获取数据异常'
#                 return HttpResponse(result)
#             else:
#                 if data['search']:
#                     return HttpResponse(data['search'])
#                 else:
#                     return HttpResponse('Baddata')
#
#
#
#
# @csrf_exempt
# def score_record(req):
#     if req.method == "GET":
#         if "id" in req.GET:
#             id = req.GET["id"]
#             try:
#                 models.ScoreChange.objects.get(pk=id).delete()
#                 return HttpResponse("删除成功")
#             except Exception as e:
#                 print(e)
#                 return HttpResponse("数据异常，请刷新后重试")
#         else:
#             currentpage = 1
#             scoreChanges = models.ScoreChange.objects.all().order_by('Id')
#             users = models.User.objects.all()
#             scores = models.Score.objects.all()
#
#             page = Paginator(scoreChanges, 6)
#             scoreChanges = page.page(currentpage).object_list
#
#             L = []
#             for i in range(0, scoreChanges.count()):
#                 info = {}
#                 info["num"] = i + 1
#                 info["scoreChange"] = scoreChanges[i]
#                 L.append(info)
#
#             return render_to_response('second/Score_record.html', {
#                 'L': L, "users": users, "scores": scores
#             })
#     if req.method == "POST":
#         id = req.POST["id"]
#         user = req.POST["user"]
#         score = req.POST["score"]
#         Event = req.POST["Event"]
#
#         score_change = models.ScoreChange.objects.filter(pk=id)
#         if score_change.exists():
#             score_change = score_change[0]
#         else:
#             score_change = models.ScoreChange()
#
#         score_change.user_id = user
#         score_change.score_id = score
#         score_change.Event = Event
#
#         try:
#             score_change.save()
#             if id != "0":
#                 return HttpResponse("创建成功")
#             else:
#                 return HttpResponse("修改成功")
#         except Exception as e:
#             print(e)
#             return HttpResponse("数据异常，请刷新后重试")
#
#
# @csrf_exempt
# def UserManager(req):
#     Users = models.User.objects.all().order_by('Id')
#     UsersList = []
#     for user in Users:
#         OneUser = {}
#         OneUser["UserName"] = user.UserName
#         OneUser["Sex"] = user.Sex
#         OneUser["RegistTime"] = str(user.RegistTime)
#         OneUser["Score"] = user.Score
#         UsersList.append(OneUser)
#     return HttpResponse(json.dumps(UsersList))
#
# @csrf_exempt
# def index(req):
#     return render_to_response('base/Base.html')
#

