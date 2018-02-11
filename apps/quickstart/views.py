# -*- coding:utf-8 -*-
from django.contrib.auth.models import User, Group
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    @REST_FRAMWORK API endpoint that allow users to be viewed or edited, 
    查看、编辑用户界面
    """
    queryset = User.objects.all().order_by('-data_joined') # 按照用户添加时间进行逆序排列
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    @REST_FRAMWORK API endpoint that allow groups to be viewed or edited
    查看、编辑 组的界面
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
