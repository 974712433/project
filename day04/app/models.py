from django.db import models

# Create your models here.
# class Cat(models.Model):
#     name = models.CharField(max_length=40)
#     color = models.CharField(max_length=40)
#     age = models.IntegerField()
#     bark = models.CharField(max_length=100)
#
# class Dog(models.Model):
#
#     name =
# 动物 模型类
class Aniaml(models.Model):
        name = models.CharField(max_length=40)
        color = models.CharField(max_length=40)
        age = models.IntegerField()
        run = models.CharField(max_length=100)

        class Meta:
            abstract = True


class Cat(Aniaml):
    bark = models.CharField(max_length=100)


class Dog(models.Model):
    eat = models.CharField(max_length=100)