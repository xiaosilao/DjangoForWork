"""RzAdmin URL Configuration

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
from django.contrib import admin
from RzAdmin import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),  # django admin
    url(r'^$', views.index),
    url(r'^accounts/login/$', views.acc_login),  # 登录
    url(r'^accounts/logout/$', views.acc_logout),  # 注销
    url(r'^accounts/change_avatar/$', views.change_avatar, name="change_avatar"),  # 修改用户头像
    url(r'^automatic/', include("automatic.urls")),  # automatic App
    url(r'^kind_admin/', include("kind_admin.urls")),  # kind_admin 插件
    url(r'^daily/', include("daily.urls")),  # daily App
]
