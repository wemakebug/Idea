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
    url(r'^index$', views.index),
    url(r'^login$', views.login),
    url(r'^regist$', views.regist),
    url(r'^team$', views.team),
    url(r'^teamdetails/(?P<teamid>\d+)$', views.teamdetails),
    url(r'^teamhelpapplication/?(\d+)$', views.teamhelpapplication),
    url(r'^creations$', views.creations),
    url(r'^forgetPassword$', views.forgetPassword),
    url(r'^homepage$',views.homepage),
    url(r'^editprofile$',views.editprofile),
    url(r'^apply$', views.apply),
    url(r'^recruit$', views.projects),
    url(r'^redetails/$', views.redetails),
    url(r'^projects$', views.projects),
    url(r'^crdetails$', views.crdetails),
    url(r'^star$', views.star),
    url(r'^attend$', views.attend),
    url(r'^service$', views.service),
    url(r'^advice$', views.advice),
    url(r'^logout$', views.logout),
    url(r'^test/?(\d+)$', views.test),
    url(r'^getimg', views.get_user_img),
    url(r'^ordinance',views.ordinance),
    url(r'^release',views.addlabel),
    url(r'comment_creation', views.Comment_Creation),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

