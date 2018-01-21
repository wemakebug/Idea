# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
import uuid
from django.utils import timezone
# Create your models here.
'''
外键 首单词小写，
'''

class Admin(models.Model):
    '''
    管理员表， 用作后台管理
    '''
    Id = models.AutoField(primary_key=True)
    Account = models.CharField(null=False, blank=False, unique=True, max_length=25)
    Password = models.CharField(null=False, blank=False, max_length=25)
    DateTime = models.DateTimeField(auto_now_add=True)
    Email = models.EmailField(null=True, blank=True)
    Uuid = models.UUIDField(null=True, blank=True)

    def __unicode__(self):
        return self.Account

class User(models.Model):
    '''
    用户表
    1.身份标示
        0 学生
        1 教师
        2 团队
    2.性别表示
        0 男
        1 女
    3.UUID用作登陆状态验证
    '''
    Id = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=10, null=False, unique=True)
    Account = models.CharField(max_length=20, null=True, unique=True)
    PassWord = models.CharField(max_length=20, null=False)
    Identity = models.PositiveSmallIntegerField(default=0, null=False)
    Sex = models.PositiveSmallIntegerField(default=0, null=False)
    Email = models.EmailField(null=False, max_length=32, unique=True)
    Score = models.PositiveIntegerField(default=0, null=False)
    RegistTime = models.DateTimeField(auto_now_add=True)
    Phone = models.CharField(null=True, blank=True, max_length=25)
    Img = models.ImageField(upload_to='photos/%Y/%m/%d/user', null=True, blank=True)
    Introduction = models.TextField(null=True)
    School = models.CharField(null=True, max_length=20)
    Institude = models.CharField(null=True, max_length=20)
    Major = models.CharField(null=True, max_length=20)
    Uuid = models.UUIDField(null=True, blank=True, default=str(uuid.uuid1()))

    def __unicode__(self):
        return self.UserName


class Project(models.Model):
    '''
    项目表
    1.Status 项目状态描述
        0 : 暂存
        1 初期招募
        2 正在开发
        3 二次招募
        4. 完成项目
        5 被举报不可用项目
        6 发布者删除的项目
    '''
    Id = models.AutoField(primary_key=True)
    ProjectName = models.CharField(null=False, max_length=20, unique=True)
    Description = models.TextField(null=False)
    StartTime = models.DateTimeField(auto_now_add=True)
    EndTime = models.DateTimeField(null=False)
    Statue = models.PositiveIntegerField(default=0)
    Number = models.PositiveIntegerField(default=1)
    Img = models.ImageField(upload_to='photos/%Y/%m/%d/project', null=True)
    Summary = models.TextField(null=True)
    Progress = models.TextField(null=True)
    Uuid = models.UUIDField(null=True, blank=True, default=str(uuid.uuid1()))

    def __unicode__(self):
        return self.ProjectName


class ProjectLabel(models.Model):
    '''
    项目标签表
    '''
    Id = models.AutoField(primary_key=True)
    ProjectLabelName = models.CharField(max_length=20, null=False, unique=True)
    IsUse = models.BooleanField(default=True)
    Uuid = models.UUIDField(null=True, blank=True, default=str(uuid.uuid1()))
    def __unicode__(self):
        return self.ProjectLabelName


class Project2ProjectLabel(models.Model):
    '''
    项目-项目标签表
    '''
    Id = models.AutoField(primary_key=True)
    projectLabel = models.ForeignKey(ProjectLabel, related_name='Project2ProjectLabel_ProjectLabel_set', null=False)
    project = models.ForeignKey(Project, related_name='Project2ProjectLabel_Project_set')
    Uuid = models.UUIDField(null=True, blank=True, default=str(uuid.uuid1()))

    def __unicode__(self):
        return self.projectLabel.__unicode__() + '  ' +self.project.__unicode__()


class UserLabel(models.Model):
    '''
    用户标签表
    IsUse  false 代表不可用
    '''
    Id = models.AutoField(primary_key=True)
    projectLabel = models.ForeignKey(ProjectLabel, related_name='UserLabel_Project_set')
    IsUse = models.BooleanField(default=True)
    Name = models.CharField(null=False, max_length=20, unique=True)
    Uuid = models.UUIDField(null=True, blank=True, default=str(uuid.uuid1()))

    def __unicode__(self):
        return self.Name

