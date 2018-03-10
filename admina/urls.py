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
from django.conf.urls import url
from . import views as views
from . import model_class

app_name = 'admina'

urlpatterns = [

    # url(r'^login$', views.login),
    # url(r'^logout$', views.logout),
    # url(r'^score_rank$', views.score_rank),
    # url(r'^score_record$', views.score_record),
    # url(r'^user_score/(?P<page>\d+)$', views.score_user),
    # url(r'^user_detail$', reload.user_detail),
    # url(r'^UserManager$', views.UserManager),
    # url(r'^label_user/(?P<page>\d+)$', reload.label_user),
    # url(r'^label_project/(?P<page>\d+)$', reload.label_project),

    url(r'^login$', views.login),
    url(r'^logout$', views.logout),

    url(r'^project/add$', views.project_add),
    url(r'^project/all/(?P<page>(\d+)?)$', views.project_all, name='project_all'),
    url(r'^project/detail/(?P<id>(\d+)?)$', views.project_detail),
    url(r'^project/recmanage/$', views.project_recmanage),
    url(r'^project/recruit$', views.project_recruit, name='project_recruit'),
    url(r'^project/delete/(?P<deleteId>(\d+))', views.project_delete),

    url(r'^user/add$', views.user_add, name='user_add'),
    url(r'^user/all/(?P<page>(\d+)?)$', views.user_all, name='user_all'),
    url(r'^user/detail/(?P<userid>(\d+)?)$', views.user_detail, name='user_detail'),
    url(r'^user/introduction$', views.user_introduction),
    url(r'^user/timeline$', views.user_timeline),

    url(r'^label/project$', views.label_project),
    url(r'^label/user$',views.label_user),
    url(r'^deletelabel/user$', views.deleteUserLable),
    url(r'^deletelabel/project$', views.deleteProjectLable),


    url(r'^creation/all/(?P<page>(\d+)?)$', views.creation_all, name='creation_all'),
    url(r'^creation/add', views.creation_add, name='creation_add'),
    url(r'^creation/delete', views.creation_delete, name='creation_delete'),
    url(r'^creation/modify', views.creation_modify),

    url(r'^report/comment$', views.report_comment, name='report_comment'),
    url(r'^report/user$', views.report_user, name='report_user'),
    url(r'^report/project$', views.report_project, name='report_project'),
    url(r'^report/creation$', views.report_creation, name='report_creation'),

    url(r'^comment/all', views.comment_statistic, name='comment_statistic'),
    url(r'^comment/project', views.comment_project, name='comment_project'),
    url(r'^comment/user', views.comment_user, name='comment_user'),
    url(r'^comment/creation', views.comment_creation, name='comment_creation'),
    url(r'^deletecomment/project$', views.deleteComment),
    url(r'^showcomment/project$', views.show_project_comment),
    url(r'^deletecomment/creation$', views.deletecreation),

    url(r'^score/rank$', views.score_rank, name='score_rank'),
    url(r'^score/record$', views.score_record, name='score_record'),

    url(r'^relation/praise$', views.relation_praise, name='relation_praise'),
    url(r'^relation/attention', views.relation_attention, name='relation_attention'),



    # 将来可能弃用的视图
    url(r'^user_detail$', views.user_detail),
    url(r'^profile$', views.Profile),
    url(r'^PhotoGallery$', views.PhotoGallary),
    url(r'^$', views.index),


    # 基于类的视图的url 暂时弃用
    url(r'^creationlist$', model_class.CreatinoDisplayAll.as_view(), name='creation_detail'),
]

handler404 = views.page_not_found
handler500 = views.permition_denied
