from . import views
from django.urls import re_path

urlpatterns = [
    re_path(r'^$', views.topics),
    re_path(r'^/heart$', views.hearts),
    re_path(r'^/home$', views.topics_home),
    re_path(r'^/view_rank$', views.topics_view_rank),
    re_path(r'^/recommend$', views.topics_recommend),
    re_path(r'^/carousel$', views.topic_carousel),
    re_path(r'^/search$', views.topic_search),
    re_path(r'^/(?P<username>\w+)$', views.topics),

]