class User2UserLabel(models.Model):
    '''
    用户-用户标签表
    '''
    Id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='User2UserLabel_User_set')
    userLabel = models.ForeignKey(UserLabel, related_name='User2UserLabel_UserLabel_set', null=False)
    Uuid = models.UUIDField(null=True, blank=True, default=str(uuid.uuid1()))

    def __unicode__(self):
        return self.user.__unicode__() + '  '+self.userLabel.__unicode__()

class ProjectUser(models.Model):    
    '''
    项目-用户表
    1.项目用户身份状态
        0为参与者
        1为项目发起人
        2为指导教师
        3为退出状态
        4为异常状态
    '''
    Id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='ProjectUser_User_set')
    project = models.ForeignKey(Project, related_name='ProjectUser_Project_set', null=False)
    Identity = models.PositiveIntegerField(default=0)
    Evaluate = models.TextField()
    Uuid = models.UUIDField(null=True, blank=True, default=str(uuid.uuid1()))
    def __unicode__(self):
        return self.project.__unicode__()


class Creation(models.Model):
    '''
    创意表
    :IsUse 是否可用 True 为不可用 False 为可用
    '''
    Id = models.AutoField(primary_key=True)
    Date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='Creation_User_set')
    LastChange = models.DateTimeField(auto_now=True)
    Describe = models.TextField(null=True)
    Name = models.CharField(max_length=20, null=False)
    IsUse = models.BooleanField(default=True)
    Img = models.ImageField(upload_to='photos/%Y/%m/%d/user')
    Uuid = models.UUIDField(null=True, blank=True, default=str(uuid.uuid1()))

    def __unicode__(self):
        return self.Name

class Creation2ProjectLabel(models.Model):
    Id = models.AutoField(primary_key=True)
    creation = models.ForeignKey(Creation,related_name='Creation2ProjectLabel_Creation_set', null=False)
    projectLabel = models.ForeignKey(ProjectLabel, related_name='Creation2ProjectLabel_ProjectLabel_set', null=False)
    Uuid = models.UUIDField(null=True, blank=True, default=str(uuid.uuid1()))

    def __unicode__(self):
        return str(self.Id)


class Recruit(models.Model):
    '''
    招募表
    State ：
        0 可用
        1 不可用
    Times :
        1 第一次招募
        2 第二次招募
        3 招募结束
        0 招募未开始
    '''
    Id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, related_name='Recruit_Project_set', null=False)
    StartTime = models.DateTimeField(auto_now_add=True)
    EndTime = models.DateTimeField(null=True)
    Describe = models.TextField(null=False)
    State = models.PositiveIntegerField(default=0)
    Times = models.PositiveIntegerField(default=1)
    PredictNumber = models.PositiveIntegerField(default=1)
    RecruitedNumber = models.PositiveIntegerField(default=0)
    Uuid = models.UUIDField(null=True, blank=True, default=str(uuid.uuid1()))

    def __unicode__(self):
        return self.project.__unicode__()
class Praise(models.Model):
    '''
    赞扬表
    '''
    Id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='Praise_User_set', null=False)
    user_prised = models.ForeignKey(User, related_name='Praised_User_set', null=True,blank=True)
    creation = models.ForeignKey(Creation, related_name='Praise_Creation_set', null=True, blank=True)
    project = models.ForeignKey(Project, related_name='Praise_Project_set', null=True, blank=True)
    Uuid = models.UUIDField(null=True, blank=True, default=str(uuid.uuid1()))

    def __unicode__(self):

        return str(self.Id)

class Apply(models.Model):
    '''
    申请表
    '''
    Id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='Apply_User_set', null=False)
    recruit = models.ForeignKey(Recruit, related_name='Apply_Recruit_set', null=False)
    Describe = models.TextField(null=True)
    State = models.PositiveIntegerField(default=0)
    SendTime = models.DateTimeField(auto_now_add=True)
    Uuid = models.UUIDField(null=True, blank=True, default=str(uuid.uuid1()))

    def __unicode__(self):
        return self.user.__unicode__()

class MessageType(models.Model):
    '''
    消息分类
    '''
    Id = models.AutoField(primary_key=True)
    Describe = models.CharField(max_length=70, null=True, blank=True)
    Priority = models.PositiveIntegerField(default=0)
    Uuid = models.URLField(null=True, blank=True, default=str(uuid.uuid1()))

class Message(models.Model):
    '''
    消息表
    1.优先级（默认为0）
    2.消息类型（默认为0）
    '''
    Id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='Message_User_set', null=False)
    Priority = models.PositiveIntegerField(default=0)
    Type = models.PositiveIntegerField(default=0)
    Date = models.DateTimeField(auto_now_add=True)
    IsUse = models.BooleanField(default=True)
    IsRead = models.BooleanField(default=False)
    Content = models.TextField(null=False)
    Uuid = models.UUIDField(null=True, blank=True, default=str(uuid.uuid1()))

    def __unicode__(self):
        return self.user.__unicode__()



