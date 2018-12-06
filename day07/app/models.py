from django.db import models

# Create your models here.
from tinymce.models import HTMLField


class wheel(models.Model):
    img = models.ImageField()
    detail = models.CharField(max_length=100)
    goodsid = models.IntegerField()
    #
    # def __str__(self):
    #     return '{}-{}'.format(self.detail,self.img)


class Grade(models.Model):
    g_name = models.CharField(max_length=100)
    def __str__(self):
        return '{}'.format(self.g_name)


class Student(models.Model):
    s_name = models.CharField(max_length=100)
    s_age = models.ImageField()
    s_score = models.ImageField()

    # 关系声明

    s_grade = models.ForeignKey(Grade)


class Book(models.Model):
    s_title = models.CharField(max_length=100)
    s_time = models.DateTimeField(auto_now=True)
    s_content = HTMLField()

    def __str__(self):
        return self.s_title