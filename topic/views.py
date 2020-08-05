import datetime
import json

from django.http import JsonResponse
from tools.loging_decorator import login_check, user_check, has_login
from . import models
from user.models import UserProfile
from tools.pagination import paginator_dic
from tools.commen import find_url
from django.db.models import Q
from urllib.parse import unquote


# Create your views here.
@login_check('POST', 'DELETE', 'PUT')
def topics(request, username=None):
    # /v1/topics/<username>
    if request.method == 'POST':
        author = request.user

        json_str = request.body
        if not json_str:
            # 前端异常提交，空数据
            result = {"code": 302, 'error': '数据不能为空'}
            return JsonResponse(result)

        json_obj = json.loads(json_str)

        title = json_obj.get("title")
        if not title:
            result = {'code': 305, 'error': '请输入标题！'}
            return JsonResponse(result)

        # 带全部样式的内容 - content
        content = json_obj.get("content")
        if not content:
            result = {'code': 306, 'error': '文章内容不能为空！'}
            return JsonResponse(result)

        # 纯文本
        content_text = json_obj.get("content_text")
        if not content_text:
            result = {'code': 307, 'error': '纯文本不能为空！'}
            return JsonResponse(result)
        introduce = content_text[:100]

        category = json_obj.get("category")
        if category not in ['tec', 'no-tec']:
            result = {'code': 304, 'error': '传入的种类格式不正确'}
            return JsonResponse(result)

        article_type = json_obj.get("type")
        if article_type not in [1, 2, 3]:
            result = {'code': 305, 'error': '传入的文章类型不正确'}
            return JsonResponse(result)

        limit = json_obj.get('limit')
        if limit not in ['public', 'private']:
            result = {"code": 303, 'error': '传入的权限格式不正确！'}
            return JsonResponse(result)

        # 设置创建时间/修改时间
        now = datetime.datetime.now()

        # 存储topic
        models.Topic.objects.create(title=title, content=content, introduce=introduce, limit=limit,
                                    article_type=article_type,
                                    category=category, created_time=now, modified_time=now, author=author)
        result = {'code': 200, 'username': author.username}
        return JsonResponse(result)

    elif request.method == 'PUT':
        # 修改文章
        author = request.user

        json_str = request.body
        if not json_str:
            # 前端异常提交，空数据
            result = {"code": 302, 'error': '数据不能为空'}
            return JsonResponse(result)

        json_obj = json.loads(json_str)

        id = json_obj.get('id')
        if not id:
            result = {'code': 305, 'error': '参数中需要带文章的id！'}
            return JsonResponse(result)

        try:
            topic = models.Topic.objects.get(id=id)
        except models.Topic.DoesNotExist:
            result = {"code": 308, 'error': '文章不存在！'}
            return JsonResponse(result)
        if topic.author != author:
            result = {"code": 309, 'error': '没有权限修改该文章！'}
            return JsonResponse(result)

        title = json_obj.get("title")
        if not title:
            result = {'code': 305, 'error': '请输入标题！'}
            return JsonResponse(result)

        # 带全部样式的内容 - content
        content = json_obj.get("content")
        if not content:
            result = {'code': 306, 'error': '文章内容不能为空！'}
            return JsonResponse(result)

        # 纯文本
        content_text = json_obj.get("content_text")
        if not content_text:
            result = {'code': 307, 'error': '纯文本不能为空！'}
            return JsonResponse(result)
        introduce = content_text[:30]

        category = json_obj.get("category")
        if category not in ['tec', 'no-tec']:
            result = {'code': 304, 'error': '传入的种类格式不正确'}
            return JsonResponse(result)

        article_type = json_obj.get("type")
        if article_type not in [1, 2, 3]:
            result = {'code': 305, 'error': '传入的文章类型不正确'}
            return JsonResponse(result)

        limit = json_obj.get('limit')
        if limit not in ['public', 'private']:
            result = {"code": 303, 'error': '传入的权限格式不正确！'}
            return JsonResponse(result)

        # 设置创建时间/修改时间
        now = datetime.datetime.now()

        topic.title = title
        topic.content = content
        topic.introduce = introduce
        topic.article_type = article_type
        topic.limit = limit
        topic.modified_time = now
        topic.save()
        result = {"code": 200, 'message': "更新成功"}
        return JsonResponse(result)


    elif request.method == 'GET':
        # 获取用户博客列表 / 具体博客内容【带?t_id=xxx】
        try:
            user = UserProfile.objects.get(username=username)
        except models.UserProfile.DoesNotExist:
            user = None

        if not user:
            # 用户不存在
            result = {'code': 208, 'error': '用户不存在'}
            return JsonResponse(result)

        is_me = user_check(request, username)

        # 具体博客内容 /v1/topics/clark?top_id=1
        topic_id = request.GET.get('topic_id')
        is_update = request.GET.get('is_update')
        if topic_id:
            if is_me:
                try:
                    topic = models.Topic.objects.get(id=topic_id, author=user)
                except models.Topic.DoesNotExist:
                    result = {'code': 308, 'error': '该文章不存在！'}
                    return JsonResponse(result)
            else:
                try:
                    topic = models.Topic.objects.get(id=topic_id, author=user, limit='public')
                except models.Topic.DoesNotExist:
                    result = {'code': 308, 'error': '该文章不存在！'}
                    return JsonResponse(result)

            result = get_topic_detail(request, is_me, topic_id, user, topic, is_update=is_update)
            return JsonResponse(result)

        # 带查询字符串 /v1/topics/clark?page_num=1&page_size=10
        # category = request.GET.get('category')
        # if category in ['tec', 'no-tec']:
        #     if is_me:
        #         topics_list = models.Topic.objects.filter(author=user, category=category).order_by('-created_time')
        #     else:
        #         topics_list = models.Topic.objects.filter(author=user, limit='public', category=category)
        # else:
        if is_me:
            topics_list = models.Topic.objects.filter(author=user).order_by('-created_time')
        else:
            topics_list = models.Topic.objects.filter(author=user, limit='public').order_by('-created_time')

        result = user_topics_list(user, topics_list, request)
        return JsonResponse(result)

    elif request.method == 'DELETE':

        author = request.user
        if author.username != username:
            result = {'code': 306, 'error': '你没有权限删除！'}
            return JsonResponse(result)
        topic_id = request.GET.get('topic_id')
        if not topic_id:
            result = {'code': 307, 'error': '无法删除！！'}
            return JsonResponse(result)

        try:
            current_topic = models.Topic.objects.get(id=topic_id)
        except Exception:
            result = {'code': 308, 'error': '该文章不存在！'}
            return JsonResponse(result)

        current_topic.delete()
        result = {'code': 200, 'username': username, 'error': '删除成功！'}
        return JsonResponse(result)


