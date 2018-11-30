from email.mime import image

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('hello')


def home(request):
    name = '张山'
    username = ''
    title = '美团.首页'

    grades = ['pt1810','pt1811','py1812']
    goods = []

    if name:
        pass
    else:
        pass
    return render(request,'home.html',context={'goods':goods,'grades':grades,'name':name,'title':title,'username':username})


# 验证码
from PIL import Image,ImageDraw,ImageFont

import random

import io

def verifycode(request):
    # 创建图片
    width = 100
    height = 50
    bgcolor = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))

    image = Image.new('RGB',(width,height),bgcolor)

    # 产生随机数
    temp_str = '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    random_str = ''
    for i in range(0,4):
        random_str += temp_str[random.randrange(0,len(temp_str))]

    # 绘制随机数
    # 创建画笔
    draw = ImageDraw.Draw(image)

    # 字体

    font = ImageFont.truetype('字体路径',40)
    # 颜色
    f_color1 = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
    f_color2 = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
    f_color3 = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
    f_color4 = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))


    # 绘制4个文字
    draw.text(5,5),random_str[0],fill=f_color1,font=font

    # 文件操作
    buff = io.IOBase()
    image.save(buff,'png')
