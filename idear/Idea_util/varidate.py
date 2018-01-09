# -*- coding:utf-8 -*-
import re

def varidate_char(str, max_length=20):
    '''
    非法字符验证
    :param sql:
    :param max_length:
    :return: False  表示字符串中含有非法字符    True 表示字符串中不含有非法字符
    '''
    if len(str) > max_length:
        return False
    dirty_stuff = ["\"", "\\", "/",
                   "*", "'", "=", "-",
                   "#", ";", "<", ">",
                   "+", "%", "$", "(",
                   ")", "%", "@", "!"]
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

def remove_script(value):
    '''去除文本中包含的script标签'''
    re_script = re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', re.I)
    return re_script.sub('', value)


''' 登陆状态验证 '''
from functools import wraps
from admina import models
from django.shortcuts import render

def user_must_login():
    '''
    检测登陆状态的装饰器,通过 session 获取用户 UUID 和 Email
    :return:
    '''
    def decorator(func):
        @wraps(func)
        def inner(request, *args, **kwargs):
            try:
                user_uuid = request.session.get("user_uuid")
                user_email = request.session.get("user_email")
                if user_email and user_uuid:
                    user = models.User.objects.get(Uuid=user_uuid)
                    print(user.UserName + "login Successfully")
                else:
                    raise ValueError('用户验证失败')
            except Exception as e:
                print(e)
                return render(request, 'idea/index.html')
            else:
                return func(request, *args, **kwargs)
        return inner
    return decorator

