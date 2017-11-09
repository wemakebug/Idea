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
from . import views as views, reload as reload
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
    url(r'^project/all$', views.project_all),
    url(r'^project/detail$', views.project_detail),
    url(r'^project/recmanage$', views.project_recmanage),
    url(r'^project/recruit$', views.projet_recruit),

    url(r'^user/add', views.user_add),
    url(r'^user/all', views.user_all),
    url(r'^user/detail', views.user_detail),
    url(r'^user/introduction$', views.user_introduction),
    url(r'^user/timeline$', views.user_timeline),

    url(r'^label/project$', views.label_project),
    url(r'^label/user$',views.label_user),
    url(r'^label/relation', views.label_relation),

    url(r'^creation/all', views.creation_all),
    url(r'^creation/add', views.creation_add),


    url(r'^user_detail$', views.user_detail),
    url(r'^profile$', views.Profile),
    url(r'^PhotoGallery$', views.PhotoGallary),
    url(r'^$', views.index),
]

handler404 = views.page_not_found

handler500 = views.permition_denied