class Comment(models.Model):
    '''
    评论表
    '''
    Id = models.AutoField(primary_key=True)

    user = models.ForeignKey(User, related_name='Comment_User_set', null=False)

    creation = models.ForeignKey(Creation, related_name='Comment_Creation_set', null=True, blank=True)
    project = models.ForeignKey(Project, related_name='Comment_Project_set', null=True, blank=True)
    commited_user = models.ForeignKey(User, related_name='commited_user_set', null=True, blank=True)

    commentedId = models.UUIDField(null=True, blank=True)

    Date = models.DateTimeField(auto_now_add=True)
    Content = models.TextField()

    IsUse = models.BooleanField(default=True)
    IsAdopt = models.BooleanField(default=False)

    Isreply = models.BooleanField(default=False)
    Uuid = models.UUIDField(null=True, blank=True, default=str(uuid.uuid1()),unique=True)

    def __unicode__(self):
        return self.user.__unicode__()


class Follow(models.Model):
    '''
    关注表
    '''
    Id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='Follow_User_set', null=False)

    project = models.ForeignKey(Project, related_name='Follow_Project_set', null=True, blank=True)
    creation = models.ForeignKey(Creation, related_name='Follow_Creation_set', null=True, blank=True)
    Follower = models.ForeignKey(User, related_name='Follow_Follower_set', null=True, blank=True)

    Uuid = models.UUIDField(null=True, blank=True, default=str(uuid.uuid1()))

    def __unicode__(self):
        return self.user.__unicode__()

class Report(models.Model):
    '''
    举报表
    1.处理状态，默认为0
    '''
    Id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='Report_User_set', null=False)
    project = models.ForeignKey(Project, related_name='Report_Project_set', null=True)
    creation = models.ForeignKey(Creation, related_name='Report_Creation_set', null=True)
    comment = models.ForeignKey(Comment, related_name='Report_Comment_set', null=True)
    Reason = models.TextField()
    ReportDate = models.DateTimeField(auto_now_add=True)
    DealTime = models.DateTimeField(null=True)
    State = models.PositiveIntegerField(default=0)
    Uuid = models.UUIDField(null=True, blank=True, default=str(uuid.uuid1()))

    def __unicode__(self):
        return self.user.__unicode__()
class Score(models.Model):
    '''
    分值等级表
    1.分值等级，默认为0
    '''
    Id = models.AutoField(primary_key=True)
    Level = models.PositiveIntegerField(default=0)
    Value = models.IntegerField(null=False, default=0)
    ScoreRankName = models.CharField(null=True, max_length=15)
    Uuid = models.UUIDField(null=True, blank=True, default=str(uuid.uuid1()))


class ScoreChange(models.Model):
    '''
    分值变动记录表
    '''
    Id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='ScoreChange_User_set', null=False)
    score = models.ForeignKey(Score, related_name='ScoreChange_Score_set', null=False)
    Event = models.CharField(null=True,max_length=30)
    Date = models.DateTimeField(auto_now_add=True)
    Uuid = models.UUIDField(null=True, blank=True, default=str(uuid.uuid1()))

    def __unicode__(self):
        return self.user

class HelpApplication(models.Model):
    '''
    帮助申请表
    '''
    Id = models.AutoField(primary_key=True)
    Applier = models.ForeignKey(User, related_name='Help_App_Applier')
    AppliedTeam = models.ForeignKey(User, related_name='Help_App_Team')
    DateTime = models.DateTimeField(auto_now_add=True)
    Reply = models.TextField(blank=True, null=True)
    Describe = models.TextField(null=True, blank=True)
    WhatWant = models.TextField(null=True,blank=True)
    Email = models.EmailField(null=False)
    IsReplied = models.BooleanField(default=False, blank=True)
    Uuid = models.UUIDField(null=True, blank=True, default=str(uuid.uuid1()))

    def __unicode__(self):
        return str(self.Id)


class UserImageForge(models.Model):
    '''
    用户图片仓库字段，用于富文本编辑器的文件上传功能的实现
    '''
    Id = models.AutoField(primary_key=True)
    Img = models.ImageField(upload_to='photos/user/', null=True, blank=True)
    IsUse = models.BooleanField(default=True)
    UploadDate = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name="UserImageForge_User_set")

    def __unicode__(self):
            return str(self.user.__unicode__())