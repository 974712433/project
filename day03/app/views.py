import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import User, Person, IDCard, Grade, Student, UserModel, Goods


def index(request):
    return render(request, 'index.html')

# 添加用户
def adduser(request):
    user = User()
    user.name = '李'+str(random.randrange(1000))
    user.score = random.randrange(1,100)
    user.save()

    return HttpResponse('添加成功')

# 显示用户
def showuser(request):
    #全部信息
    #users = User.objects.all()

    #逻辑删除
    #users = User.objects.filter(isdelete=False)

    # 自定义管理器后
    users = User.myObjects.all()
    temp =''
    for user in users:
        temp += '<p>{}-{}-{}分<p>'.format(user.id,user.name,user.score)
    return HttpResponse(temp)

# 更新
def updateuser(request):
    user = User.myObjects.last()
    user.score = 99
    user.save()
    return HttpResponse('更新成功(%s)'% user.name)

# 删除
def daleteuser(request):
    user = User.myObjects.first()
    user.delete()
    user.save()
    return HttpResponse('删除成功(%s)'% user.name)


####################
# 一对一
# 人 和 身份证(一个人对应一张身份证(身份证号码))

# 添加人
def addperson(request):
    person = Person()
    person.p_name = '小张'+str(random.randrange(1000))
    person.p_age = random.randrange(18,100)
    person.save()
    return HttpResponse('添加成功'+ person.p_name)

# 添加卡
def addcard(request):
    card = IDCard()
    card.i_num ='5202211995'+ str(random.randrange(1000,9999))
    temp = random.randrange(0,2)
    if temp:
        card.i_sex = '男'
    else:
        card.i_sex = '女'
    card.i_addr = '深圳市南山区'


    #绑定

    person = Person.objects.last()
    card.i_person = person

    card.save()
    return HttpResponse('添加卡成功--(%s)'% person.p_name)

# 删除一个人
def delperson(request):
    person = Person.objects.last()
    person.delete()
    return HttpResponse('(%s)--死了'% person.p_name)

# 注销卡
def delcard(request):
    card = IDCard.objects.last()
    card.delete()
    return HttpResponse('注销卡成功')

# 卡找人
def getcard(request):
    card = IDCard.objects.last()

    # 获取卡 对应 人的信息
    person = card.i_person
    return HttpResponse('身份证{},姓名{},年龄{}'.format(card.i_num, person.p_name, person.p_age))

# 人找卡
def getperson(request):
    person = Person.objects.last()

    # 获取人 对应 卡的信息 [隐藏属性  表名小写]

    card = person.idcard
    return HttpResponse('姓名{},年龄{},身份证{}'.format(person.p_name,person.p_age,card.i_num))



######### 一对多 ############
# 一个班级 对应 多个学生

# 天加班级
def addgrade(request):
    grade = Grade()
    grade.g_name = 'Python18'+str(random.randrange(10,18))
    grade.save()
    return HttpResponse('添加班级成功'+ grade.g_name)

# 添加学生
def addstu(request):
    stu = Student()
    stu.s_name = str(random.randrange(1000))+'张珊'
    stu.s_age = random.randrange(18,30)
    stu.s_detail = '好好学习 天天向上'

    # 班级
    grade = Grade.objects.last()
    stu.s_grade_id = grade.id
    stu.save()

    return HttpResponse('班级 (%s) 添加学生 (%s)' % (grade.g_name, stu.s_name))

# 删除班级
def delgrade(request):
    grade = Grade.objects.last()
    grade.delete()

    return HttpResponse('删除班级成功')

# 学生获取班级信息
def getstugrade(request):
    stu = Student.objects.last()

    # 从表获取主表信息
    grade  = stu.s_grade

    return HttpResponse('%s 是 %s'%(stu.s_name,grade.g_name) )

#获取班级学生信息
def getgradestu(request):
    grade = Grade.objects.last()
    # 主表获取从表信息
    # student_set 类似于objcets
    students = grade.student_set.all()
    temp ='<p>{}<p>'.format(grade.g_name)
    for student in students:
        temp += '<p>姓名:{},年龄{},描述{}<p>'.format(student.s_name,student.s_age,student.s_detail)
    return HttpResponse(temp)



###### 多对多 #######

# 添加用户
def addusermodel(request):
    user = UserModel()
    user.u_name = str(random.randrange(1000))+ '小李'
    user.save()
    return HttpResponse('添加用户'+user.u_name)

# 添加商品
def addgoods(request):
    goods = Goods()
    goods.g_name = 'iPhone'+ str(random.randrange(1000))
    goods.g_price = random.randrange(10000)
    goods.save()
    return HttpResponse('商品添加'+ goods.g_name)

# 加购物车
def addcart(request):
    user = UserModel.objects.last()
    goods = Goods.objects.last()

    # 添加集合
    goods.g_user.add(user)

    return HttpResponse('添加购物车成功')

# 显示购物车
def showcart(request):
    # 一个用户 对应 多个商品
    user = UserModel.objects.last()
    goods_list = user.goods_set.all()

    temp ='<h1>{}</h1>'.format(user.u_name)
    for goods in goods_list:
        temp += '<p>名称{},价格{}<p>'.format(goods.g_name,goods.g_price)
    return HttpResponse(temp)

# 添加收藏
def addcollect(request):
    user = UserModel.objects.last()
    goods = Goods.objects.last()

    #
    goods.g_user.add(user)

    return HttpResponse('%s 被 %s 收藏成功'% (goods.g_name,user.u_name))

# 显示商品收藏数量
def showgoods(request):
    goods_list = Goods.objects.all()
    temp =''
    for goods in goods_list:
       # 获取用户
        users = goods.g_user.all()
        temp += '<p>名称{},价格{},---{}<p>'.format(goods.g_name, goods.g_price,users.count())

    return HttpResponse(temp)