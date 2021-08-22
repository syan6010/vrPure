from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib import auth
from nccu_gis_app.models import imgData, markerType
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
import logging
from PIL import Image
import exifread
import json

import uuid
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
from google.cloud.storage import Blob

# 正式使用的時候要import
# import whatimage
# import pyheif
# import traceback
# import piexif

cred = credentials.Certificate({
    "type": "service_account",
    "project_id": "webgisapi",
    "private_key_id": "c5a64cebada1e69d300d2e20b0009eeb12d59df4",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDd8UCARlAAD5mB\nO95w7sP0stqC44ZqNoejxfztv5MdGzJaxPPoPNcKiNPs+l6uNMjHmj1i4CVNSlaV\n0mlYY5ZuIK8Fo7VL1CSZNn2IJBZfXU97LPUDiWWbIRGXl2JF5EzbMQA2XH2dYFsN\n65XYLxj1rJJKQW80bbnMYH6ALdzA1cHVQXiKfZCNIgJrKC+j+5q54a0RWQaWNZWW\n/UikxtqCUcWKn/e/NUUDoN3mN0jAQhc93sHsPk07XJgpE//8i9MP3av3nksgRDZ0\nGFPVPrR4C4hdI9IJZ/sEfHFodNXujsLreIPCzR+glfpoLw9f+9Uo9Gy3FPZyQxjr\nydU5VsxBAgMBAAECggEABP8vABRVLcMsJhQ2fF1rzQEP2V2NA6wpnp7RBHtJMSER\nH6kKgsKH5uVQvCeg5RQsJw5KboT0YgqX63SayZIoa19SAXL/nG7wygBHkD6bwFbl\n+LR46bT4tCbo8fxHCqLKti6ivhaT/2yRcD1LGNxql/FkM8bIXapQwhC0GGev7il3\nIXeel0SuMof91WkGH1veGF8Zaz2HXtXQJESPXYsQqzpA/f55jCtoaQX5nwg3vh/1\nloJxxkKm2kCLYUpITLQsd90EaCWyKXYalCAFDYLxEjSuSDPSmgpkw4tcKl/nCp1r\nzuVtUzv+4sIxdUbg1CdYhHM9Ukr+vj9obvxrDchjqQKBgQDv58ILGDhnxJZpJU1y\nOrN6xc8lXpNK22GW0uXN764YWvw5NwzBgO7kvf8WBHn4IwTRIKSISNVH61iYrQjt\neMFG91pj4JMe6LUTdRuf/D7Clmlzb7HbUmKbWzktsMq0JUNS1ktE58TeiV4YrUEo\n9bAv13aWwA2919kixsdRu+3GzQKBgQDs1P2jmRZR8/lyr6CywuV/bIjkzyYX+Aq9\nFP6lSKvDZ3S9eIlQrVKuRb0VAGPqGkxU3fsbwr1ovroQV8DioY0ZJS5OZO1zUy+0\nWYmN2HrxP6Bvg9oZF3zzD4USUNqNnSUxvbERSKEAKEtc67YZ8HfFn/S5KIH3aV+x\niyP+CHsTRQKBgQDtVecW2MA8kDSJEtk6T65toDHc82JeJQi3kC6+fAZMm/54j+hz\nqp0r+HbaDlWn0OUcCuIa3Yr6Wm7MpCp33AXBskVfF7YUVv2EoU9SB9cC5JCwHejj\nY+6faTD47bSrYU3oLo5KPcv6qAVJ/mS/I8hInCz62Eb/8AElMWfQiU2jZQKBgD+Z\n84O72QKpQpRKFh3ruTY/L4RDHTfSpQ+iU8CPg5E2d2Nqu3WvFkU29VBuimaUKWuh\nMY6C/drjXZSF/IbgW8Qk+AqVkC8oZ+dHJGmzeVDQhYVtI2UZqbSctl/01ryxNwvk\npWi+2H3yVErgAkd1DLVF/7K57i1DXy+O7luKa4MBAoGADL6PT5yapXdH90Zxd23O\nyHAfgdZ2rwRo6abpnqOYEU/xtVGODsPqgN3mBKLjqGfE5pkcwjZLwmK3Ryxbk38K\nJpZToL6bxtPY0Vm+k1nT2y5cvquYpkOP+2ac1pw85T7PNgySxRTn+H30aKL9SdlT\n2opxzkIF9q5pGc0JdzuVAwY=\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-oka2e@webgisapi.iam.gserviceaccount.com",
    "client_id": "107754772873691982517",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-oka2e%40webgisapi.iam.gserviceaccount.com"
})
firebase_admin.initialize_app(cred, {
    'storageBucket': 'webgisapi.appspot.com'
})

bucket = storage.bucket()

