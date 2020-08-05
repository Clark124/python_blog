import time

from django.http import JsonResponse
import os
from django.conf import settings
from tools.loging_decorator import login_check

# Create your views here.

@login_check('POST')
def uploadImage(request):
    if request.method != 'POST':
        return JsonResponse({'code': 501, 'error': '请求方法错误！'})
    else:

        my_file = request.FILES['upload_image']
        if not my_file:
            result = {'code':502, 'error': '请求参数不正确！'}
            return JsonResponse(result)

        with open(os.path.join(settings.MEDIA_ROOT + 'images', str(round(time.time())) + my_file.name),
                  'wb+') as f:
            b = my_file.file.read()
            f.write(b)

        return JsonResponse({'code': 200, 'data': {'url': 'images/' + str(round(time.time())) + my_file.name}})
