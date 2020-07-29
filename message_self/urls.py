from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^/(?P<topic_id>\d+)$', views.messages),
    re_path(r'^/(?P<topic_id>\d+)/(?P<message_id>\d+)$', views.reply),
    re_path(r'^/(?P<topic_id>\d+)/(?P<message_id>\d+)/(?P<reply_id>\d+)$', views.deleteReply),
]