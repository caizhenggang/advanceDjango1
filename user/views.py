import os
import random
from django.core.paginator import Paginator
from django.db.models import Q
import uuid

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import json
from PIL import Image, ImageDraw, ImageFont
from common import code
from common.code import new_code_str
from user.models import Order
from django.core.cache import cache


@csrf_exempt
def regist_2(request, user_id=None):
    loves = ['H5', 'Java', 'Python', 'Linux', 'Oracle', 'Cookie']
    # 获取参数名相同的多个参数值
    select_loves = request.GET.getlist('love')

    return render(request, 'regist2.html', locals())


@csrf_exempt
def regist3(request, user_id=None):
    print(request.POST)  # 只接受post请求方法上传的form表单数据
    print(request.method)

    # 查看META元信息
    print(type(request.META))
    print(request.environ)

    return render(request, 'regist3.html', locals())


@csrf_exempt
def regist4(request, user_id=None):
    # print(request.method)
    # print(request.POST)
    # print(request.FILES)

    # print(request.body)

    name = request.POST.get('name')
    phone = request.POST.get('phone')

    upload_file: InMemoryUploadedFile = request.FILES.get('img1')
    if upload_file:
        # print(upload_file.name) # 文件名
        # print(upload_file.content_type) #文件类型   MIMETYPE image/png
        # print(upload_file.size)
        # print(upload_file.charset)

        # 上传必须是图片且必须小于50k
        if all((
                upload_file.content_type.startswith('image/'),
                upload_file.size < 50 * 1024
        )):
            print(request.META.get('REMOTE_ADDR'), '上传了', upload_file)
            filename = name + os.path.splitext(upload_file.name)[-1]

            # 将内存中的文件写入到磁盘中
            with open('images/' + filename, 'wb') as f:
                # 分段写入
                for chunk in upload_file.chunks():
                    f.write(chunk)
                f.flush()

            return HttpResponse('上传文件成功！')
        else:
            return HttpResponse('请上传小于50k以内的图片')

    return render(request, 'regist4.html', locals())


def regist(request):
    resp1 = HttpResponse(content='你好'.encode('utf-8'),
                         status=200,
                         content_type='text/html;charset=utf-8')

    with open('images/李晨西.jpg', 'rb') as f:
        bytes = f.read()
    # 响应图片数据
    resp2 = HttpResponse(content=bytes,
                         content_type='image/jpg')
    # ?? 响应头如何设置

    # 响应json数据
    data = {'name': 'disen', 'age': 20}

    # 序列化，把对象转成字符串
    resp3 = HttpResponse(content=json.dumps(data),
                         content_type='application/json')

    resp4 = JsonResponse(data)
    return resp2


def add_cookie(request):
    # 生成token，并存储到Cookie
    token = uuid.uuid4().hex

    resp = HttpResponse('增加Cookie： token成功')

    from datetime import datetime, timedelta
    resp.set_cookie('token', token,
                    expires=datetime.now() + timedelta(minutes=2))

    return resp


def del_cookie(request):
    resp = HttpResponse('删除Cookie： token成功!')

    # 删除单个cookie
    resp.delete_cookie('token')

    # 删除所有的cookie
    # 先从请求对象中获取所有的Cookie信息，然后在删除
    for k in request.COOKIES:
        resp.delete_cookie(k)

    return resp


def login(request):
    phone = request.GET.get('phone')
    code = request.GET.get('code')

    # 判断缓存中是否存在phone
    # 存在则读取
    if all((
            cache.has_key(phone),
            cache.get(phone) == code
    )):
        resp = HttpResponse('登录成功！')
        token = uuid.uuid4().hex  # 保存到缓存
        resp.set_cookie('token', token)

        # 删除缓存
        cache.delete(phone)

        return resp

    return HttpResponse('登录失败，请确认phone和code！')


def logout(request):
    # 删除所有的cookie和session中的信息
    request.session.clear()  # 删除所有的Session中信息
    resp = HttpResponse('注销成功')
    resp.delete_cookie('token')  # 删除单个Cookie的信息

    return resp


def list(request):
    # 验证是否登录

    return HttpResponse('请先登录！')


def new_code(request):
    # 生成手机验证码
    # 随机产生验证码；大小写字母+数字
    code_txt = code.new_code_str(4)
    print(code_txt)

    phone = request.GET.get('phone', '')
    # 将验证码保存到session中
    request.session['code'] = code_txt
    request.session['phone'] = phone

    # 将验证码保存到cache
    # timeout是缓存的时间
    cache.set(phone, code_txt, timeout=60)

    # 向手机发送验证码； 华为云、阿里云：短信服务

    return HttpResponse('以向 %s 手机发送验证码！' % phone)


def new_img_code(request):
    # 创建画布
    img = Image.new('RGB', (120, 40), (100, 100, 0))

    # 从画布中获取画笔
    draw = ImageDraw.Draw(img, 'RGB')

    # 创建字体对象和字体颜色
    font_color = (0, 20, 100)
    font = ImageFont.truetype(font='static/fonts/buding.ttf',
                              size=30)

    valid_code = new_code_str(6)
    request.session['code'] = valid_code
    # 开始画内容
    draw.text((5, 5), valid_code, fill=font_color, font=font)

    for _ in range(500):
        x = random.randint(0, 120)
        y = random.randint(0, 40)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        draw.point((x, y), (r, g, b))

    # 将画布写入到内存字节数组中
    from io import BytesIO
    buffer = BytesIO()
    img.save(buffer, 'png')  # 写入

    return HttpResponse(content=buffer.getvalue(),
                        content_type='image/png')


def order_list(request):
    wd = request.GET.get('wd', '')
    page = request.GET.get('page', 1)
    orders = Order.objects.filter(Q(title__icontains=wd)).all()

    # 分页器Paginator
    paginator = Paginator(orders, 5)
    pager = paginator.page(page)  # 查询第page页

    return render(request, 'list.html', locals())
