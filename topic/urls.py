from . import views
from django.urls import re_path

urlpatterns = [
    re_path(r'^$', views.topics),
    re_path(r'^/heart$', views.hearts),
    re_path(r'^/(?P<username>\w+)$', views.topics),

]
