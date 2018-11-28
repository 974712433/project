from django.conf.urls import url

from taobao import views

urlpatterns = {
    url(r'^$', views.index),
    url(r'^index/$', views.index),
}