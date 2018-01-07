# -*- coding:utf-8 -*-
from django.core.files.base import ContentFile
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

# -*- coding:utf-8 -*-
import base64
import cStringIO
import PIL.Image
import datetime
def base64ToImg(base64Code ,filetype):
    '''
    转码base 生成图片，存储到文件
    :param base64code:
    :return:
    '''
    imgData = base64.b64decode(base64Code)
    leniyimg = open('123.png', 'wb')
    leniyimg.write(imgData)
    leniyimg.close()

def decode_img(img_base64, img_name,fileext):
    '''
    生成图片到内存
    :param img_base64:
    :return:
    '''
    decode_str = img_base64.decode("base64")
    rgb_img = ContentFile(decode_str, img_name + "." + fileext)
    return rgb_img


# # 以下为测试代码 暂时不用
# with open('base64.txt', 'r') as file :
#     file_content = file.read()
#     imagetype = file_content.split(',')[0]
#     imagetype = imagetype.split('/')[1].split(';')[0]
#     base64Code = file_content.split(',')[1]
#     # print base64Code
#     print decode_img(base64Code)
#     # base64ToImg(base64Code,imagetype)
