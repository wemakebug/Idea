# -*- coding:utf-8 -*-
"""Idea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from idear import views as views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^login$', views.login),
    url(r'^regist$', views.regist),
    url(r'^inCode$', views.inCode),
    url(r'^team$', views.team),
    # url(r'^team_history_project$', views.team_history_project),
    url(r'^praise$',views.creations),
    url(r'^teamdetails/(?P<teamid>\d+)/$', views.teamdetails),
    url(r'^teamhelpapplication/(?P<teamhelpid>\d+)$', views.teamhelpapplication),
    url(r'^creations$', views.creations),
    url(r'^forgetPassword$', views.forgetPassword),
    url(r'^obtainVerify$', views.obtainVerify),
    url(r'^homepage$', views.homepage),
    url(r'^unread_messages$', views.unread_messages),
    url(r'^show_messages$', views.show_messages),
    url(r'^unread_read$', views.unread_read),
    url(r'^read_message$', views.read_message),
    url(r'^allFollow$',views.allFollow),
    url(r'^profollow$',views.profollow),
    url(r'^creationfollow$',views.creationfollow),
    url(r'^userfollow$',views.userfollow),
    url(r'^following_user$',views.following_user),
    url(r'^follower_user$',views.follower_user),
    url(r'^editprofile$',views.editprofile),

    url(r'^apply$', views.apply),

    url(r'^project$', views.projects),
    url(r'project_comment', views.project_comment),
    url(r'^redetails/$', views.redetails),
    url(r'^deprojects$', views.deprojects),
    url(r'^dedetails/$', views.dedetails),
    url(r'^projects$', views.projects),
    url(r'^recruit$', views.recruit),
    url(r'^starttime$', views.starttime),
    url(r'^praisecount$', views.praisecount),
    url(r'^commentcount$', views.commentcount),
    url(r'^recruit_apply$', views.recruit_apply),
    url(r'^prcomment$',views.prcomment),
    url(r'^preport$',views.preport),
    url(r'^prcreport$',views.preport),
    url(r'^pcreport$',views.pcreport),
    url(r'^prattendadd$',views.prattendadd),
    url(r'^prattenddelete$',views.prattenddelete),
    url(r'^prpraiseadd$',views.prpraiseadd),
    url(r'^prpraisedelete$',views.prpraisedelete),


    url(r'^crdetails$', views.crdetails),
    url(r'^crcreate$',views.crcreate),
    url(r'^crreport$',views.crreport),
    url(r'^rdcreport$',views.rdcreport),
    url(r'^star$', views.star),
    url(r'^attend$', views.attend),
    url(r'^service$', views.service),
    url(r'^advice$', views.advice),
    url(r'^logout$', views.logout),
    url(r'^ordinance',views.ordinance),
    url(r'^release',views.release),
    url(r'^comment',views.comment),
    url(r'^rcomment',views.rcomment),
    url(r'^teamattend$',views.teamattend),
    url(r'^team_attend$', views.team_attend),
    url(r'^team_star$', views.team_star),
    url(r'star', views.star),

    url(r'^teamcomment$', views.teamcomment),

    url(r'^editprofile$', views.editprofile),
    url(r'^perCreation$', views.perCreation),
    url(r'^PM$', views.PM),
    url(r'^PM_content/(?P<projectid>\d+)$', views.PM_content),
    url(r'^PM_join$', views.PM_join),
    url(r'^PM_draft$', views.PM_draft),
    url(r'^delpeople$', views.delpeople),
    url(r'^get_follow_count$', views.get_follow_count),
    url(r'^get_praise_count$', views.get_praise_count),
    url(r'^get_user_name$', views.get_user_name),
    url(r'^personal_information$', views.personal_information),
    url(r'^account_information$', views.account_information),
    url(r'^account_information_imgs$', views.account_information_imgs),
    url(r'^change_password$', views.change_password),
    url(r'^personal_label$', views.personal_label),
    url(r'^user_delete_personal_label$', views.user_delete_personal_label),


    # 工具函数
    url(r'^getimg', views.get_user_img),
]



