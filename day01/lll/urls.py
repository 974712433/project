from django.conf.urls import url

from lll import views

urlpatterns = [
    url(r'^index/$', views.index),
]