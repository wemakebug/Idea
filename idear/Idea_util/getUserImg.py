# -*- coding:utf-8 -*-
from django.http import HttpResponse, Http404
import json
from admina import models
def get_user_img(req):
    '''
    动态获取用户图片
    :param req:
    :return:
    '''
    if req.method == "GET":
        return Http404
    elif req.method == "POST":
        result = {
            'status': 0,
            'message': None,
            'img_path': None,
        }
        try:
            email = req.COOKIES.get('email')
            print(email)
            username = req.COOKIES.get('username')
            print(username)
        except:
            result['status'] = 0
            result['message'] = '尚未登陆'
            return HttpResponse(json.dumps(result))
        else:
            try:
                user = models.User.objects.get(UserName=username)
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
                    print(img_path)
                    result['img_path'] = img_path
                except Exception as e:
                    print(e)
                    result['status'] = 1
                    result['message'] = '用户暂未上传图片'
                    img_path = 'photos/2017/09/19/user/default_cdNstvn.jpg'
                    result['img_path'] = img_path
                    return HttpResponse(json.dumps(result))
                else:
                    return HttpResponse(json.dumps(result))