def user_topics_list(author, author_topics, request):
    page_size = request.GET.get('page_size', 5)
    page_num = request.GET.get('page_num', 1)
    page_dic = paginator_dic(author_topics, page_size, page_num)

    page_info = {
        'has_next': page_dic.get('has_next'),
        "next_number": page_dic.get('next_number'),
        'has_previous': page_dic.get('has_previous'),
        'pre_number': page_dic.get('pre_number'),
        'current_page': page_dic.get('current_page'),
        'current_num': page_dic.get('current_num'),
        'total': page_dic.get('count'),
        'total_page': page_dic.get('number_pages')
    }

    data = []
    for item in page_dic.get('list'):
        urls = find_url(item.content)
        obj = {
            'id': item.id,
            'title': item.title,
            'category': item.category,
            "created_time": item.created_time.strftime('%Y-%m-%d %H:%M:%S'),
            'introduce': item.introduce,
            'username': author.username,
            'author': author.nickname,
            'browse_count': item.browse_count,
            'heart_count': len(item.topicheart_set.all()),
            'images': urls
        }
        data.append(obj)
    result = {"code": 200, 'data': {'nickname': author.nickname, "topics": data, 'pageInfo': page_info}}
    return result


def get_topic_detail(request, is_me, topic_id, user, topic, is_update):
    next_id = None
    next_title = None
    last_id = None
    last_title = None

    if is_me:
        next_topic = models.Topic.objects.filter(id__gt=topic_id, author=user).first()
        last_topic = models.Topic.objects.filter(id__lt=topic_id, author=user).last()
    else:
        next_topic = models.Topic.objects.filter(id__gt=topic_id, limit='public', author=user).first()
        last_topic = models.Topic.objects.filter(id__lt=topic_id, limit='public', author=user).last()

    if next_topic:
        next_id = next_topic.id
        next_title = next_topic.title
    if last_topic:
        last_id = last_topic.id
        last_title = last_topic.title

    messages = topic.message_set.all()
    messages_list = []

    message_count = 0
    for item in messages:
        message_count += 1
        replys = []
        for reply in item.reply_set.all():
            message_count += 1
            reply_to = None
            if reply.reply_to:
                reply_user = UserProfile.objects.get(username=reply.reply_to)
                reply_to = {
                    "username": reply_user.username,
                    "nickname": reply_user.nickname
                }
            obj = {
                "reply_id": reply.id,
                "content": reply.content,
                "author": reply.author.nickname,
                "author_id": reply.author.username,
                "created_time": reply.created_time.strftime('%Y-%m-%d %H:%M:%S'),
                "avatar": str(reply.author.avatar),
                "reply_to": reply_to
            }
            replys.append(obj)

        obj = {
            "message_id": item.id,
            "content": item.content,
            "author": item.author.nickname,
            "author_id": item.author.username,
            "created_time": item.created_time.strftime('%Y-%m-%d %H:%M:%S'),
            "avatar": str(item.author.avatar),
            "replys": replys
        }
        messages_list.append(obj)

    heart_count = 0
    all_heart = models.TopicHeart.objects.filter(topic=topic)
    if all_heart:
        heart_count = len(all_heart)

    has_heart = False
    has_login_user = has_login(request)
    if has_login_user:
        hearts = models.TopicHeart.objects.filter(topic=topic, user=has_login_user)
        if hearts:
            has_heart = True

    if is_update:
        result = {
            "code": 200,
            "data": {
                "id": topic.id,
                "title": topic.title,
                "limit": topic.limit,
                "article_type": topic.article_type,
                "content": topic.content,
                "introduce": topic.introduce,
            }
        }
        return result
    else:
        # 浏览次数增加1
        topic.browse_count += 1
        topic.save()

        result = {
            "code": 200,
            "data": {
                "id": topic.id,
                "nickname": topic.author.nickname,
                "title": topic.title,
                "category": topic.category,
                "created_time": topic.created_time.strftime('%Y-%m-%d %H:%M:%S'),
                "content": topic.content,
                "introduce": topic.introduce,
                "next_id": next_id,
                "next_title": next_title,
                "last_id": last_id,
                "last_title": last_title,
                "messages": messages_list,
                "messages_count": message_count,
                "has_heart": has_heart,
                "heart_count": heart_count,
                "browse_count": topic.browse_count,
            }
        }
        return result