imgWidthId = 256
imgLengthId = 257
pixelDix = 40962
pixelDiy = 40963
imgTimeId = 306
orientationId = 274
gpsTagId = 34853

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def index(request):
    user_name = request.user.username
    return render(request, "index.html", locals())


def add(request):
    all = markerType.objects.all()  # 取得所有景點
    if ('title' in request.POST):
        try:
            logger.debug('run')
            aTitle = request.POST['title']
            aContent = request.POST['content']
            aType = request.POST['type']
            avaImg = request.FILES.get('avaImg', False)
            lon = request.POST['lon']
            lat = request.POST['lat']
            user_name = request.user.username
            filename = "%s" % (uuid.uuid4())

            im = Image.open(avaImg)

            width, height = im.size

            # reduce to 30% of the original size
            target_size_percent = 30
            new_width = int(width * target_size_percent / 100)
            new_height = int(height * target_size_percent / 100)
            new_size = (new_width, new_height)
            im = im.resize(new_size)
            avaImg.seek(0)
            im.save(avaImg, "jpeg")
            avaImg.seek(0)
            logger.debug("長寬：{}".format(avaImg.size))

            blob = Blob(filename, bucket)
            blob.upload_from_file(avaImg, content_type='image/jpeg')
            blob.make_public()
            url = blob.public_url

            rec = imgData(title=aTitle, content=aContent, type=aType,
                          purl=url, lon=lon, lat=lat, username=user_name)
            rec.save()
            return render(request, "index.html")

        except Exception as e:
            logger.debug("error: {}".format(e))
            return redirect('/error/')
    else:
        return render(request, "add_refine.html", locals())


def map(request):
    user_name = request.user.username
    markerTypes = markerType.objects.all()
    if request.method == "POST":
        getTitle = request.POST['title']
        getType = request.POST['type']
        all = imgData.objects.filter(title__contains="{}".format(
            getTitle), type="{}".format(getType))
        return render(request, "map_refine.html", locals())
    else:
        if request.user.is_authenticated:
            all = imgData.objects.filter(username="{}".format(user_name))
        else:
            all = imgData.objects.all()  # 取得所有景點
        return render(request, "map_refine.html", locals())


def login(request):
    # messages = ''  #初始時清除訊息，依照判斷結果決定秀出那些訊息
    if request.method == 'POST':  # 如果是以POST方式才處理
        name = request.POST['username'].strip()  # 取得輸入帳號
        password = request.POST['password']  # 取得輸入密碼
        user1 = authenticate(username=name, password=password)  # 驗證
        if user1 is not None:  # 驗證通過
            if user1.is_active:  # 帳號有效
                auth.login(request, user1)  # 登入
                return redirect('/index/')  # 開啟管理頁面
            else:  # 帳號無效
                message = '帳號尚未啟用！'
        else:  # 驗證未通過
            message = '登入失敗！'
    return render(request, "login.html", locals())


def logout(request):  # 登出
    auth.logout(request)
    return redirect('/index/')


def profileUpdate(request):
    if request.method == "POST":
        try:
            name = request.POST['username'].strip()  # 取得輸入帳號
            password = request.POST['password']  # 取得輸入密碼
            email = request.POST['email']  # 取得輸入密碼
            user = User.objects.create_user(name, email, password)
            user.save()
            return redirect('/login/')
        except:
            return redirect('/error/')
    else:
        return render(request, "profileUpdate.html")


def error(request):
    return render(request, "error.html")


def modify(request, editid=None, deletetype=None):  # 修改景點資料
    user_name = request.user.username
    item = imgData.objects.get(id=editid)
    markerTypes = markerType.objects.all()  # 取得所有景點
    if request.method == 'POST':
        item.title = request.POST['title']
        item.content = request.POST['content']
        item.lat = request.POST['lat']
        item.lon = request.POST['lon']
        item.type = request.POST['type']
        item.save()
        return redirect('/user_blog/')
    else:
        if deletetype == 'delete':  # 刪除相片
            logger.debug(item.purl.split('https://storage.googleapis.com/webgisapi.appspot.com/')[1])
            photoId = item.purl.split('https://storage.googleapis.com/webgisapi.appspot.com/')[1]
            try:
                blob = bucket.blob(photoId)
                blob.delete()
            except Exception as e:
                print(e)
            else:
                print("File is deleted successfully")
            item.delete()  # 從資料庫移除
            return redirect('/user_blog/')
        return render(request, "modify.html", locals())


def blog(request):
    all = imgData.objects.all().order_by('-id')  # 取得所有景點
    return render(request, "blog.html", locals())


def user_blog(request):
    user_name = request.user.username
    all = imgData.objects.filter(username="{}".format(user_name))
    return render(request, "user_blog.html", locals())
