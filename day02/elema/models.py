from django.db import models

# Create your models here.

# 定義模型
# 默認 對應字段是不能爲空的
class Student(models.Model):
    # id默認系統自動添加(主鍵,自增長)
    name = models.CharField(max_length=100)
    #score = models.IntegerField(null=True)
    age = models.IntegerField(null=True)
    English = models.IntegerField(default=0)
    math = models.IntegerField(default=0)
    dateil = models.TextField(default='')
    weight = models.FloatField(default=0.0)
    wwigth2 = models.DecimalField(default=0.0, max_digits=4, decimal_places=1)
    cerate_time = models.DateTimeField(auto_now=True)
    isdelete = models.BooleanField(default=False)


class Dog(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField
    sex = models.CharField(max_length=50)