# 点赞、取消点赞
@login_check('POST', 'DELETE')
def hearts(request):
    user = request.user

    if request.method == 'POST':
        json_str = request.body
        if not json_str:
            result = {"code": 403, 'error': '请求数据不能为空！'}
            return JsonResponse(result)

        json_obj = json.loads(json_str)
        topic_id = json_obj.get("topic_id")

        if not topic_id:
            result = {"code": 501, 'error': '传入topic_id参数不正确'}
            return JsonResponse(result)

        try:
            topic = models.Topic.objects.get(id=topic_id)
        except:
            result = {"code": 502, 'error': '文章不存在！'}
            return JsonResponse(result)

        heart = models.TopicHeart.objects.filter(user=user, topic=topic)
        if heart:
            result = {'code': 504, "error": '已经点过赞了！'}
            return JsonResponse(result)

        models.TopicHeart.objects.create(user=user, topic=topic)
        result = {'code': 200, "username": user.username}
        return JsonResponse(result)

    elif request.method == 'DELETE':
        topic_id = request.GET.get('topic_id')
        if not topic_id:
            result = {"code": 501, 'error': '传入topic_id参数不正确'}
            return JsonResponse(result)

        try:
            topic = models.Topic.objects.get(id=topic_id)
        except:
            result = {"code": 502, 'error': '文章不存在！'}
            return JsonResponse(result)

        try:
            heart = models.TopicHeart.objects.get(user=user, topic=topic)
        except models.TopicHeart.DoesNotExist:
            result = {'code': 503, "error": "该文章您没有点过赞"}
            return JsonResponse(result)

        heart.delete()
        result = {'code': 200, "username": user.username}
        return JsonResponse(result)


