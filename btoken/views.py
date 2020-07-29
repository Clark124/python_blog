import hashlib
import json
import time
import jwt

from django.http import JsonResponse
from user.models import UserProfile


# Create your views here.
def btoken(request):
    if not request.method == 'POST':
        result = {'code': 101, 'error': 'Please use POST'}
        return JsonResponse(result)

    json_str = request.body
    if not json_str:
        result = {'code': 102, 'error': 'Please post data'}
        return JsonResponse(result)

    json_obj = json.loads(json_str)

    # 获取用户名和密码
    username = json_obj.get("username")
    password = json_obj.get("password")

    if not username:
        result = {'code': 103, 'error': 'Please give me username!'}
        return JsonResponse(result)

    if not password:
        result = {'code': 104, 'error': 'Please give me password!'}
        return JsonResponse(result)

    users = UserProfile.objects.filter(username=username)

    # 用户不存在
    if not users:
        result = {'code': 105, 'error': 'The user is not existed'}
        return JsonResponse(result)

    # hash password
    p_m = hashlib.sha1()
    try:
        p_m.update(password.encode())
    except Exception:
        result = {'code': 107, 'error': '密码的数据类型为字符串！'}
        return JsonResponse(result)

    # 对比密码
    if p_m.hexdigest() != users[0].password:
        result = {'code': 106, 'error': 'The username maybe wrong or the password is wrong'}
        return JsonResponse(result)

    # 生成token
    token = make_token(username)
    result = {'code': 200, 'username': username, 'data': {'token': token.decode()}}
    return JsonResponse(result)


def make_token(username, expire=3600 * 24 * 7):
    """
    生成token
    :param username:
    :param expire:
    :return:
    """
    key = 'abcdef1234'
    now_t = time.time()
    payload = {'username': username, 'exp': int(now_t + expire)}
    return jwt.encode(payload, key, algorithm='HS256')
