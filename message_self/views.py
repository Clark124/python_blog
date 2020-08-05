import json

from django.shortcuts import render
from django.http import JsonResponse
from tools.loging_decorator import login_check
from topic.models import Topic
from message_self.models import Message, Reply
from user.models import UserProfile
import datetime


# Create your views here.
@login_check('POST')
def messages(request, topic_id):
    if request.method == 'POST':

        try:
            topic = Topic.objects.get(id=topic_id)
        except:
            result = {'code': 402, 'error': '该id的文章不存在！'}
            return JsonResponse(result)

        author = request.user
        if topic.limit == 'private' and author != topic.author:
            result = {'code': 406, 'error': '你没有权限发送留言！'}
            return JsonResponse(result)

        json_str = request.body
        if not json_str:
            result = {"code": 403, 'error': '请求数据不能为空！'}
            return JsonResponse(result)

        json_obj = json.loads(json_str)
        content = json_obj.get('content')
        if not content:
            result = {"code": 404, 'error': '留言内容不能为空！'}
            return JsonResponse(result)

        message = Message.objects.create(topic=topic, author=author,
                                         content=content, )
        result = {'code': 200, 'data': {
            'author': author.nickname,
            'author_id': author.username,
            'avatar': str(author.avatar),
            'content': content,
            'created_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'message_id': message.id,
            'replys': [],
        }}
        return JsonResponse(result)


@login_check('POST', 'DELETE')
def reply(request, topic_id, message_id):
    try:
        Topic.objects.get(id=topic_id)
    except Topic.DoesNotExist:
        result = {'code': 402, 'error': '该id的文章不存在！'}
        return JsonResponse(result)

    try:
        message = Message.objects.get(id=message_id)
    except Message.DoesNotExist:
        result = {'code': 402, 'error': '留言不存在！'}
        return JsonResponse(result)

    author = request.user

    if request.method == "POST":
        json_str = request.body
        if not json_str:
            result = {"code": 403, 'error': '请求数据不能为空！'}
            return JsonResponse(result)

        json_obj = json.loads(json_str)
        content = json_obj.get('content')
        if not content:
            result = {"code": 405, 'error': '回复不能为空！'}
            return JsonResponse(result)
        reply_to = json_obj.get('reply_to')

        try:
            reply_to_user = UserProfile.objects.get(username=reply_to)
        except:
            reply_to_user = None

        if reply_to_user:
            reply_to_user = reply_to_user.username

        reply_item = Reply.objects.create(message=message, author=author, reply_to=reply_to_user,
                                          content=content, )
        result = {'code': 200, 'data': {
            'author': author.nickname,
            'author_id': author.username,
            'avatar': str(author.avatar),
            'created_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'content': content,
            'reply_id': reply_item.id

        }}
        return JsonResponse(result)

    elif request.method == 'DELETE':
        try:
            message = Message.objects.get(id=message_id, author=author)
        except Reply.DoesNotExist:
            result = {'code': 406, 'error': '您没有留言'}
            return JsonResponse(result)

        message.delete()
        result = {'code': 200, 'message': '删除留言成功'}
        return JsonResponse(result)


@login_check('DELETE')
def deleteReply(request, topic_id, message_id, reply_id):
    try:
        Topic.objects.get(id=topic_id)
    except Topic.DoesNotExist:
        result = {'code': 402, 'error': '该id的文章不存在！'}
        return JsonResponse(result)

    try:
        Message.objects.get(id=message_id)
    except Message.DoesNotExist:
        result = {'code': 402, 'error': '该文章还没有留言！'}
        return JsonResponse(result)

    author = request.user

    try:
        reply = Reply.objects.get(id=reply_id, author=author)
    except Reply.DoesNotExist:
        result = {'code': 402, 'error': '回复不存在！'}
        return JsonResponse(result)

    reply.delete()
    result = {'code': 200, 'message': '删除回复成功'}
    return JsonResponse(result)
