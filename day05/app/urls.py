from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^goods/$', views.goods,name='goods1'), # 默认
    url(r'^goods/(\d+)$', views.goods,name='goods2'), # 一个分组即一个参数
    url(r'^sum/(\d+)/(\d+)/(\d+)/$',views.sum,name='sum'),# 多个参数
    url(r'^goindex/$',views.goindex,name='goindex'),
    url(r'^gogoods/$',views.gogoods,name='gogoods'),
    url(r'^gosum/$',views.gosum,name='gosum'),
    url(r'^test500/$',views.test500,name='test500$'),
    url(r'^requesttest/$',views.requesttest,name='requesttest'),
    url(r'^gettest/$',views.gettest,name='gettest'),
    url(r'^register/$',views.register,name='register'),
    url(r'^exit/$',views.exit,name='exit'),
    url(r'^login/$',views.login,name='login'),
]