from django.contrib import admin
from . import models


# 模型管理器类
class TopicManager(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_time', 'limit', 'category']
    list_display_links = ['title']
    list_filter = ['title']
    search_fields = ['title', ]
    # list_editable = ['email']


# Register your models here.
admin.site.register(models.Topic, TopicManager)
