import hashlib
import json

from django.http import JsonResponse
from . import models
from btoken.views import make_token
from tools.loging_decorator import login_check


# Create your views here.
@login_check('PUT')
def users(request, username=None):
    if request.method == 'GET':
        if username:
            # 具体用户的数据
            # /v1/users/clark?into=1&email=1
            try:
                user = models.UserProfile.objects.get(username=username)
            except models.UserProfile.DoesNotExist:
                user = None

            if not user:
                # 用户不存在
                result = {'code': 208, 'error': 'The user is not existed'}
                return JsonResponse(result)

            # 判断查询字符串
            if request.GET.keys():
                # 证明有查询字符串
                data = {}
                for k in request.GET.keys():
                    # 数据库中最好有非空默认值
                    if hasattr(user, k):
                        data[k] = getattr(user, k)
                result = {'code': 200, 'username': username, 'data': data}
                return JsonResponse(result)
            else:
                # 证明指定查询用户全量数据
                result = {'code': 200, 'username': username,
                          'data': {'info': user.info, 'sign': user.sign,
                                   'nickname': user.nickname,
                                   'avatar': str(user.avatar)
                                   }}
                return JsonResponse(result)

        else:
            # 全部用户的数据
            try:
                users = models.UserProfile.objects.all()
            except:
                users = []

            data = []
            host = request.META['HTTP_HOST']
            for item in users:
                obj = {
                    'username': item.username,
                    'email': item.email,
                    'info': item.info,
                    'avatar': host + "/" + str(item.avatar),
                    'sign': item.sign
                }
                data.append(obj)

            result = {"code": 200, 'data': data}
            return JsonResponse(result)

    elif request.method == 'POST':
        # 注册
        # 密码需用SHA-1 hashlib.sha1() ->update ->
        json_str = request.body
        if not json_str:
            # 前端异常提交，空数据
            result = {"code": 202, 'error': 'please POST data'}
            return JsonResponse(result)

        # 反序列化json_str
        json_str = json.loads(json_str)
        username = json_str.get("username")
        email = json_str.get("email")
        password_1 = json_str.get("password_1")
        password_2 = json_str.get("password_2")

        if not username:
            # 用户名不存在
            result = {"code": 203, "error": 'please give me username'}
            return JsonResponse(result)
        if not email:
            # 邮箱不存在
            result = {"code": 204, "error": 'please give me email'}
            return JsonResponse(result)
        if not password_1 or not password_2:
            # 密码不存在
            result = {"code": 205, "error": 'please give me password'}
            return JsonResponse(result)
        if password_1 != password_2:
            result = {"code": 206, "error": 'Two password is not same'}
            return JsonResponse(result)

        # 检查用户是否存在
        old_user = models.UserProfile.objects.filter(username=username)
        if old_user:
            # 改用户已经注册
            result = {"code": 207, "error": '用户已存在！'}
            return JsonResponse(result)

        # 将密码进行hash
        h = hashlib.sha1()
        h.update(password_1.encode())
        try:
            models.UserProfile.objects.create(username=username, nickname=username,
                                              email=email, password=h.hexdigest())
        except Exception as e:
            print("UserProfile create error is %s" % (e))
            result = {"code": 207, "error": 'The username is existed'}
            return JsonResponse(result)

        # 根据用户名 生成token
        token = make_token(username)
        result = {'code': 200, 'username': username, 'data': {'token': token.decode()}}
        return JsonResponse(result)

    elif request.method == 'PUT':

        user = request.user
        if not username:
            # 用户名不存在
            result = {"code": 203, "error": 'please give me username'}
            return JsonResponse(result)

        if username != user.username:
            result = {"code": 203, "error": '没有权限修改！'}
            return JsonResponse(result)

        json_str = request.body
        # 判断前端是否给了json 串
        if not json_str:
            result = {'code': 202, 'error': '没有数据传过来！'}
            return JsonResponse(result)

        json_obj = json.loads(json_str)
        nickname = json_obj.get('nickname')
        if not nickname:
            result = {'code': 209, 'error': '昵称不能为空！'}
            return JsonResponse(result)
        #
        sign = json_obj.get('sign', '')
        info = json_obj.get('info', '')

        # 保存
        user.sign = sign
        user.nickname = nickname
        user.info = info
        user.save()

        return JsonResponse({'code': 200, 'username': username})


@login_check('POST')
def user_avatar(request, username):
    # 上传图片：
    # 1.前端 form提交 并且 content-type -> multipart/form-data
    # 2.后端只要拿到post提交 request.FILES['avatar']
    # 注意：有余目前django获取put请求的multipart数据较为负载,故改为post获取multipart数据

    if not request.method == 'POST':
        result = {'code': 210, 'error': '请求方法必须为post请求！'}
        return JsonResponse(result)

    # users = models.UserProfile.objects.filter(username=username)
    #
    # if not users:
    #     result = {'code': 208, 'error': '用户不存在！'}
    #     return JsonResponse(result)

    user = request.user
    if user.username != username:
        result = {'code': 212, 'error': '不能上传改用户的头像'}
        return JsonResponse(result)

    if request.FILES.get('avatar'):
        # 正常提交图片信息,进行存储
        user.avatar = request.FILES['avatar']
        user.save()
        result = {'code': 200, 'username': username, 'data': {'avatar': str(user.avatar)}}
        return JsonResponse(result)
    else:
        result = {'code': 211, 'error': '没有上传头像数据'}
        return JsonResponse(result)

    return JsonResponse('ok')
