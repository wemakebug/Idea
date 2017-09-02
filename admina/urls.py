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
from admina import views as views, reload as reload
urlpatterns = [
    url(r'login$', views.login),
    url(r'logout$', views.logout),
    url(r'score_rank$', views.score_rank),
    url(r'score_record$', views.score_record,),
    url(r'user_score', views.score_user),
    url(r'user_detail$', reload.user_detail),
    url(r'UserManager$', views.UserManager),
    url(r'label_user$', reload.label_user),
    url(r'label_project$', reload.label_project),

    # test urls  deleted  enable
    url(r'util1$', reload.util1),
    url(r'util2$', reload.util2),
    url(r'util3$', reload.util3),
    url(r'util4$', reload.util4),
    url(r'util5$', reload.util5),

    # this url should always in the last
    url(r'', views.login),

]
