from django.db import models
from user.models import UserProfile


# mysql 查询指定表的创建语句 show create table topic\G


# Create your models here.
class Topic(models.Model):
    title = models.CharField('文章标题', max_length=50)
    # 作者
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    # tec 技术类的 & no-tec 非技术类
    category = models.CharField('文章分类', max_length=20)
    # limit - public 公开的 & private 私有的 【只有文章作者本人能看】
    limit = models.CharField('文章权限', max_length=10)
    # 文章创建时间
    created_time = models.DateTimeField()
    # 文章修改时间
    modified_time = models.DateTimeField()
    content = models.TextField('文章内容')
    introduce = models.CharField('文章简介', max_length=90)

    class Meta:
        # 自定义表名
        db_table = 'topic'

    def __str__(self):
        return self.title


class TopicHeart(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)