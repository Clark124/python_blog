from django.conf.urls import url
from . import views
from django.urls import path, re_path

urlpatterns = [
    re_path(r'^$', views.users),
    re_path(r'^/(?P<username>\w+)$', views.users),
    re_path(r'^/(?P<username>\w+)/avatar$', views.user_avatar)
]
