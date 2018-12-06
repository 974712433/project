from django.db import models

# Create your models here.

#objects管理器,是Manager对象 系统自带

#自定义管理器
class UserManager(models.Manager):
    # 重写父类方法
    def all(self):
        # 调用父类方法获取所有数据
        # 按需求操作
        return super().all().filter(isdelete=False)


class User(models.Model):
    name = models.CharField(max_length=80)
    score = models.IntegerField()
    isdelete = models.BooleanField(default=False)

    # 如果没有自定义管理器,默认是系统的objects

    myObjects = UserManager()

    #元选项
    class Meta:
        # 表名
        db_table = 'user'
        #排序
        ordering = ['-score']





###################### 一对一 #############


# 主表
class Person(models.Model):
    p_name = models.CharField(max_length=80)
    p_age = models.IntegerField()

# 从表
class IDCard(models.Model):
    i_num = models.CharField(max_length=40)
    i_sex = models.CharField(max_length=8)
    i_addr = models.CharField(max_length=100)
    # 在从表中声明关系
    #i_person = models.OneToOneField(Person,models.CASCADE)

    # 保护模式
    i_person = models.OneToOneField(Person)
    # 通过外键实现表与表之间的关联,通过唯一约束从而达到一对一

    # 删除模式
    # 默认是models.CASECADE模型,会删除级联数据
    # 当人删除时,对应身份证也会被删除

    # models.PROTECT 保护模式
    # 当人删除时,身份证不存在,直接删除

    # models.SET_NULL, null=True 设置为空
    # 当人删除时,身份证存在,将身份证中 i_person  设置为空

    # models.SET_DEFAULT default=1
    # 当人删除时,身份证存在,将身份证中 i_person  设置为默认值




######### 一对多 ############
# 一个班级 对应 多个学生

class Grade(models.Model):
    g_name = models.CharField(max_length=40)


class Student(models.Model):
    s_name = models.CharField(max_length=40)
    s_age = models.IntegerField()
    s_detail = models.CharField(max_length=100)

    # 声明关系
    s_grade = models.ForeignKey(Grade,on_delete=models.SET_DEFAULT,default=1)




###### 多对多 #######

# 用户和商品 多对多
# 一个用户 对应 收藏多个商品
# 一个商品 对应 多个用户收藏

# 用户模型
class UserModel(models.Model):
    u_name = models.CharField(max_length=100)


# 商品模型
class Goods(models.Model):
    g_name = models.CharField(max_length=100)
    g_price = models.FloatField()

    # 多对多关
    g_user = models.ManyToManyField(UserModel)