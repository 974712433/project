from django.conf.urls import url

from elema import views

urlpatterns = {
    url(r'^$',views.index),
    url(r'^index$',views.index),
    url(r'^addstudent/$', views.addstudent),
    url(r'^showDog$', views.showDog),
    url(r'^showstu/$',views.showstu),
    url(r'^cart/$',views.cart),
    url(r'^stu/$',views.stu)



}