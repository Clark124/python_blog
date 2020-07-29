from django.contrib import admin
from . import models


# 模型管理器类
class UserManager(admin.ModelAdmin):
    list_display = ['username', 'password', 'nickname', 'email']
    list_display_links = ['username']
    list_filter = ['username']
    search_fields = ['username', ]
    list_editable = ['email']


# Register your models here.
admin.site.register(models.UserProfile, UserManager)
