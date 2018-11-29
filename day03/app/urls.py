from django.conf.urls import url

from app import views

urlpatterns=[
    url(r'^$', views.index),
    url(r'^adduser/$', views.adduser),
    url(r'^showuser/$', views.showuser),
    url(r'^updateuser/$',views.updateuser),
    url(r'^deleteuser/$',views.daleteuser),
# 添加人
    url(r'^addperson/$',views.addperson),

# 添加卡
    url(r'^addcard/$',views.addcard),

# 删除人
    url(r'^delperson/$',views.delperson),

# 删除卡
    url(r'^delcard/$',views.delcard),

# 人找卡
    url(r'^getperson/$',views.getperson),

# 卡找人
    url(r'^getcard/$', views.getcard),



# 添加班级
    url(r'^addgrade/$',views.addgrade),

# 添加学生
    url(r'^addstu/$',views.addstu),

# 删除班级
    url(r'^delgrade/$',views.delgrade),

# 学生对应班级信息
    url(r'^getstugrade/$',views.getstugrade),

# 班级对应学生
    url(r'^getgradestu/$',views.getgradestu),



# 多对多
    #添加用户
    url(r'^addusermodel/$',views.addusermodel),

    # 添加商品
    url(r'^addgoods/$',views.addgoods),

    # 添加购物车
    url(r'^addcart/$',views.addcart),

    # 查看购物车
    url(r'^showcart/$',views.showcart),

    # 添加收藏
    url(r'^addcollect/$',views.addcollect),

    # 显示商品(收藏数)
    url(r'^showgoods/$',views.showgoods),









]