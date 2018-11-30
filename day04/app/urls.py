from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/$', views.index),
    url(r'^hone$',views.home)
]