from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from app.models import User


def index(request):
    # 获取用户信息
    username = request.COOKIES.get('username')
    return render(request,'index.html',context={'username':username})

# 视图函数中 第一个参数默认是request,
# 是客户端发起请求 Django接受到请求 后系统生成的
# 参数和url中正则规则分组个数对应
def goods(request,num=1):
    temp = '第%s页' % num
    return HttpResponse(temp)


def sum(request, a=1, b=1, c=1):
    temp = '%s-%s-%s'%(a, b, c)
    return HttpResponse(temp)


def goindex(request):
    #return HttpResponse('返回首页')
    # 从定向首页
    #return redirect('/')
    # 反向解析(不带参数)'namespace:name'
    return redirect('mt:index')


def gogoods(request):
    # 反向解析(带一个参数)
    return redirect('mt:goods2',10)


def gosum(request):
    # 反向解析 (多个参数)
    return redirect('mt:sum',10,50,12)


def test500(request):
    return None


def requesttest(request):
    # 请求路劲
    # path = request.path
    data = {
        '请求路径path':request.path,
        '请求方式method':request.method,
        '浏览器相关信息encoding':str(request.encoding),
        'get请求参数':str(request.GET),
        '文件参数':request.FILES,
        'cookie':request.COOKIES,



    }
    return HttpResponse(data)


def gettest(request):
    # 获取git请求参数
    name = request.GET['name']
    return HttpResponse('名字'+name)


def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    elif request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        tel = request.POST.get('tel')
        print(username,password,tel)

        #存到数据库
        user = User()
        user.username = username
        user.password = password
        user.tel = tel
        user.save()
        response = redirect('mt:index')

        # 设置cookie
        response.set_cookie('username',username)

        return response


def exit(request):
    response = redirect('mt:index')

    # 删除cookie
    response.delete_cookie('username')
    return response


def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        users = User.objects.filter(username=username).filter(password=password)
        if users.count(): #  ok
            respones =

    return None