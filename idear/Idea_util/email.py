# -*- coding:utf8 -*-
from django.core.mail import send_mail
from django.http import HttpResponse
def Email(req):
    result = send_mail('Django邮件测试', u'请不要回复', '1337074512@qq.com', ['472303924@qq.com'], fail_silently=False)
    # 收件人为一个列表，发送成功返回状态 1
    return HttpResponse(result)
