# _*_coding:utf_8_*_
# @Time :2021/8/2023:30
# Author :焕
# @File :urls.py
from django.urls import path
from photo.views import home, upload

# App名称
# 用于Django幕后的url查询
app_name = 'photo'

# url列表
urlpatterns = [
    path('', home, name='home'),
    path('upload/', upload, name='upload'),
]