# 首页文章列表
def topics_home(request):
    if request.method != 'GET':
        result = {'code': 201, 'error': '请求方法不正确'}
        return JsonResponse(result)

    topics = models.Topic.objects.filter(limit='public').order_by('-modified_time')

    page_size = request.GET.get('page_size', 10)
    page_num = request.GET.get('page_num', 1)

    result = topics_list_paginator(topics, page_size, page_num)
    return JsonResponse(result)


# 查询文章点击排行列表
def topics_view_rank(request):
    if request.method != 'GET':
        result = {'code': 201, 'error': '请求方法不正确'}
        return JsonResponse(result)

    topics = models.Topic.objects.filter(limit='public').order_by('-browse_count')[:5]

    result = topics_list_res(topics)
    return JsonResponse(result)


#
def topics_recommend(request):
    if request.method != 'GET':
        result = {'code': 201, 'error': '请求方法不正确'}
        return JsonResponse(result)

    topics = models.TopicRecommend.objects.all()
    topics = (item.topic for item in topics if item.topic.limit == 'public')

    result = topics_list_res(topics)
    return JsonResponse(result)


def topic_carousel(request):
    if request.method != 'GET':
        result = {'code': 201, 'error': '请求方法不正确'}
        return JsonResponse(result)

    carousel = models.Carousel.objects.all()
    carousel = (item.topic for item in carousel if item.topic.limit == 'public')

    result = topics_list_res(carousel)
    return JsonResponse(result)


def topic_search(request):
    if request.method != 'GET':
        result = {'code': 201, 'error': '请求方法不正确'}
        return JsonResponse(result)

    key = request.GET.get('key')
    if not key:
        result = {'code': 202, 'error': '搜索内容不能为空~'}
        return JsonResponse(result)
    key = unquote(key)
    topics = models.Topic.objects.filter(Q(limit='public') & Q(title__icontains=key) | Q(content__icontains=key))

    page_size = request.GET.get('page_size', 10)
    page_num = request.GET.get('page_num', 1)

    result = topics_list_paginator(topics, page_size, page_num)
    return JsonResponse(result)


# 返回文章列表的基本数据（带分页）
def topics_list_paginator(topics, page_size, page_num):
    page_dic = paginator_dic(topics, page_size, page_num)

    page_info = {
        'has_next': page_dic.get('has_next'),
        "next_number": page_dic.get('next_number'),
        'has_previous': page_dic.get('has_previous'),
        'pre_number': page_dic.get('pre_number'),
        'current_page': page_dic.get('current_page'),
        'current_num': page_dic.get('current_num'),
        'total': page_dic.get('count'),
        'total_page': page_dic.get('number_pages')
    }

    data = []
    for item in page_dic.get('list'):
        urls = find_url(item.content)
        obj = {
            'id': item.id,
            'title': item.title,
            "created_time": item.created_time.strftime('%Y-%m-%d %H:%M:%S'),
            'introduce': item.introduce,
            'username': item.author.username,
            'author': item.author.nickname,
            'browse_count': item.browse_count,
            'heart_count': len(item.topicheart_set.all()),
            'images': urls
        }
        data.append(obj)
    return {"code": 200, 'data': {"topics": data, 'pageInfo': page_info}}


# 返回文章列表的基本数据
def topics_list_res(topics):
    data = []
    for item in topics:
        urls = find_url(item.content)
        obj = {
            'id': item.id,
            'title': item.title,
            "created_time": item.created_time.strftime('%Y-%m-%d %H:%M:%S'),
            'introduce': item.introduce,
            'username': item.author.username,
            'author': item.author.nickname,
            'browse_count': item.browse_count,
            'heart_count': len(item.topicheart_set.all()),
            'images': urls
        }
        data.append(obj)
    return {"code": 200, 'data': {"topics": data}}
