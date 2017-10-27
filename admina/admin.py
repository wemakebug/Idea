# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
# Register your models here.

'''
将数据库字段注册到Django自带后台，方便数据添加测试
后台账号为admin 密码adminadmin
'''
admin.site.register(Admin)
admin.site.register(User)
admin.site.register(UserLabel)
admin.site.register(User2UserLabel)
admin.site.register(Project)
admin.site.register(ProjectLabel)
admin.site.register(Project2ProjectLabel)
admin.site.register(ProjectUser)
admin.site.register(Creation)
admin.site.register(Recruit)
admin.site.register(Praise)
admin.site.register(Apply)
admin.site.register(Message)
admin.site.register(Comment)
admin.site.register(Follow)
admin.site.register(Report)
admin.site.register(Score)
admin.site.register(ScoreChange)
admin.site.register(Creation2ProjectLabel)
admin.site.register(HelpApplication)
admin.site.register(UserImageForge)
