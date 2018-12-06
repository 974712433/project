from django.contrib import admin

# Register your models here.
# 注册后,后台站点会帮我们管理


# 自定义管理页面
class WhellAdmin(admin.ModelAdmin):

    # 显示列表
    list_display = ['pk','detail','img']


    # 过滤字段
    list_filter = ['goodsid']


    # 收索
    search_fields = ['pk','detail']

    # 分页(每页显示)

    list_per_page = 3


    # 添加页(修改页面)显示顺序
    fields = ['detail','img','goodsid']
from app.models import wheel, Grade, Student, Book

admin.site.register(wheel,WhellAdmin)


# 关联关系
class StudnetInfo(admin.TabularInline):
    model = Student
    extra = 3





admin.site.register(wheel,WhellAdmin)

class GradeAdmin(admin.ModelAdmin):
    list_display = ['pk','g_name']
admin.site.register(Grade,GradeAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ['pk','s_name','s_age','s_score',"s_grade"]
admin.site.register(Student,StudentAdmin)


# 注册富文本
admin.site.register(Book)

