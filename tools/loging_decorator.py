import jwt
from django.http import JsonResponse
from user.models import UserProfile

KEY = 'abcdef1234'


# *methods - 可接受 任意参数
def login_check(*methods):
    def _login_check(func):
        def wrapper(request, *args, **kwargs):
            # token request header -> authorization
            token = request.META.get('HTTP_AUTHORIZATION')

            if not methods:
                # 如果没有传methods参数，则直接返回视图
                return func(request, *args, **kwargs)

            if request.method not in methods:
                # 如果当前请求的方法不再 methods内，则直接返回视图
                return func(request, *args, **kwargs)

            # 严格件数大小写，统一大写
            # 严格检查methods里的参数是 POST,GET,PUT,DELETE

            # 校验token,
            if not token or token == 'null':
                result = {'code': 107, 'error': '请登录!'}
                return JsonResponse(result)

            # 校验token,pyjwt 注意 异常检测
            try:
                res = jwt.decode(token, KEY, algorithms='HS256')
            # except jwt.ExpiredSignature:
            #     result = {'code': 108, 'error': '请登录'}
            #     return JsonResponse(result)
            except Exception as e:
                print('---token error is %s' % (e))
                result = {'code': 108, 'error': '请登录!'}
                return JsonResponse(result)

            # token 校验成功，根据用户名取出用户
            username = res['username']
            user = UserProfile.objects.get(username=username)

            # request.user = user
            request.user = user
            return func(request, *args, **kwargs)

        return wrapper

    return _login_check


# 检查是否本人
def user_check(request, username):
    token = request.META.get('HTTP_AUTHORIZATION')
    if not token or token == 'null':
        return None
    else:
        try:
            res = jwt.decode(token, KEY, algorithms='HS256')
        except Exception as e:
            return None

        if res['username'] == username:
            return True
        else:
            return None


def has_login(request):
    token = request.META.get('HTTP_AUTHORIZATION')
    if not token or token == 'null':
        return None
    else:
        try:
            res = jwt.decode(token, KEY, algorithms='HS256')
        except Exception as e:
            return None

        username = res['username']
        user = UserProfile.objects.get(username=username)
        return user
