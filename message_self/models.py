from django.db import models

from user.models import UserProfile
from topic.models import Topic


# Create your models here.
class Message(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    content = models.CharField('留言内容', max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        # 自定义表名
        db_table = 'message'


class Reply(models.Model):
    content = models.CharField('回复留言内容', max_length=100)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    reply_to = models.CharField('回复给谁', max_length=30, null=True)

    class Meta:
        # 自定义表名
        db_table = 'reply'
