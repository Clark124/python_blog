
from . import views
from django.urls import re_path

urlpatterns = [
    re_path(r'^image$', views.uploadImage),
]