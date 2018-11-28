import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from elema.models import Student, Dog


def index(request):
    return render(request,'index.html')


def addstudent(request):
    # 實例化對象
    stu = Student()
    # 對象中的屬性
    stu.name = '張珊-' + str(random.randrange(1, 1000))
    stu.age = random.randrange(18, 30)
    stu.English = random.randrange(0, 100)
    stu.math = random.randrange(0, 100)
    stu.dateil = '好好學習 天天向上'
    stu.weight = 80.5555555
    stu.wwigth2 = 100.333333

    stu.save()
    return HttpResponse('成功')

def showDog(request):
    # dog = Dog()
    #
    # dog.name = '小花花'
    # dog.age = 2
    # dog.sex = '女'
    #
    # dog.save()
    return HttpResponse('添加狗成功')


def showstu(request):
    # 所有
    #students = Student.objects.all()


    #filter()  找符合要求的條件
    # id大於3的
    #students = Student.objects.filter(id=3)

    #數學成績大於60
    #students = Student.objects.filter(math__gt=60)

    #英語成績大於60 數學大於60
    #students = Student.objects.filter(English__gt=60,math__gt=60)

    # exclude() 過濾符合要求的
    #students = Student.objects.exclude(English=60)

    #order_by() 排序

    #students = Student.objects.order_by('math') #math  -math  沒有-號升序    有-號表示降序

    # 包含'3'
    #students = Student.objects.filter(name__contains='3')

    # 以3結尾
    #students = Student.objects.filter(name__endswith='3')

    # 以3開頭
    #students = Student.objects.filter(name__startwith='3')
    # in
    students = Student.objects.filter()



    student_str = ''
    for student in students:
        student_str += '<p>{}-{} 英語成績:{},數學成績:{},體重:{}kg,<p>'.format(student.id,student.name,student.English,student.math,student.weight)
    return HttpResponse(student_str)


def cart(request):
    return HttpResponse('購物車')


def stu(request):

    #get() 符合要求的
    # student = Student.objects.get(id=3)  id=3的
    # 數據如果不存在  DoesNoteExist  異常

    #student = Student.objects.get(id=3)

    student = Student.objects.filter(math=100)
    if student.count():
        student = student.first()


        temp = '<p>{}-{} 英語成績:{},數學成績:{},體重:{}kg,<p>'.format(student.id, student.name, student.English,
                                                                 student.math, student.weight)
        return HttpResponse(temp)
    else:
        return HttpResponse('沒有該學生')